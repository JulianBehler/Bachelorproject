from jit_DExtended_model import DeepJITExtended
from jit_utils import mini_batches_DExtended
   
import torch 
from tqdm import tqdm
from sklearn.metrics import confusion_matrix, roc_auc_score, matthews_corrcoef, precision_recall_fscore_support, classification_report, auc
import math
def evaluation_model(data, params):
    cc2ftr, pad_msg, pad_code, labels, dict_msg, dict_code = data
    batches = mini_batches_DExtended(X_ftr=cc2ftr, X_msg=pad_msg, X_code=pad_code, Y=labels)

    params.vocab_msg, params.vocab_code = len(dict_msg), len(dict_code)
    if len(labels.shape) == 1:
        params.class_num = 1
    else:
        params.class_num = labels.shape[1]
    params.embedding_ftr = cc2ftr.shape[1]

    # set up parameters
    params.cuda = (not params.no_cuda) and torch.cuda.is_available()
    del params.no_cuda
    params.filter_sizes = [int(k) for k in params.filter_sizes.split(',')]

    model = DeepJITExtended(args=params)
    if torch.cuda.is_available():
        model = model.cuda()
    model.load_state_dict(torch.load(params.load_model))

    model.eval()  # eval mode (batchnorm uses moving mean/variance instead of mini-batch mean/variance)
    with torch.no_grad():
        all_predict, all_label = list(), list()
        for i, (batch) in enumerate(tqdm(batches)):
            ftr, pad_msg, pad_code, label = batch
            if torch.cuda.is_available():
                ftr = torch.tensor(ftr).cuda()
                pad_msg, pad_code, labels = torch.tensor(pad_msg).cuda(), torch.tensor(
                    pad_code).cuda(), torch.cuda.FloatTensor(label)
            else:
                ftr = torch.tensor(ftr).long()
                pad_msg, pad_code, label = torch.tensor(pad_msg).long(), torch.tensor(pad_code).long(), torch.tensor(
                    labels).float()
            if torch.cuda.is_available():
                predict = model.forward(ftr, pad_msg, pad_code)
                predict = predict.cpu().detach().numpy().tolist()
            else:
                predict = model.forward(ftr, pad_msg, pad_code)
                predict = predict.detach().numpy().tolist()
            all_predict += predict
            all_label += labels.tolist()
    print(all_label)
    print(all_predict)
    y_true=all_label
    y_score = []
    for each_element in all_predict: 
        if each_element <= 0.5:
            y_score.append(0)
        else:
            y_score.append(1)
    prec, rec, f1, _ = precision_recall_fscore_support(y_true,y_score,average='weighted') # at threshold = 0.5
    tn, fp, fn, tp   = confusion_matrix(y_true,y_score, labels=[0, 1]).ravel()
    print('Test data -- Precision score:', prec)
    print('Test data -- Rexall score:', rec)  
    print('Test data -- f1 score:', f1)
    print(tn)
    print(fp)
    print(fn)
    print(tp)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    print('Accuracy:', accuracy)
    FAR = fp/(fp+tn) # false alarm rate
    dist_heaven = math.sqrt((pow(1-rec,2)+pow(0-FAR,2))/2.0) # distance to heaven
    conf_matrix = confusion_matrix(y_true, y_score)
    per_clas_acc = conf_matrix.diagonal()/conf_matrix.sum(axis=1)
    print(' per-class accuracy score: ', per_clas_acc)
    auc_score = roc_auc_score(y_true=all_label,  y_score=all_predict)
    print('Test data -- AUC score:', auc_score)