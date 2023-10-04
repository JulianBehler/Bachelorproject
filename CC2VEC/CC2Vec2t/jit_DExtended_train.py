from jit_DExtended_model import DeepJITExtended
import torch 
from tqdm import tqdm
from jit_utils import mini_batches_update_DExtended
import torch.nn as nn
import os, datetime
from jit_utils import save
from collections import Counter
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler

def train_model(data, params):
    cc2ftr, data_pad_msg, data_pad_code, data_labels, dict_msg, dict_code = data
    
    # set up parameters
    params.cuda = (not params.no_cuda) and torch.cuda.is_available()
    del params.no_cuda
    params.filter_sizes = [int(k) for k in params.filter_sizes.split(',')]

    params.save_dir = os.path.join(params.save_dir, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

    params.vocab_msg, params.vocab_code = len(dict_msg), len(dict_code)
    params.embedding_ftr = cc2ftr.shape[1]

    if len(data_labels.shape) == 1:
        params.class_num = 1
    else:
        params.class_num = data_labels.shape[1]
    params.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # create and train the defect model
    model = DeepJITExtended(args=params)
    if torch.cuda.is_available():
        model = model.cuda()
    optimizer = torch.optim.Adam(model.parameters(), lr=params.l2_reg_lambda)
    criterion = nn.BCELoss()
    
    print("normal")
    X_ftr= cc2ftr
    X_msg=data_pad_msg
    X_code=data_pad_code
    Y=data_labels
    
    print("Oversampling")
    print('Original dataset shape %s' % Counter(Y))
    print(len(X_ftr))
    print(len(X_msg))
    print(len(X_code))
    print(X_code.shape)
    print(X_code.ndim)
    X_code = X_code.reshape((X_code.shape[0], -1))

    ros = RandomOverSampler()
    #ros = RandomOverSampler(random_state=24)
    X_ftr2, y_res0 = ros.fit_resample(X_ftr,Y)
    X_code2,  y_res = ros.fit_resample(X_code, Y)
    X_msg2, y_res2 = ros.fit_resample(X_msg, Y)
    print('Resampled dataset shape %s' % Counter(y_res))
    print(len(X_ftr2))
    print(len(X_msg2))
    print(len(X_code2))
    print(X_code2.shape)
    print(X_code2.ndim)
    
    data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    cc2ftr= X_ftr2
    data_pad_msg= X_msg2
    data_labels=y_res2
    print(len(data_pad_code))
    print(data_pad_code.shape) 
    
    
    """
    
    #under sampling
    print("Undersampling")
    print('Original dataset shape %s' % Counter(Y))
    X_code = X_code.reshape((X_code.shape[0], -1))
    #undersampler = RandomUnderSampler(sampling_strategy="majority",random_state=42)
    undersampler = RandomUnderSampler(sampling_strategy="majority")
    X_ftr2, y_res0 = undersampler.fit_resample(X_ftr,Y)
    X_code2, y_res = undersampler.fit_resample(X_code, Y)
    X_msg2, y_res2 = undersampler.fit_resample(X_msg, Y)

    data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    cc2ftr= X_ftr2
    data_pad_msg= X_msg2
    data_labels=y_res2
    

    print(len(X_code2))
    print(len(X_msg2))
    print('Resampled dataset shape %s' % Counter(y_res))
    """
   
   
    """
    #smote

    print("smote")
    print('Original dataset shape %s' % Counter(Y))
    print(len(X_ftr))
    print(len(X_msg))
    print(len(X_code))
    print(X_code.shape)
    print(X_code.ndim)
    X_code = X_code.reshape((X_code.shape[0], -1))
    smote = SMOTE(random_state=None)
   
    X_ftr2, y_res0 = smote.fit_resample(X_ftr,Y)
    X_code2,  y_res = smote.fit_resample(X_code, Y)
    X_msg2, y_res2 = smote.fit_resample(X_msg, Y)
    print('Resampled dataset shape %s' % Counter(y_res))
    print(len(X_ftr2))
    print(len(X_msg2))
    print(len(X_code2))
    print(X_code2.shape)
    print(X_code2.ndim)
    
    data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    cc2ftr= X_ftr2
    data_pad_msg= X_msg2
    data_labels=y_res2
    print(len(data_pad_code))
    print(data_pad_code.shape) 
    """

    for epoch in range(1, params.num_epochs + 1):
        total_loss = 0
        # building batches for training model
        batches = mini_batches_update_DExtended(X_ftr=cc2ftr, X_msg=data_pad_msg, X_code=data_pad_code, Y=data_labels)
        for i, (batch) in enumerate(tqdm(batches)):
            ftr, pad_msg, pad_code, labels = batch
            if torch.cuda.is_available():
                ftr = torch.tensor(ftr).cuda()
                pad_msg, pad_code, labels = torch.tensor(pad_msg).cuda(), torch.tensor(
                    pad_code).cuda(), torch.cuda.FloatTensor(labels)
            else:
                ftr = torch.tensor(ftr).long()
                pad_msg, pad_code, labels = torch.tensor(pad_msg).long(), torch.tensor(pad_code).long(), torch.tensor(
                    labels).float()

            optimizer.zero_grad()
            predict = model.forward(ftr, pad_msg, pad_code)
            loss = criterion(predict, labels)
            total_loss += loss
            loss.backward()
            optimizer.step()

        print('Epoch %i / %i -- Total loss: %f' % (epoch, params.num_epochs, total_loss))    
        save(model, params.save_dir, 'epoch', epoch)
