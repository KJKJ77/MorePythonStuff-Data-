import numpy as np 
import matplotlib.pyplot as plt

x= np.array([37,27,27,17])
ch_labels = ["first","second","third","fourth"]

plt.pie(x, labels = ch_labels)
plt.title("Pie Chart Testing")
plt.show()