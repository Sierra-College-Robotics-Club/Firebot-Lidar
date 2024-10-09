import math
from matplotlib import pyplot as plt
with open("../rawDataCapture/data.txt", "r", encoding="utf-8") as f:
    data = f.read()
    data = data.split(";")
    for i in range(len(data)):
        data[i] = int(data[i])
print(data)
print(data[0])

yoffset = []
for i in range(len(data)):
    point = (i / len(data)) * math.pi
    yoffset.append(point)
yoffset.reverse()
print(yoffset)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(yoffset,data)
ax.grid(True)

plt.show()
