from keras.models import model_from_json
import numpy as np



data_file = open('/home/rushabh/Project/logs/seperate_id_data_2/158_bin.log','r')

X = np.zeros(64, dtype = np.int8)

data_len = 3600#4000

aaa = 0
for line in data_file:
	#print line,
	if aaa<=2400:#28600:
		aaa+=1
		continue
	elif aaa>6000:#32600:
		break
	a = line[:64]
	xxx = [int(i) for i in a]
	a = np.array(xxx)
	if aaa==2401:#28601:
		X = a
		#print X
	else:
		X = np.vstack((X,a))
	aaa+=1

X = X[range(1,data_len)]



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



 
file_path = 'trained_models/model8'
# load json and create model
json_file = open(file_path+'.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights(file_path+'.h5')
print("Loaded model from disk")
 
# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
score = loaded_model.evaluate(X, y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))