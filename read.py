import cv2
import numpy as np

# 读取图片
image = cv2.imread('STAR.png')

# 转换为HSV色彩空间，hsv比bgr更符合人的色彩感知
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 定义绿色的HSV范围，array便于后面使用inRange函数
lower_green = np.array([35, 50, 50])  # 绿色的HSV下限,[色调（0~179），饱和度（0~255），亮度（0~255）]
upper_green = np.array([85, 255, 255])  # 绿色的HSV上限

# 创建绿色掩膜，inRange（图像，下层，上层）
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

# 找到绿色区域的轮廓，findContours（图像，mode，method）
contours = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 计算绿色区域的重心，moments（矩），可用于描述物体位置，面积，形状，方向，重心
M = cv2.moments(green_mask)

# 计算重心坐标 (cx, cy)，m00代表面积，m10和m01分别是x，y方向所有像素坐标加权和
if M["m00"]!=0:
    cx=int(M["m10"]/M["m00"])
    cy=int(M["m01"]/M["m00"])
else:
    cx=0
    cy=0    
# 打印重心坐标
print(f"绿色像素的重心坐标为: ({cx}, {cy})")

# 可视化绿色区域（对任务没什么屌用，但学都学了）
cv2.imshow('Green Mask', green_mask)#掩膜返回的图像是二值图，符合条件为白色，不符合为白色
#利用cv2.bitwise_and(image,image,mask=mask)来将掩膜部分恢复成原图颜色
cv2.imshow('Original Image with Green ', cv2.bitwise_and(image,image, mask=green_mask))

cv2.waitKey(0)
cv2.destroyAllWindows()
