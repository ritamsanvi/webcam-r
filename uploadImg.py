import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)

    #initailizing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while (result):
        #read the frames while camera is on
        ret,frame=videoCaptureObject.read()
    
        #cv2.imwrite()method is used to save an image to any storing device.
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    
    print("image captured")
    
    #release the camera
    videoCaptureObject.release()
    #closes all the window that might be open while this process runs
    cv2.destroyAllWindows()

    return img_name

def uploadFiles(img_name):
    access_token ="drCJdiE4ZdkAAAAAAAAAAWypFA7T87_fhxqLTlWjCnSZBlU56ECJBoywmawfU3eL"
    file=img_name

    file_from = file
    file_to = "/UploadingMachine/" + (img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)


    print("file has been moved")

def main(): 
    while(True):
        if ((time.time() - start_time) >= 1):
            name = take_snapshot()
            uploadFiles(name)

main()