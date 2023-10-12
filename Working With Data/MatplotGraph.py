import matplotlib.pyplot as plt
import numpy as np

new_array=np.arange(9,0,-1)

plt.title("Test Graph")
#plt.plot(new_array)
plt.xlabel('" X "')
plt.ylabel('" Y "')

X_array = [1,2,3,4,5,6]
Y_array = [1,4,9,16,25,36]

#plt.plot(X_array,Y_array)

data1= np.arange(2,7,0.3)
plt.plot(data1, data1, "r--", data1, data1**2, "bs", data1, data1**3, "g^")
plt.savefig("DATA_VIS.png")
plt.show()