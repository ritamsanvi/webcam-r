import cv2

def take_snapshot():
    #initailizing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        #read the frames while camera is on
        ret,frame=videoCaptureObject.read()
        print(ret)
        #cv2.imwrite()method is used to save an image to any storing device.
        cv2.imwrite("newpic1.jpg",frame)
        result=False
    
    #release the camera
    videoCaptureObject.release()
    #closes all the window that might be open while this process runs
    cv2.destroyAllWindows()

take_snapshot()