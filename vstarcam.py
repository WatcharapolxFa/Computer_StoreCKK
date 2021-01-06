import cv2


cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
tracker = cv2.TrackerMedianFlow_create()

onTracking = False
while True :
    _, frame = cap.read()
    if not onTracking :
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3,5)
        for(x, y, w, h) in faces :
            cv2.rectangle(frame, (x,y), (x + w , y + h), (0, 0, 255), 2)
            if  tracker.init(frame,(x, y, w, h)) :
                onTracking = True
           
    else :
        ok, bbox = tracker.update(frame)
        if ok :
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0]+bbox[2]),int(bbox[1]+bbox[3]))
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
        else:
            onTracking =False
            tracker = cv2.TrackerMedianFlow_create()

    cv2.imshow('frame',frame)
    cv2.waiKey(1)