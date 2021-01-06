import cv2
import urllib.request

cap = cv2.VideoCapture('http://192.168.1.126:27261/videostream.cgi?user=admin&pwd=888888')
urlup ='http://192.168.1.126:27261/decoder_control.cgi?loginuse=admin&loginpas=888888&command=0&onestep=1&16099455500550.7579112705690318&_=1609945550056'
urldown ='http://192.168.1.126:27261/decoder_control.cgi?loginuse=admin&loginpas=888888&command=4&onestep=1&16099455500550.7579112705690318&_=1609945550056'
urlleft ='http://192.168.1.126:27261/decoder_control.cgi?loginuse=admin&loginpas=888888&command=2&onestep=1&16099455500550.7579112705690318&_=1609945550056'
urlright ='http://192.168.1.126:27261/decoder_control.cgi?loginuse=admin&loginpas=888888&command=6&onestep=1&16099455500550.7579112705690318&_=1609945550056'
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