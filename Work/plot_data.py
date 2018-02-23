import numpy as np
import matplotlib.pyplot as plt
#import plotly.plotly as py


file = open('/home/rushabh/Project/logs/seperate_id_data_2/324.log','r')

num_lines = sum(1 for line in file)
print(num_lines)
i = 0
file = open('/home/rushabh/Project/logs/seperate_id_data_2/324.log','r')

x = np.zeros(num_lines+1)
y1 = np.zeros(num_lines+1)
y2 = np.zeros(num_lines+1)
y3 = np.zeros(num_lines+1)
y4 = np.zeros(num_lines+1)
y5 = np.zeros(num_lines+1)
y6 = np.zeros(num_lines+1)
y7 = np.zeros(num_lines+1)
y8 = np.zeros(num_lines+1)
y9 = np.zeros(num_lines+1)
y10 = np.zeros(num_lines+1)
y11 = np.zeros(num_lines+1)
y12 = np.zeros(num_lines+1)


for line in file.readlines():

	#data[i][]
	A = line.split('\t')
	B = line.split(':')

	x[i] = int(B[0])
	#x[i] = int(A[8],16)
	y1[i] = int(A[1],16)
	y2[i] = int(A[2],16)
	y3[i] = int(A[3],16)
	y4[i] = int(A[4],16)
	y5[i] = int(A[5],16)
	y6[i] = int(A[6],16)
	y7[i] = int(A[7],16)
	y8[i] = int(A[8],16)

	y9[i] = int(A[1]+A[2],16)
	y10[i] = int(A[3]+A[4],16)
	y11[i] = int(A[5]+A[6],16)
	y12[i] = int(A[7]+A[8],16)
	#plt.plot(x, y, "o")
	#plt.show('1')
	#plt.close('all')
	i+=1

plt.plot(x, y1, "o", color='pink', alpha=0.6)
plt.plot(x, y2, "o", color='green', alpha=0.6)
plt.plot(x, y3, "o", color='black', alpha=0.6)
# plt.plot(x, y4, "o", color='cyan', alpha=0.6)
plt.plot(x, y5, "o", color='chocolate', alpha=0.6)
plt.plot(x, y6, "o", color='blue', alpha=0.6)
plt.plot(x, y7, "o", color='red', alpha=0.6)
plt.plot(x, y8, "o", color='yellow', alpha=0.6)
# plt.plot(x, y9, "o", color='maroon', alpha=0.6)
# plt.plot(x, y10, "o", color='magenta', alpha=0.6)
# plt.plot(x, y11, "o", color='orange', alpha=0.6)
# plt.plot(x, y12, "o", color='turquoise', alpha=0.6)
plt.show()