import imageio
import matplotlib.pyplot as plt
import numpy as np

for k in range(13):
    image = imageio.imread("parcoursProfondeur"+str(k)+".png")
    imageCrop = image[230:605,360:670,:].copy()
    n, p, _ = imageCrop.shape
    for i in range(n):
        for j in range(p):
            if not (imageCrop[i,j,:] - np.array([255, 255, 255, 255])).any() :
                imageCrop[i,j,:] = np.array([255, 255, 255, 0])
    # plt.imshow(imageCrop)
    # plt.show()
    imageio.imwrite("parcoursProfondeurCrop"+str(k)+".png", imageCrop)


# i = 0
# image = imageio.imread("parcoursProfondeur"+str(i)+".png")
# imageCrop = image[230:605,360:670,:]
# plt.imshow(image)
# plt.show()
# plt.imshow(imageCrop)
# plt.show()
