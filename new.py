from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = Image.open("IMG_8319.jpg")
data = np.asarray(img)
# cau 2
gray_img1 = Image.new("L", img.size)
for x in range(img.width):
    for y in range(img.height):
        r, g, b = img.getpixel((x, y))
        gray_value = int((r + g + b) / 3)
        gray_img1.putpixel((x, y), (gray_value,))
gray_img1.show()

# cau 3

img1 = Image.open("IMG_8319.jpg")
img_array = np.array(img) / 255.0
gamma = 1.2
gamma_corrected_array = np.power(img_array, gamma)
gamma_corrected_img_array = gamma_corrected_array * 255.0
gamma_corrected_img = Image.fromarray(
    gamma_corrected_img_array.astype(np.uint8))
gamma_corrected_img.show()
denormalized_img = ((gamma_corrected_img_array **
                    (1 / gamma)) * 255).astype(np.uint8)
Image.fromarray(denormalized_img).show()

# img2 = Image.fromarray(data, 'RGB')
# imgplot = plt.imshow(img2)
# plt.show
# cau4

array_before = np.array(img)
array_after = denormalized_img
plt.hist(array_before.flatten(), bins=256,
         range=(0, 255), alpha=0.5, label="Before")
plt.hist(array_after.flatten(), bins=256,
         range=(0, 255), alpha=0.5, label="After")
plt.title("Histogram of Brightness Values")
plt.xlabel("Độ sáng")
plt.ylabel("Số điểm ảnh")
plt.legend(loc="upper right")
plt.show()
