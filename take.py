import picamera
import time
import Tkinter as tk
i=0
camera=0
def capture(event):
  global i
  global camera
  camera.capture(('image'+ str(i) + '.jpg'),use_video_port=True)
  i+=1


camera = picamera.PiCamera()
camera.resolution = (1920,1080)
camera.start_preview()
time.sleep(2)

root = tk.Tk()
entry = tk.Entry(root)
entry.bind('<F5>',capture)
entry.pack()
root.mainloop()