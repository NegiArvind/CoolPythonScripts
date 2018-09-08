import cv2

video="DemoVideo.mp4"
imageFolder="/home/arvind/Documents/FrameCaptured/"
captureObject=cv2.VideoCapture(video)

# cap.get(propId) method where propId is a number from 0 to 18.
#  Each number denotes a property of the video (if it is applicable to that video).

print(captureObject.get(3)) # get(3) return me the frame width
print(captureObject.get(4)) # get(4) return me the frame height
# captureObject.set(3,600)  # setting width
# captureObject.set(4,400) # setting height
count=1
while captureObject.isOpened():

    # cap.read() returns a bool (True/False) and frame. If frame is read correctly, it will be True
    readCorrectly,frame=captureObject.read()

    if not readCorrectly:
        break

    # capturing frame after 1 sec(not sure)
    if count%10==0:
        frameNumber=captureObject.get(1)
        filename=imageFolder+video.rstrip(".mp4")+" image "+str(count)[:-1]+".png" # setting filename
        cv2.imwrite(filename,frame)
        print("Saved "+str(count)[:-1]+" "+str(frameNumber)+"\n") # [:-1] is used to remove last digit of string
    count+=1

captureObject.release()
print("done")