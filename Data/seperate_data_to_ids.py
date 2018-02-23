import numpy as np
import os.path

file = open('C:\\Users\\Rushabh\\Desktop\\CanBus\\temp.log','r')

num_lines = sum(1 for line in file)
#print(num_lines)
i = 0
file = open('C:\\Users\\Rushabh\\Desktop\\CanBus\\city_data_3.log','r')
sepIDLoc = 'C:\\Users\\Rushabh\\Desktop\\CanBus\\seperate_id_data_3\\'
#time = np.zeros(num_lines)
#ids = np.zeros(shape=(num_lines), dtype=str)
#data = np.zeros(shape=(num_lines), dtype='S100')
for line in file.readlines():
	if(line[0]>='0' and line[0]<='9'):
		#data[i][]
		A = line.split(';')
		time = (A[0])
		#print(A[1].split('\t'))
		ids = ((((A[1].split('\t'))[1]).split(':')[0]))
		data = (line.split(':')[1])
		#data[i][0] = A[0]
		#A = A[1].split(':')
		#data[1]
		if os.path.exists(sepIDLoc + ids + '.log'):
			g=open(sepIDLoc + ids  + '.log','a')
			g.write(time + " : " + data)
		else:
			g=open(sepIDLoc + ids  + '.log','w')
			g.write(time + " : " + data)
		#print(np.array((A[1].split('\t'))[1]))
		i+=1

# for i in range(num_lines):
# 	if os.path.exists(sepIDLoc + str(ids[i]) + '.log'):
# 		g=open(sepIDLoc + str(ids[i])  + '.log','a')
# 		g.write(str(time[i]) + " : " + str(data[i]))
# 	else:
# 		g=open(sepIDLoc + str(ids[i])  + '.log','w')
# 		g.write(str(time[i]) + " : " + str(data[i]))