import cv2
import urllib.request

cap = cv2.VideoCapture('http://192.168.1.126:14026/videostream.cgi?user=admin&pwd=888888')
urlup ='http://192.168.1.126:14026/decoder_control.cgi?loginuse=admin&loginpas=888888&command=1&onestep=0&16099090134280.6695055990897747&_=1609909013428'
urldown ='http://192.168.1.126:14026/decoder_control.cgi?loginuse=admin&loginpas=888888&command=3&onestep=0&16099090304380.6935537129919782&_=1609909030438'
urlleft ='http://192.168.1.126:14026/decoder_control.cgi?loginuse=admin&loginpas=888888&command=5&onestep=0&16099090589110.1875092007795247&_=1609909058912'
urlright ='http://192.168.1.126:14026/decoder_control.cgi?loginuse=admin&loginpas=888888&command=7&onestep=0&16099090815000.7435879814536643&_=1609909081500'
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