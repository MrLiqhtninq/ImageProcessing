import os
import time
import cv2 
import pafy
import numpy as np
from rich.console import Console
from rich.theme import Theme 
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)

def Week4():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        prev_frame_time = 0
        new_frame_time = 0
        #url = "https://www.youtube.com/watch?v=1oYLqu_Yp6I"
        
        #video = pafy.new(url)
        #best = video.getbest(preftype="mp4")

        net = cv2.dnn.readNet("/Users/mrliqhtninq/Desktop/ImageProcessing/dnn_model/yolov4-tiny.cfg","/Users/mrliqhtninq/Desktop/ImageProcessing/dnn_model/yolov4-tiny.weights")
        model = cv2.dnn_DetectionModel(net)
        model.setInputParams(size=(320,320),scale=1/125)
        classes = []
        with open("/Users/mrliqhtninq/Desktop/ImageProcessing/dnn_model/classes.txt","r") as file_object:
            for class_name in file_object.readlines():
                class_name = class_name.strip()
                classes.append(class_name)
        
	
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        while True:
            ret, frame = cap.read()
            (class_ids, scores, bboxes)= model.detect(frame)
            for class_id, score, bbox in zip(class_ids, scores, bboxes):
                x, y, w, h = bbox
                cv2.putText(frame,str(classes[class_id]),(x,y-5),cv2.FONT_HERSHEY_PLAIN,1,(200,0,50),2)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,50),3)
            new_frame_time = time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            prev_frame_time = new_frame_time
            cv2.putText(frame, str(int(fps)), (7, 70), cv2.FONT_HERSHEY_PLAIN, 3, (100, 255, 0), 3, cv2.LINE_AA)

            cv2.imshow("Basic",frame)
            cv2.waitKey(1)
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")