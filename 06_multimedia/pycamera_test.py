import picamera
import time

path = '/home/pi/src3/06_multimedia/'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)  # 크기(해상도)
    camera.start_preview()
    time.sleep(3)

    #camera.capture('%s/pictures/photo.jpg' % path)
    
    camera.start_recording('%svideos/video.h264' % path)
    input('Press Anything to Stop Recording')
    camera.stop_recording()
finally:
    camera.stop_preview()