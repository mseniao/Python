import cv2
import numpy as np

vtr = cv2.imread("sheat.png")
while(True):
   # ret,frame = vtr.read()
    if vtr is None:
        print("映像を取得できません")
        break
    ref = cv2.resize(vtr, dsize=None, fx=0.5, fy=0.5) #全体が映るようにリサイズ
    grf = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY) #判別をしやすくするためにグレースケール化
    can = cv2.Canny(grf,40.0,200.0)  #canny処理
    lines = cv2.HoughLinesP(can, rho=1, theta=np.pi/360, threshold=30, minLineLength=25, maxLineGap=5) #ライン検出

    for line in lines:
        x1, y1, x2, y2 = line[0]

        # 赤線を引く
        cv2.line(ref, (x1,y1), (x2,y2), (0,0,255), 3)
        #cv2.imwrite('linewriter.jpg', ref)
   
    cv2.imshow('f',can)
    cv2.imshow('g',ref)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

