import cv2
import os
import numpy as np
cap = cv2.VideoCapture(0)
path = './image/'
h = s = p = e = 0
while True:
    _, frame = cap.read()
    key = cv2.waitKey(1) & 0xFF
    if key == ord('z'):
        h += 1
        cv2.imwrite(path + 'Anniversary_'+str(h) + '.png', frame)
    if key == ord('x'):
        s += 1
        cv2.imwrite(path + 'three_'+str(s) + '.png', frame)
    if key == ord('c'):
        p += 1
        cv2.imwrite(path + 'month_'+str(p) + '.png', frame)
    if key == ord('v'):
        e += 1
        cv2.imwrite(path + 'fahsai_'+str(e) + '.png', frame)
    y = []
    D = []
    for fname in os.listdir(path):
        if '.png' in fname:
            x = cv2.imread(path + fname)
            y.append(fname.split('_')[0])
            D.append(np.sum((x-frame)**2))
    if len(D) > 0:
        ans = y[D.index(min(D))]
        if ans != 'else':
            cv2.putText(frame, ans, (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
    cv2.imshow('frame', frame)
