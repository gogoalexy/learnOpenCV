from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import FPS
import argparse
import cv2

frameHW = (256, 256)

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100, help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1, help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

print("[INFO] sampling frames from PiCam through pure OpenCV...")
stream = cv2.VideoCapture(0)
stream.set(cv2.CAP_PROP_FPS, 30)
stream.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHW[0])
stream.set(cv2.CAP_PROP_FRAME_WIDTH, frameHW[1])
time.sleep(2.0)

fps = FPS().start()
while fps._numFrames < args["num_frames"]:
	(grabbed, frame) = stream.read()

	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

	fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

stream.release()
cv2.destroyAllWindows()
fps.reset()

print("[INFO] sampling frames from PiCam through picamera module and OpenCV...")
camera = PiCamera()
camera.resolution = frameHW
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=frameHW)
stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
time.sleep(2.0)

fps = FPS().start()
while fps._numFrames < args["num_frames"]:
	frame = f.array

	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

	rawCapture.truncate(0)
	fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
stream.close()
rawCapture.close()
camera.close()
