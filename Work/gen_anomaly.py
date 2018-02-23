import numpy as np
np.set_printoptions(threshold=np.nan)

data_file = open('/home/rushabh/Project/logs/seperate_id_data_2/1D0_bin.log','r')

X = np.zeros(64, dtype = np.int8)

aaa = 0
for line in data_file:
	#print line,
	a = line[:64]
	xxx = [int(i) for i in a]
	a = np.array(xxx)
	if aaa==0:
		X = a
		#print X
	else:
		X = np.vstack((X,a))
	aaa+=1

data_len = X.shape[0]

prob = X.sum(axis=0)

prob = prob/data_len

print(prob)


anomaly_data_len = 3000

a = np.zeros(64, dtype = np.int8)
for i in range(anomaly_data_len):
	for j in range(64):
		r = np.random.rand()
		if r < prob[j]:
			a[j] = 1
		else:
			a[j] = 0

	if i==0:
		anomaly = a
	else:
		anomaly = np.vstack((anomaly,a))

print(anomaly)


# data_file = open('/home/rushabh/Project/logs/seperate_id_data_2/1D0_anomaly.log','w')

np.savetxt('/home/rushabh/Project/logs/seperate_id_data_2/1D0_anomaly.log', anomaly, fmt='%1u', delimiter='', newline='\n')