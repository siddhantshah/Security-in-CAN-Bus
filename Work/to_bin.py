import numpy as np
import os.path
import binascii

ids = '1D0'
file = open('/home/rushabh/Project/logs/seperate_id_data_2/'+ids+'.log','r')

num_lines = sum(1 for line in file)
#print(num_lines)
i = 0
file = open('/home/rushabh/Project/logs/seperate_id_data_2/'+ids+'.log','r')
sepIDLoc = '/home/rushabh/Project/logs/seperate_id_data_2/'
#time = np.zeros(num_lines)
#ids = np.zeros(shape=(num_lines), dtype=str)
#data = np.zeros(shape=(num_lines), dtype='S100')
for line in file.readlines():

	#data[i][]
	A = line.split(':')
	data = (A[1])

	B = data.split('\t')
	data_len = len(B)
	#print(B)

	bin_data = ''
	for i in range(data_len):
		if(i==0 or i==data_len-1):
			continue
		#print(B[i])
		
		bin_data += str(bin(int(B[i], 16))[2:].zfill(8))
	# time = (A[0])
	# #print(A[1].split('\t'))
	# ids = ((((A[1].split('\t'))[1]).split(':')[0]))
	# data = (line.split(':')[1])
	#data[i][0] = A[0]
	#A = A[1].split(':')
	#data[1]
	if os.path.exists(sepIDLoc + ids+'_bin.log'):
		g=open(sepIDLoc + ids+'_bin.log','a')
		g.write(bin_data + '\n')
	else:
		g=open(sepIDLoc + ids+'_bin.log','w')
		g.write(bin_data + '\n')
	#print(np.array((A[1].split('\t'))[1]))
	i+=1

# for i in range(num_lines):
# 	if os.path.exists(sepIDLoc + str(ids[i]) + '.log'):
# 		g=open(sepIDLoc + str(ids[i])  + '.log','a')
# 		g.write(str(time[i]) + " : " + str(data[i]))
# 	else:
# 		g=open(sepIDLoc + str(ids[i])  + '.log','w')
# 		g.write(str(time[i]) + " : " + str(data[i]))