import imageio
import matplotlib.pyplot as plt
import numpy as np

for k in range(10):
    image = imageio.imread("parcoursLargeur"+str(k)+".png")
    imageCrop = image[190:630,320:700,:].copy()
    n, p, _ = imageCrop.shape
    for i in range(n):
        for j in range(p):
            if not (imageCrop[i,j,:] - np.array([255, 255, 255, 255])).any() :
                imageCrop[i,j,:] = np.array([255, 255, 255, 0])
    # plt.imshow(imageCrop)
    # plt.show()
    imageio.imwrite("parcoursLargeurCrop"+str(k)+".png", imageCrop)


# i = 0
# image = imageio.imread("parcoursLargeur"+str(i)+".png")
# imageCrop = image[190:630,320:700,:]
# plt.imshow(image)
# plt.show()
# plt.imshow(imageCrop)
# plt.show()
