import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import mysql.connector
    
path = 'Downloads'
myList = os.listdir(path)

images = []
classNames = []
for cls in myList:
    curImage=cv2.imread(f'{path}/{cls}')
    images.append(curImage)
    classNames.append(os.path.splitext(cls)[0])
    #cv2.imshow(os.path.splitext(cls)[0],curImage)
    #print(classNames)

def findEncoding(images):
    encodingList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encodingimg = face_recognition.face_encodings(img)[0]
        encodingList.append(encodingimg)
    return encodingList
encodeListKnown = findEncoding(images)
print('Encoding Complete')
cap = cv2.VideoCapture(0)


while True:
        reader = SimpleMFRC522()

        try:
                id, text = reader.read()
                print(id)
                print(text)
                if (id in (153102784051,346928459818,153162684073,908810524168,663174284848)):
                        print("helo")
                        success, img = cap.read()
                        img = cv2.resize(img,(0,0),None,0.25,0.25)
                        imgS = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                        facesCurFrame = face_recognition.face_locations(imgS)
                        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
                
                        for encodeFace,faceLoc in zip(encodesCurFrame, facesCurFrame):
                            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                            faceDist = face_recognition.face_distance(encodeListKnown,encodeFace)
                            matchIndex = np.argmin(faceDist)
                            if matches[matchIndex]:
                                name = classNames[matchIndex].upper()
                                print(name)
                            if id == int(name):
                                mydb = mysql.connector.connect(
                                        host="82.180.143.118",
                                        user="u394450735_SIH",
                                        password="Game@123456789",  
                                        database="u394450735_Student_data"
                                )  
                                mycursor = mydb.cursor()
                                s = str(id)
                                id = int(s[3:])
                                if (id==928459818):
                                    sql = "UPDATE data SET aug29 ='1' WHERE id = '928459818'"
                                elif (id==102784051):
                                    sql = "UPDATE data SET aug29 = '1' WHERE id = '102784051'"
                                elif (id==162684073):
                                    sql = "UPDATE data SET aug29 = '1' WHERE id = '162684073'"
                                elif (id==810524168):
                                    sql = "UPDATE data SET aug29 = '1' WHERE id = '810524168'"
                                elif (id==174284848):
                                    sql = "UPDATE data SET aug29 = '1' WHERE id = '174284848'"
                                mycursor.execute(sql)
                    
                                mydb.commit()

                                print(mycursor.rowcount, "record(s) update")
                                
                        
        finally:
                GPIO.cleanup()
