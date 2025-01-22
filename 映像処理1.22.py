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
    lines = cv2.HoughLinesP(neg, rho=1, theta=np.pi/360, threshold=80, minLineLength=400, maxLineGap=5) #ライン検出

    for line in lines:
        x1, y1, x2, y2 = line[0]

        # 赤線を引く
        red_line_img = cv2.line(ref, (x1,y1), (x2,y2), (0,0,255), 3)
        cv2.imwrite("calendar_mod3.png", red_line_img)

    cv2.imshow('f',red_line_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vtr.release()
cv2.destroyAllWindows()

