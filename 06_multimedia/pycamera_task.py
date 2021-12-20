# pycamera_task.py

import picamera
import time

path = '/home/pi/src3/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()

    while (1):
        cmd = int(input('photo: 1, video: 2, exit: 9 > '))
        now_str = time.strftime('%Y%m%d_%H%M%S')

        if cmd == 1:
            print('taking photo...')

            name = 'photo_'+ now_str +'.jpg'
            camera.capture('%s/pictures/%s' % (path, name))
        elif cmd == 2:
            print('taking video...')

            name = 'video_'+ now_str +'.h264'
            camera.start_recording('%s/videos/%s' % (path, name))

            input('press any key to stop recording...')
            camera.stop_recording()
        elif cmd == 9:
            break
        else:
            print('Invalid command')

finally:
    camera.stop_preview()
