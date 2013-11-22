import scriptcontext
import Rhino
import System
from Rhino.Geometry import *
from scriptcontext import doc
import rhinoscriptsyntax as rs
import Rhino.RhinoApp as app
from array import *
import os
import sys


frames = 300


#rs.CurrentView("perspective")
#rs.Command ("!_-Render")

#saveRenderview("C:\Users\ebberly")

#rs.Command ("_-SaveRenderWindowAs " + renderfilepath)

cameraLine = rs.GetCurveObject("Pick camera curve", False, False) 
targetLine = rs.GetCurveObject("Pick target curve", False, False) 


if cameraLine:
    cameraList = rs.DivideCurve(cameraLine[0], frames)
    
if targetLine:
    targetList = rs.DivideCurve(targetLine[0], frames)




view = doc.Views.ActiveView.ActiveViewport
point = Point3d(3.4, 5.4, 0.0)
point2 = Point3d(100, 6.4, 6.0)

# fileFolder = rs.BrowseForFolder("D:\Strathairn\Animation")

for x in range(0,frames):
    view.SetCameraLocations(targetList[x], cameraList[x])
    # imgDrop = '"' + fileFolder + "\image" + str(x) + '.png"'
    # rs.Command("-_ViewCaptureToFile " + imgDrop + " _Enter")
    
    rs.CurrentView("perspective")
    rs.Command ("!_-Render")
    rs.Command ("_-SaveRenderWindowAs D:\Strathairn\Animation\img"+str(x)+".png")
    #rs.Command (fileFolder + "\image" + str(x) + '.png"' + "_-Enter")
    
    #print cameraList[x]
    #print targetList[x]
    



    
