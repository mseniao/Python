import cv2
import numpy as np

vtr = cv2.VideoCapture("IMG_5578.MOV")
while(True):
    ret,frame = vtr.read()
    if not vtr.isOpened():
        print("映像を取得できません")
        break
    ref = cv2.resize(frame, dsize=None, fx=0.3, fy=0.3) #全体が映るようにリサイズ
    grf = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY) #判別をしやすくするためにグレースケール化
    neg = cv2.bitwise_not(grf)  #黒線を強調するためにネガポジ反転
    lines = cv2.HoughLinesP(neg, rho=1, theta=np.pi/360, threshold=80, minLineLength=400, maxLineGap=5)
    print(lines)

    cv2.imshow('f',neg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vtr.release()
cv2.destroyAllWindows()

