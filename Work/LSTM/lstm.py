import numpy as np
import h5py
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import GRU
from keras.utils import np_utils
from keras.layers import TimeDistributed
import os

data_file = open('/home/rushabh/Project/logs/seperate_id_data_2/158_bin.log','r')

X = np.zeros(64, dtype = np.int8)

data_len = 5000

aaa = 0
for line in data_file:
	#print line,
	if aaa<=41500:
		aaa+=1
		continue
	elif aaa>46500:
		break
	a = line[:64]
	xxx = [int(i) for i in a]
	a = np.array(xxx)
	if aaa==41501:
		X = a
		#print X
	else:
		X = np.vstack((X,a))
	aaa+=1


full_data = X
X = X[range(1,data_len)]
# test_data = full_data[range(data_len+1,2*data_len)]
full_data = X

true_data_len = X.shape[0]
print(true_data_len)


seq_length = 15
dataX = []
dataY = []
for i in range(0, len(X) - seq_length):
	seq_in = X[i : i+seq_length]
	seq_out = X[i + seq_length]
	dataX.append([data for data in seq_in])
	dataY.append(seq_out)

print(np.array(dataY).shape)
X = np.reshape(dataX, (len(dataX), seq_length, 64))
# y = np_utils.to_categorical(dataY)
y = np.array(dataY)
# print(y.shape)


model = Sequential()
model.add(Dense(128, activation='tanh', input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(128, activation='tanh'))
model.add(LSTM(128, activation='tanh', return_sequences=True))
model.add(LSTM(128, stateful= False, activation='tanh'))
model.add(Dense(y.shape[1], activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=150, batch_size=400, verbose=2, shuffle=False)

# model.save('/home/rushabh/Project/trained_models/')

scores = model.evaluate(X, y, verbose=0)
print("Model Accuracy: %.2f%%" % (scores[1]*100))

# serialize model to JSON
model_json = model.to_json()

file_path = "trained_models/model"
abc = 0
for i in range(100):
	if not os.path.exists(file_path+str(i+1)+'.json'):
		file_path+=str(i+1)
		abc = i+1
		break

with open(file_path+".json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights(file_path+".h5")
print("Saved model", abc, "to disk")
 

