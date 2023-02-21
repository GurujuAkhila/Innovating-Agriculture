import picamera
print("about to capture")
with picamera.PiCamera() as camera:
camera.resolution = (1280, 720)
camera.capture("picture captured”) 
