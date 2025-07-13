# -*- coding: utf-8 -*-
# imgKit.py

import cv2
from PyQt5.QtGui import QPixmap

class FRImage:
    # Initialize haarcascade for face detection
    alg = "haarcascade_frontalface_default.xml"
    hc = cv2.CascadeClassifier(alg)
    InstanceCount = 0
    Instances = []
    
    def __init__(self):
        # Generate a unique ID for each instance
        self.InstanceID = FRImage.InstanceCount
        FRImage.InstanceCount += 1
        FRImage.Instances.append(self)
        #print(str(FRImage.InstanceCount)+" - "+str(self.InstanceID)+" - ", type(FRImage.Instances[FRImage.InstanceCount-1]))
        
    def Open(self, filePath):
        # Keep file origin just in case
        self.FilePath = filePath
        # Read the image defined by 'filePath' parameter
        self.cv2Img = cv2.imread(str(self.FilePath), 0)
        # Create a grayscale copy
        self.cv2ImgGray = cv2.cvtColor(self.cv2Img, cv2.COLOR_RGB2BGR)
        # Create a QPicmap copy to display in PyQt5 objects
        self.Pixmap = QPixmap(self.FilePath)

    def FindFaces(self, id):
        # Use haar_cascade algorithm to find faces in the image
        # Store found faces in an Array
        self.cv2Faces = self.hc.detectMultiScale(
            self.cv2ImgGray, scaleFactor=1.05, minNeighbors=2, minSize=(100, 100)
        )
                
        self.Faces  = []
        i = 0
        for x, y, w, h in self.cv2Faces:
            # crop the image to select only the face
            cropped_image = self.cv2Img[y : y + h, x : x + w]
            # loading the target image path into target_file_name variable
            target_file_name = self.FilePath +'_Face' + str(i) + '.jpg'
            cv2.imwrite(
                target_file_name,
                cropped_image,
            )
            self.Faces.append(FRFace())
            #print(FRFace.InstanceCount, " - i=", i)
            self.Faces[i].Open(target_file_name)
            i = i + 1;
            
            
class FRFace:
    InstanceCount = 0

    def __init__(self):
        # Generate a unique ID for each instance
        self.InstanceID = FRFace.InstanceCount
        FRFace.InstanceCount += 1
        
    def Open (self, filePath):
        self.FilePath = filePath
        #self.Pixmap = QPixmap.load(filePath, 0)
    
   
