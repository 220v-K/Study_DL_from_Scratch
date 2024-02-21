# show image
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("Chapter1_HelloPython/pikachu.png")

plt.imshow(img)
plt.show()