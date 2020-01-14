# coding=UTF-8

import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
import h5py

#裝標記的list
labels = []
#用來裝one-hot encoding過後的五個頻譜
numbers = []


def timeconnect(yourfile, timeamount, labels):

    newfile = open('new.txt', 'w', encoding='utf-8')

    labs = []
    # label數量
    while labels:
        line = yourfile.readline()
        if len(line) < 5:
            line = yourfile.readline()
        # 從1開始到你要幾行寫成一行資料
        count = 1
        #多行5個數字變成一行數字
        linesnumbers = []
        list0 = line.split()
        #數字與標籤分開
        *numbers, label = list0
        #用來判斷是否與前一個是相同標籤
        labs.append(label)
        pastlabelindex = labs.index(label)

        while line:
            if len(line) < 5:
                pass
            else:
                list0 = line.split()
                *numbers, label = list0
                if label in labs and pastlabelindex == labs.index(label):
                    pass
                else:
                    break
                linesnumbers += numbers
                if count < timeamount:
                    count += 1
                else:
                    str1 = ' '.join(linesnumbers)
                    newfile.write(str1+" "+label+'\n')

                    print(linesnumbers)
                    for i in range(5):
                        linesnumbers.pop(0)
            line = yourfile.readline()
        labels -= 1
    return newfile




#標籤class轉成數字
lab_num = ['小雲雀', '石燕', '竹雞', '灰樹鵲', '白頭翁']
lab_number = []
numberscount = 0


new = open('C:/Users/x240/PycharmProjects/untitled/new.txt', 'r', encoding='utf-8')
#new = timeconnect(f, 20, 5)


line = new.readline()

while line:
    list0 = line.split()
    #將數字資料與class分開
    *number, label = list0
    labels.append(label)
    lab_number.append(lab_num.index(label))
    numbers.append([])
    numbers[numberscount].append(number)
    line = new.readline()
    numberscount += 1


new.close()
print(np.shape(numbers))

#轉為獨熱編碼
numbers = np_utils.to_categorical(numbers, 65).tolist()
numbers = np.squeeze(numbers, axis=(1,))
#numbers = np.reshape(numbers, (numberscount, 5*65)).astype('float32')
print(np.shape(numbers))
numbers = np.reshape(numbers, (numberscount, 100*65)).astype('float32')
print(np.shape(numbers))
print(lab_number)

model = Sequential()
model.add(Dense(units=20,
                input_dim=6500,
                kernel_initializer='normal',
                activation='relu'))
model.add(Dense(units=len(lab_num),
                kernel_initializer='normal',
                activation='softmax'))
print(model.summary())
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

train_history = model.fit(x=numbers,
                          y=lab_number,
                          validation_split=0,
                          epochs=100,
                          batch_size=50,
                          verbose=1)
#保存模型
model.save('model.h5')

