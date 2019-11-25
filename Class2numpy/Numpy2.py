import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im

img = im.imread('./_Pic/Flower.png')

#plt.subplot(221)
#plt.imshow(img)
# ===========================================
#t = img.copy()
#r = t[::-1]
#plt.subplot(222)
#plt.imshow(r)

# ===========================================
#t = img.copy()
#r = t.transpose(1, 0, 2)
#x = r[:, :: -1]
#plt.subplot(223)
#plt.imshow(x)


# ===========================================

#t = img.copy()
#r = t.transpose(1, 0, 2)
#plt.subplot(224)
#plt.imshow(r)
#plt.show()

# =========================================
#print(type(t))
#print(t.shape)
#print(t[0][0])
t = img.copy()
mask = np.full((200, 200, 4), fill_value=(0.3, 0.2, 0.5, 0.3))
t[x1:x2, y1:y2] = mask
plt.imshow(t)
plt.show()

# 作业4——————在原图的（x1，y1）位置，打上mask
# mask的尺寸为：宽度为w，高度为h

和[x1:(x1+w),y1:(y1+h)] = mask
