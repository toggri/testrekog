import cv2


webcam = cv2.VideoCapture(0)
success, image = webcam.read()

import boto3

rekog = boto3.client('rekognition')

h,w = image.shape[:2]

regImg = cv2.resize(image, (int(0.2 * w), int(0.2*h))
_, newjpeg = cv2.imencode('.jpg', regImg)
imgbytes = newjpeg.tobytes()

resp = rekog.detect_labels(Image = {'Bytes':imgbytes})


from flask import Flask, render_template, Response

@app.route('/video_feed')
def video_feed():
   return Respone(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')



