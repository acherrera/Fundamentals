import numpy as np
import matplotlib.pyplot as plt


length = 100
y = [np.sin(i/np.pi) for i in range(length)]
""" This is a very useful syntax for creating an array/list.
Save a lot of space and some time for creating lists.
Does the same thing as the following:
y = []
for i in range(length):
    y.append(np.sin(i/np.pi))
"""

x = [i for i in range(length)]

# How to actually plot this:
plt.plot(x, y)
plt.title("Some Title")
plt.xlabel("This is the X label")
plt.ylabel("This is the y label")

plt.show()
