import cv2
import numpy as np
import imutils



lowerRED=np.array([0,50,50])
upperRED=np.array([10,255,255])

lowerGREEN=np.array([33,80,40])
upperGREEN=np.array([102,255,255])

lowerWHITE=np.array([0,0,100], dtype=np.uint8)
upperWHITE=np.array([50,180,255], dtype=np.uint8)

cam= cv2.VideoCapture(0)


kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))



while True:

    ret, video=cam.read()
    cv2.imshow("video", video)

    
    c = cv2.waitKey(20)
    #Press F to take a screenshot to analyze
    if c == 102:

        

        ret, img=cam.read()

        #convert BGR to HSV
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


        
        maskRED=cv2.inRange(imgHSV,lowerRED,upperRED)
        maskGREEN=cv2.inRange(imgHSV, lowerGREEN, upperGREEN)
        maskWHITE=cv2.inRange(imgHSV, lowerWHITE, upperWHITE)


        
        #RED
        maskOpenRED=cv2.morphologyEx(maskRED,cv2.MORPH_OPEN,kernelOpen)
        maskCloseRED=cv2.morphologyEx(maskOpenRED,cv2.MORPH_CLOSE,kernelClose)
        #GREEN
        maskOpenGREEN=cv2.morphologyEx(maskGREEN,cv2.MORPH_OPEN,kernelOpen)
        maskCloseGREEN=cv2.morphologyEx(maskOpenGREEN,cv2.MORPH_CLOSE,kernelClose)
        #WHITE
        maskOpenWHITE=cv2.morphologyEx(maskWHITE,cv2.MORPH_OPEN,kernelOpen)
        maskCloseWHITE=cv2.morphologyEx(maskOpenWHITE,cv2.MORPH_CLOSE,kernelClose)

         #contours RED
        conts,h=cv2.findContours(maskCloseRED.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        #draw contours
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            area=w*h
            if area>=50:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
                coord=[x,y,w,h]
                cv2.putText(img,"RED, "+ str(coord[0]+(coord[2]/2))+" "+str(coord[1]+(coord[3]/2)), (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1, cv2.LINE_AA)
                

  


         #contours GREEN
        conts,h=cv2.findContours(maskCloseGREEN.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        #draw contours
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            area=w*h
            if area>=50:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
                coord=[x,y,w,h]
                cv2.putText(img,"GREEN, "+ str(coord[0]+(coord[2]/2))+" "+str(coord[1]+(coord[3]/2)), (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1, cv2.LINE_AA)
                


         #contours WHITE
        conts,h=cv2.findContours(maskCloseWHITE.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        #draw contours
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            area=w*h
            if area>=50:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
                coord=[x,y,w,h]
                cv2.putText(img,"WHITE, "+ str(coord[0]+(coord[2]/2))+" "+str(coord[1]+(coord[3]/2)), (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1, cv2.LINE_AA)
                

      
        cv2.imshow("RED",maskCloseRED)
        cv2.imshow("GREEN",maskCloseGREEN)
        cv2.imshow("WHITE",maskCloseWHITE)
        cv2.imshow("cam",img)



    #ESC
    key = cv2.waitKey(20)
    if key == 27:

        cv2.destroyAllWindows()
        break
