import cv2
import os
import numpy as np
cap = cv2.VideoCapture(0)
path = './image/'
z = a = c = v = 0
while True:
    _, frame = cap.read()
    key = cv2.waitKey(1) & 0xFF
    if key == ord('z'):
        z += 1
        cv2.imwrite(path + 'Anniversary_'+str(z) + '.png', frame)
    if key == ord('a'):
        a += 1
        cv2.imwrite(path + 'Three_'+str(a) + '.png', frame)
    if key == ord('c'):
        c += 1
        cv2.imwrite(path + 'month_'+str(c) + '.png', frame)
    if key == ord('v'):
        v += 1
        cv2.imwrite(path + 'fahsai_'+str(v) + '.png', frame)
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
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    cv2.imshow('frame', frame)
