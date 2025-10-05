import cv2
import numpy as np

# 打开视频文件，利用cv2.VideoCapture
cap = cv2.VideoCapture('nature.mp4') 

# 获取视频帧尺寸、FPS,其中cap.get(3)获得宽度，cap.get(4)获得高度，cv2.CAP_PROP_FPS获得帧率
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)

# 输出视频文件
out = cv2.VideoWriter('green_only_output.mp4',#文件名
                      cv2.VideoWriter_fourcc(*'mp4v'),#编码格式('mp4v')
                      fps, (frame_width, frame_height))#输出的宽度高度，帧率

#利用以下的while语句，逐帧读取视频
while True:#无限循环的写法
    ret, frame = cap.read()#ret为布尔值，frame为图像数据
    #如果没有成功读取到帧，就break
    if not ret:
        break

    # 转换为HSV色彩空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义绿色范围
    lower_green = np.array([35, 50, 50])     # 可以根据需要微调
    upper_green = np.array([85, 255, 255])

    # 创建掩膜，只保留绿色区域
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # 将掩膜应用到原图像上
    green_only = cv2.bitwise_and(frame, frame, mask=green_mask)

    # 显示结果帧
    cv2.imshow('Green Only Video', green_only)
    
    # out.write将保存后的结果帧写入新视频
    out.write(green_only)

    # 按 ' '(空格) 键退出
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
