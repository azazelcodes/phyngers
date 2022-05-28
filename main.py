# IMPORTS
import webbrowser as web
from cv2 import cv2
import time
import mediapipe as mp
import os
from datetime import datetime, timedelta
import pyttsx3 as tts
from playsound import playsound
import asyncio

# TIME SET
startTime = time.time()
currentTime = 0

# HAND INIT
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# FRAME INIT
new_frame_time = 0
prev_frame_time = 0

# CAM INIT
cap = cv2.VideoCapture(0)

# BUG NOTIFY

with mp_hands.Hands(
  min_detection_confidence=0.5,
  min_tracking_confidence=0.5,
  max_num_hands=2) as hands :

  while cap.isOpened():

    success,image = cap.read(0)
    if not success :
      print("Skipping empty frame !")
      continue
    
    #image = cv2.flip(image,1)

    results = hands.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

    hand = str(results.multi_handedness)
    
    # GET HAND
    if 'Right' in hand :
      whathand = 'Hand : Right'
    elif 'Left' in hand :
      whathand = 'Hand : Left'
    else :
      whathand = 'Hand : -'
    
    image.flags.writeable = True
    imageHeight, imageWidth, _ = image.shape
     
    # SET GESTURE
    gesture = 'Gesture : -'    
    
    # DRAW HAND CONNECTIONS
    if results.multi_hand_landmarks :
      for handLandmarks in results.multi_hand_landmarks :
        mp_drawing.draw_landmarks(image, handLandmarks, mp_hands.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(16,31,235), thickness=4, circle_radius=3,), # Land Mark
        mp_drawing.DrawingSpec(color=(52,235,155), thickness=2)) # Land Connections
        
        # GET EVERY FINGERS POS (throw error if not found)
        try:
          normalizedLandmark = handLandmarks.landmark[4]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Thumb_Tip_x = pixelCoordinatesLandmark[0]           
          Thumb_Tip_y = pixelCoordinatesLandmark[1]
        except:
          print("No THUMB TIP found")
        
        try:
          normalizedLandmark = handLandmarks.landmark[6]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Index_Pip_x = pixelCoordinatesLandmark[0]           
          Index_Pip_y = pixelCoordinatesLandmark[1]
        except:
          print("No INDEX PIP found")

        try:
          normalizedLandmark = handLandmarks.landmark[10]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Middle_Pip_x = pixelCoordinatesLandmark[0]           
          Middle_Pip_y = pixelCoordinatesLandmark[1]
        except:
          print("No MIDDLE PIP found")

        try:
          normalizedLandmark = handLandmarks.landmark[14]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Ring_Pip_x = pixelCoordinatesLandmark[0]           
          Ring_Pip_y = pixelCoordinatesLandmark[1]
        except:
          print("No RING PIP found")

        try:
          normalizedLandmark = handLandmarks.landmark[18]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Pinky_Pip_x = pixelCoordinatesLandmark[0]           
          Pinky_Pip_y = pixelCoordinatesLandmark[1]
        except:
          print("No PINKY PIP found")
        #--------------------------------------------------
        try:
          normalizedLandmark = handLandmarks.landmark[5]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Index_Mcp_x = pixelCoordinatesLandmark[0]           
          Index_Mcp_y = pixelCoordinatesLandmark[1]
        except:
          print("No INDEX MCP found")

        try:
          normalizedLandmark = handLandmarks.landmark[9]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Middle_Mcp_x = pixelCoordinatesLandmark[0]           
          Middle_Mcp_y = pixelCoordinatesLandmark[1]
        except:
          print("No MIDDLE MCP found")

        try:
          normalizedLandmark = handLandmarks.landmark[13]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Ring_Mcp_x = pixelCoordinatesLandmark[0]           
          Ring_Mcp_y = pixelCoordinatesLandmark[1]
        except:
          print("No RING MCP found")

        try:
          normalizedLandmark = handLandmarks.landmark[17]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Pinky_Mcp_x = pixelCoordinatesLandmark[0]           
          Pinky_Mcp_y = pixelCoordinatesLandmark[1]
        except:
          print("No PINKY MCP found")

        #------------------------------------
        try:
          normalizedLandmark = handLandmarks.landmark[3]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Thumb_Ip_x = pixelCoordinatesLandmark[0]           
          Thumb_Ip_y = pixelCoordinatesLandmark[1]
        except:
          print("No THUMB IP found")

        try:
          normalizedLandmark = handLandmarks.landmark[8]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Index_Tip_x = pixelCoordinatesLandmark[0]           
          Index_Tip_y = pixelCoordinatesLandmark[1]
        except:
          print("No INDEX TIP found")

        try:
          normalizedLandmark = handLandmarks.landmark[12]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Middle_Tip_x = pixelCoordinatesLandmark[0]           
          Middle_Tip_y = pixelCoordinatesLandmark[1]
        except:
          print("No MIDDLE TIP found")

        try:
          normalizedLandmark = handLandmarks.landmark[16]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Ring_Tip_x = pixelCoordinatesLandmark[0]           
          Ring_Tip_y = pixelCoordinatesLandmark[1]
        except:
          print("No RING TIP found")

        try:
          normalizedLandmark = handLandmarks.landmark[20]# Point No.
          pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
          Pinky_Tip_x = pixelCoordinatesLandmark[0]           
          Pinky_Tip_y = pixelCoordinatesLandmark[1]
        except:
          print("No PINKY TIP found")

        thmb_indx_diff = Thumb_Ip_x-Index_Mcp_x


        # FINGER POSITIONS

        if Thumb_Ip_y < Middle_Tip_y and Thumb_Ip_y < Ring_Tip_y and Thumb_Ip_y < Pinky_Tip_y and Thumb_Ip_y < Index_Tip_y :
            if Thumb_Tip_y < Middle_Pip_y and Thumb_Tip_y < Ring_Pip_y and Thumb_Tip_y < Pinky_Pip_y and Thumb_Tip_y < Index_Pip_y :
                gesture = 'Gesture : Fist'
        
        if Index_Pip_y < Middle_Tip_y and Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y and Index_Pip_y < Thumb_Tip_y :
            if Index_Tip_y < Middle_Pip_y and Index_Tip_y < Ring_Pip_y and Index_Tip_y < Pinky_Pip_y and Index_Tip_y < Thumb_Ip_y :
                gesture = 'Gesture : Index'

                
        
        if Middle_Pip_y < Index_Tip_y and Middle_Pip_y < Ring_Tip_y and Middle_Pip_y < Pinky_Tip_y and Middle_Pip_y < Thumb_Tip_y :
            if Middle_Tip_y < Index_Tip_y and Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y and Middle_Tip_y < Thumb_Ip_y :
                gesture = 'Gesture : Middle'
        
        if Ring_Pip_y < Index_Tip_y and Ring_Pip_y < Middle_Tip_y and Ring_Pip_y < Pinky_Tip_y and Ring_Pip_y < Thumb_Tip_y :
            if Ring_Tip_y < Index_Tip_y and Ring_Tip_y < Middle_Pip_y and Ring_Tip_y < Pinky_Pip_y and Ring_Tip_y < Thumb_Ip_y :
                gesture = 'Gesture : Ring'
        
        if Pinky_Pip_y < Index_Tip_y and Pinky_Pip_y < Ring_Tip_y and Pinky_Pip_y < Middle_Tip_y and Pinky_Pip_y < Thumb_Tip_y :
            if Pinky_Tip_y < Index_Tip_y and Pinky_Tip_y < Ring_Pip_y and Pinky_Tip_y < Middle_Pip_y and Pinky_Tip_y < Thumb_Ip_y : 
                gesture = 'Gesture : Pinky'
                
                # EXAMPLE OF SOMETHING THAT RUNS EVERY PYTHON UPDATE (not frame)
                print("TEA - The Eaten Austrich")

        # NUMBERS
        if Index_Pip_y < Middle_Tip_y and Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y and Index_Pip_y < Thumb_Tip_y :
            if Index_Tip_y < Middle_Pip_y and Index_Tip_y < Ring_Pip_y and Index_Tip_y < Pinky_Pip_y and Index_Tip_y < Thumb_Ip_y :
                gesture = 'Gesture : One'  
                
                # GET TIME AND SPLIT INTO BITS


                rawCurrentDate = str(datetime.now())

                splitRawTime = rawCurrentDate.split()[1]
                splitTime = splitRawTime.split(".")[0]
                hourTime = splitTime.split(":")[0]
                minuteTime = splitTime.split(":")[1]
                secondTime = splitTime.split(":")[2]
                
                # DONT REMOVE THE 1. "0" IF THERE ARE 2 (but do when theres a different number on the 2. spot)
                if hourTime[0] == "0" and hourTime[1] != "0":
                  fixHourTime = hourTime[1]
                else:
                  fixHourTime = hourTime
                if minuteTime[0] == "0" and minuteTime[1] != "0":
                  fixMinuteTime = minuteTime[1]
                else:
                  fixMinuteTime = minuteTime
                if secondTime[0] == "0" and secondTime[1] != "0":
                  fixSecondTime = secondTime[1]
                else:
                  fixSecondTime = secondTime

                hourTimeInt = int(fixHourTime)
                minuteTimeInt = int(fixMinuteTime)
                secondTimeInt = int(fixSecondTime)


                splitDate = rawCurrentDate.split()[0]
                year = splitDate.split("-")[0]
                month = splitDate.split("-")[1]
                day = splitDate.split("-")[2]
  
                # LOG TIME EVERY SECOND WHILE INDEX UP
                print(rawCurrentDate + " - RAW TIME")
                print(splitTime + " - SPLIT TIME")
                print(splitDate + " - DATE")

                # SPEAK OVER TTS
                tts.speak("Its " + splitDate)
                tts.speak(fixHourTime + "o'clock, " + fixMinuteTime + "minutes and" + fixSecondTime + "seconds")
                
                # EXAMPLE FOR IF TIME AFTER **:**
                if hourTimeInt >= 12 and minuteTimeInt >= 0:
                  tts.speak("Heres a quick reminder that its over 12 o'clock")
                  # CHANGE THIS TO YOUR SAVE DIRECTORY
                  playsound(r"C:/Users/BinuOS/Documents/root/dev % development/phyngers/cuckoo.mp3")

        if Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y and Index_Pip_y < Thumb_Tip_y :
            if Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y and Middle_Tip_y < Thumb_Ip_y :
                gesture = 'Gesture : Two'  

        if Index_Pip_y < Pinky_Tip_y and Middle_Pip_y < Pinky_Tip_y and Ring_Pip_y < Pinky_Tip_y  :
            if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y :
                if Index_Tip_y < Thumb_Tip_y and Middle_Tip_y < Thumb_Tip_y and Ring_Tip_y < Thumb_Tip_y :
                    gesture = 'Gesture : Three'   
                    
                    # EXAMPLE OF RUNNING SOMETHING EVERY 1.5 SECONDS (opens kity phonk by soviss)
                    web.open("https://www.youtube.com/watch?v=MYzB3AbK00g")
                    time.sleep(1.5)

        if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y  :
            if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y and Index_Tip_y < Thumb_Ip_y :
                gesture = 'Gesture : Four' 

        if thmb_indx_diff < -15 :
            if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y :
                gesture = 'Gesture : Five'
        

        # IF middle (pip) IS HIGHER THAN (<) tip (tip) IS gesture ...
    
    # GET FRAMES AND DISPLAY
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps2text = 'FPS : '+str(int(fps))

    cv2.rectangle(image,(5,5),(320,110),(0,170,240),-1)
    cv2.putText(image,gesture,(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)     
    cv2.putText(image,fps2text,(20,90),cv2.FONT_HERSHEY_COMPLEX,1,(3,3,138),2)
    cv2.imshow('Hand Detection',image)     
    
    # BREAK ON ESC
    if cv2.waitKey(5) & 0xFF == 27 :
      break

cap.release()
