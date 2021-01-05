import cv2
import urllib.request

cap = cv2.VideoCapture('http://192.168.1.126:44212/videostream.cgi?user=admin&pwd=888888')
urlup =''
urldown =''
urlleft =''
urlright =''
while True :
    _, frame = cap.read()
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1) &0xFF
    if key == ord('w') :  #UP
        urllib.request.urlopen(urlup)
    if key == ord('a') :  #DOWN
        urllib.request.urlopen(urldown)
    if key == ord('s') :  #LEFT
        urllib.request.urlopen(urlleft)
    if key == ord('d') :  #RIGHT
        urllib.request.urlopen(urlright)