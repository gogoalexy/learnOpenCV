from picamera.array import PiRGBArray
from picamera import PiCamera
from timer import FPS
from threaded import PiVideoStream
import argparse
import time
import cv2

frameHW = (128, 128)

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100, help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", help="Whether or not frames should be displayed", action="store_true")
args = vars(ap.parse_args())

print("[INFO] sampling frames from PiCam through pure OpenCV...")
stream = cv2.VideoCapture(0)
stream.set(cv2.CAP_PROP_FPS, 32)
stream.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHW[0])
stream.set(cv2.CAP_PROP_FRAME_WIDTH, frameHW[1])
time.sleep(2.0)

fps = FPS().start()
while not fps.isPassed(args["num_frames"]):
    (grabbed, frame) = stream.read()

    if args["display"]:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    fps.update()

fps.stop()
print("[INFO] elasped time: {:.4f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.3f}".format(fps.fps()))

stream.release()
cv2.destroyAllWindows()
fps.reset()

print("[INFO] sampling frames from PiCam through picamera module and OpenCV...")
camera = PiCamera()
camera.resolution = frameHW
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=frameHW)
stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
time.sleep(2.0)

fps = FPS().start()
while not fps.isPassed(args["num_frames"]):
    frame = next(stream).array

    if args["display"]:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    fps.update()

fps.stop()
print("[INFO] elasped time: {:.4f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.3f}".format(fps.fps()))

cv2.destroyAllWindows()
stream.close()
rawCapture.close()
camera.close()
fps.reset()

print("[INFO] sampling THREADED frames from picamera module...")
vs = PiVideoStream(frameHW).start()
time.sleep(2.0)

fps = FPS().start()
while not fps.isPassed(args["num_frames"]):
    frame = vs.read()
    
    if args["display"]:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
 
    fps.update()

fps.stop()
print("[INFO] elasped time: {:.4f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.3f}".format(fps.fps()))
 
cv2.destroyAllWindows()
vs.stop()