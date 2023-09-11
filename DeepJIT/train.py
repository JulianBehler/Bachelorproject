from model import DeepJIT
import torch 
from tqdm import tqdm
from utils import mini_batches_train, save
import torch.nn as nn
import os, datetime
from collections import Counter
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTETomek


def train_model(data, params):
    data_pad_msg, data_pad_code, data_labels, dict_msg, dict_code = data
    
    # set up parameters
    params.cuda = (not params.no_cuda) and torch.cuda.is_available()
    del params.no_cuda
    params.filter_sizes = [int(k) for k in params.filter_sizes.split(',')]

    params.save_dir = os.path.join(params.save_dir, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

    params.vocab_msg, params.vocab_code = len(dict_msg), len(dict_code)    

    if len(data_labels.shape) == 1:
        params.class_num = 1
    else:
        params.class_num = data_labels.shape[1]
    params.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # create and train the defect model
    model = DeepJIT(args=params)
    if torch.cuda.is_available():
        model = model.cuda()
        print("bug")
    optimizer = torch.optim.Adam(model.parameters(), lr=params.l2_reg_lambda)

    criterion = nn.BCELoss()

    #print("normal")
    X_msg=data_pad_msg
    X_code=data_pad_code
    Y=data_labels
    if(params.runtype == "normal"):
        print("normal")
        X_msg=data_pad_msg
        X_code=data_pad_code
        Y=data_labels
    elif params.runtype == "randomOversampling":
        print("randomOversampling")
        X_code = X_code.reshape((X_code.shape[0], -1))
        ros = RandomOverSampler(random_state=42)
        X_code2,  y_res = ros.fit_resample(X_code, Y)
        X_msg2, y_res2 = ros.fit_resample(X_msg, Y)
        data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
        data_pad_msg= X_msg2
        data_labels=y_res2
    elif params.runtype == "randomUndersampling":
        print("randomUndersampling")
        X_code = X_code.reshape((X_code.shape[0], -1))
        undersampler = RandomUnderSampler(sampling_strategy="majority",random_state=1)
        X_code2, y_res = undersampler.fit_resample(X_code, Y)
        X_msg2, y_res2 = undersampler.fit_resample(X_msg, Y)
        data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
        data_pad_msg= X_msg2
        data_labels=y_res2
    elif params.runtype == "SMOTE":
        print("SMOTE")
        X_code = X_code.reshape((X_code.shape[0], -1))
        sm = SMOTE(random_state=1) #Default k_neighbors=5
        X_code2, y_res = sm.fit_resample(X_code, Y)
        X_msg2, y_res2 = sm.fit_resample(X_msg, Y)
        data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
        data_pad_msg= X_msg2
        data_labels=y_res2
    elif params.runtype == "SMOTETomek":
        print("SMOTETomek")
        X_code = X_code.reshape((X_code.shape[0], -1))
        smt = SMOTETomek(random_state=1) #Default k_neighbors=5
        X_code2, y_res = smt.fit_resample(X_code, Y)
        X_msg2, y_res2 = smt.fit_resample(X_msg, Y)
        data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
        data_pad_msg= X_msg2
        data_labels=y_res2

    """  #oversampling
    print("Oversampling")
    print('Original dataset shape %s' % Counter(Y))
    print(len(X_msg))
    print(len(X_code))
    print(X_code.shape)
    print(X_code.ndim)
    X_code = X_code.reshape((X_code.shape[0], -1))

    #ros = RandomOverSampler()
    ros = RandomOverSampler(random_state=42)
    X_code2,  y_res = ros.fit_resample(X_code, Y)
    X_msg2, y_res2 = ros.fit_resample(X_msg, Y)
    print('Resampled dataset shape %s' % Counter(y_res))
    print(len(X_msg2))
    print(len(X_code2))
    print(X_code2.shape)
    print(X_code2.ndim)

    data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    data_pad_msg= X_msg2
    data_labels=y_res2
    print(len(data_pad_code))
    print(data_pad_code.shape)
    #"""

    """ muss gefixed werden
    #under sampling
    #print("Undersampling")
    #print('Original dataset shape %s' % Counter(Y))
    X_code = X_code.reshape((X_code.shape[0], -1))
    undersampler = RandomUnderSampler(sampling_strategy="majority",random_state=1)
    #undersampler = RandomUnderSampler(sampling_strategy="majority")
    X_code2, y_res = undersampler.fit_resample(X_code, Y)
    X_msg2, y_res2 = undersampler.fit_resample(X_msg, Y)

    data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    data_pad_msg= X_msg2
    data_labels=y_res2

    #print(len(X_code2))
    #print(len(X_msg2))
    #print('Resampled dataset shape %s' % Counter(y_res))
    #"""

    """#Smote
    print("SMOTE")
    print('Original dataset shape %s' % Counter(Y))
    X_code = X_code.reshape((X_code.shape[0], -1))
    sm = SMOTE(random_state=1) #Default k_neighbors=5
    X_code2, y_res = sm.fit_resample(X_code, Y)
    X_msg2, y_res2 = sm.fit_resample(X_msg, Y)
    print('Resampled dataset shape %s' % Counter(y_res))
    print(X_code2.shape)
    print(X_code2.ndim)
    data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    data_pad_msg= X_msg2
    data_labels=y_res2
    #"""
    """
    print("SMOTETomek")
    print('Original dataset shape %s' % Counter(Y))
    X_code = X_code.reshape((X_code.shape[0], -1))
    smt = SMOTETomek(random_state=1) #Default k_neighbors=5
    #X_res, y_res = smt.fit_resample(X, y)
    X_code2, y_res = smt.fit_resample(X_code, Y)
    X_msg2, y_res2 = smt.fit_resample(X_msg, Y)
    print('Resampled dataset shape %s' % Counter(y_res))
    print(X_code2.shape)
    print(X_code2.ndim)
    data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    data_pad_msg= X_msg2
    data_labels=y_res2
    #"""
    #data_pad_code= X_code2.reshape(len(X_code2), 10, 512)
    #data_pad_msg= X_msg2
    #data_labels=y_res2


    for epoch in range(1, params.num_epochs + 1):
        total_loss = 0
        # building batches for training model
        batches = mini_batches_train(X_msg=data_pad_msg, X_code=data_pad_code, Y=data_labels)
        for i, (batch) in enumerate(tqdm(batches)):
            pad_msg, pad_code, labels = batch
            if torch.cuda.is_available():                
                pad_msg, pad_code, labels = torch.tensor(pad_msg).cuda(), torch.tensor(
                    pad_code).cuda(), torch.cuda.FloatTensor(labels)
            else:            
                pad_msg, pad_code, labels = torch.tensor(pad_msg).long(), torch.tensor(pad_code).long(), torch.tensor(
                    labels).float()

            optimizer.zero_grad()
            predict = model.forward(pad_msg, pad_code)
            loss = criterion(predict, labels)
            total_loss += loss
            loss.backward()
            optimizer.step()

        print('Epoch %i / %i -- Total loss: %f' % (epoch, params.num_epochs, total_loss))    
        save(model, params.save_dir, 'epoch', epoch)
