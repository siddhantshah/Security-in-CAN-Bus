import numpy as np
import matplotlib.pyplot as plt
#import plotly.plotly as py


file = open('C:\\Users\\Rushabh\\Desktop\\CanBus\\seperate_id_data_2\\221.log','r')

num_lines = sum(1 for line in file)
print(num_lines)
i = 0
file = open('C:\\Users\\Rushabh\\Desktop\\CanBus\\seperate_id_data_2\\221.log','r')

x = np.zeros(num_lines+1)
y = np.zeros(num_lines+1)

for line in file.readlines():

	#data[i][]
	A = line.split('\t')
	#B = line.split(':')
	#print(A)
	#x[i] = int(B[0])
	x[i] = int(A[1],16)
	y[i] = int(A[4],16)
	#plt.plot(x, y, "o")
	#plt.show('1')
	#plt.close('all')
	i+=1

plt.plot(x, y, "o")
plt.show()