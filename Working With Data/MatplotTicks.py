import numpy as np 
import matplotlib.pyplot as plt

films=["Film 1"," Film 2","Film 3"," Film 4"]
awards=[3,9,1,5]

plt.bar(films,awards)
plt.title("Top Films")
plt.ylabel("Number of awards")
plt.show()