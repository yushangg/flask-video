from cv2 import *


class VideoCamera(object):
    def __init__(self):
		#used to get the image from the camera
        #self.video = cv2.videoCapture(0)
        self.video1 = cv2.VideoCapture('test1.mp4')
        self.video2 = cv2.VideoCapture('test2.mp4')
        self.video3 = cv2.VideoCapture('test3.mp4')

    def __del__(self):
        self.video1.release()
        self.video2.release()
        self.video3.release()

    def get_frame(self):
        image1 = self.video1.read()[1]
		#encode the image to jpeg
        jpeg = cv2.imencode('.jpg', image1)[1]
        return jpeg.tobytes()

    def get_frame2(self):
        image2 = self.video2.read()[1]
        jpeg2 = cv2.imencode('.jpg', image2)[1]
        return jpeg2.tobytes()

    def get_frame3(self):
        image3 = self.video3.read()[1]
        jpeg3 = cv2.imencode('.jpg', image3)[1]
        return jpeg3.tobytes()