# cv.py将图片旋转90度并保存
import cv2

# flags传入0表示灰度图像, 1表示彩色图像
img=cv2.imread('test.jpeg',flags=1)

# 获取图片尺寸
rows,cols=img.shape[:2]

# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

# 第三个参数是输出图像的尺寸中心
dst=cv2.warpAffine(img,M,(cols,rows))

# 写入文件
cv2.imwrite("test-rotated.jpg", dst, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
print('rotated and saved.')
