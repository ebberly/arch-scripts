import rhinoscriptsyntax as rs
import time
import Rhino
import datetime

#foldernameDate = str(datetime.datetime.now().date())
#foldernameTime = str(datetime.datetime.now().time())
#foldername = foldernameDate[2:4]+foldernameDate[5:7]+foldernameDate[8:10]
for i in range(1, 2):
    print i
    rs.RestoreNamedView (str(i), view=None, restore_bitmap=False)
    outpath = "F:\\_GSAPP\\05 Fall 2013\\01 Studio\\01 Rhino\\02 Renderings\\131115\\Batch\\img"+str(i)+".png"
    Rhino.RhinoApp.RunScript("Render", True)
    
    print (outpath)
    Rhino.RhinoApp.RunScript("_-SaveRenderWindowAs   \n\"" + outpath + "\"\n" , False)
    
    
    
    
