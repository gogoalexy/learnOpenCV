from threading import Thread
import cv2

class VideoStream:
	def __init__(self, src=0, usePiCamera=False, resolution=(640, 480), framerate=32):
		if usePiCamera:
			from PiStream import PiVideoStream
			self.stream = PiVideoStream(resolution=resolution, framerate=framerate)

		else:
			self.stream = WebcamVideoStream(src=src)

	def start(self):
		return self.stream.start()

	def update(self):
		self.stream.update()

	def read(self):
		return self.stream.read()

	def stop(self):
		self.stream.stop()


class WebcamVideoStream:
	def __init__(self, src=0):
		self.stream = cv2.VideoCapture(src)
		(self.grabbed, self.frame) = self.stream.read()
		self.stopped = False

	def start(self):
		Thread(target=self.update, args=(), daemon=True).start()
		return self

	def update(self):
		while True:
			if self.stopped:
				return

			(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		return self.frame

	def stop(self):
		self.stopped = True

