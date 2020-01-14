# coding=UTF-8
import numpy as np
from keras.utils import np_utils
from keras.models import load_model


model = load_model('model.h5')

lab_num = ['小雲雀', '石燕', '竹雞', '灰樹鵲', '白頭翁']
x = [46, 53, 45, 16, 15]

x = np_utils.to_categorical(x, 65).tolist()
x = np.reshape(x, (1,5*65)).astype('float32')

print(np.shape(x))

predictions = model.predict_classes(x)
print(lab_num[predictions[0]])
