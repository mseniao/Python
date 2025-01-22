import cv2
import numpy as np

vtr = cv2.imread("sheat.png")
while(True):
   # ret,frame = vtr.read()
    if vtr is None:
        print("映像を取得できません")
        break
    ref = cv2.resize(vtr, dsize=None, fx=0.3, fy=0.3) #全体が映るようにリサイズ
    grf = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY) #判別をしやすくするためにグレースケール化
    neg = cv2.bitwise_not(grf)  #黒線を強調するためにネガポジ反転
    lines = cv2.HoughLinesP(neg, rho=1, theta=np.pi/360, threshold=100, minLineLength=300, maxLineGap=5) #ライン検出

    #for line in lines:
    #    x1, y1, x2, y2 = line[0]

        # 赤線を引く
    #    cv2.line(ref, (x1,y1), (x2,y2), (0,0,255), 3)
    #    cv2.imwrite('linewriter.jpg', ref)

    cv2.imshow('f',neg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vtr.release()
cv2.destroyAllWindows()

