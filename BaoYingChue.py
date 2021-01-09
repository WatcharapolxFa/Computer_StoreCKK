import cv2

cap = cv2.VideoCapture(0)
path = './python_cam/image/'

h = s = p = 0 
while True :
    _, frame =cap.read()
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('h') : h += 1 ; cv2.imwrite(path + 'hammer_'+str(h) + '.png',frame)
    if key == ord('s') : s += 1 ; cv2.imwrite(path + 'scissors_'+str(s) + '.png',frame)
    if key == ord('p') : p += 1 ; cv2.imwrite(path + 'paper_'+str(p) + '.png',frame)

    cv2.imshow('frame',frame)