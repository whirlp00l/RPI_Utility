import serial
import string
from math import *

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)

grad2rad = 3.141592/180.0

roll = 0
pitch = 0
yaw = 0
while 1:
	line = ser.readline();
	line = line.replace("!RAW:","")
	if (line.find("#YPR=")!=-1):
		line = line[5:]
		#print line
		words = line.split(",")
		if len(words)>2:
			try:
				yew = float(words[0])
				pitch = float(words[1])
				row = float(words[2])
			except:
				print "Invalid line"
		#print "Yaw:: {0} \t Pitch:: {1} \t Roll:: {2}".format(yaw,pitch,roll)
		yaw = -yaw * grad2rad
		pitch = -pitch * grad2rad
		roll = roll * grad2rad
#Here we use http://planning.cs.uiuc.edu/node102.html
		m00 = cos(roll)*cos(yaw) + sin(pitch)*sin(roll)*sin(yaw)
		m01 = cos(roll)*sin(pitch)*sin(yaw) - cos(yaw)*sin(roll)
		m02 = cos(pitch)*sin(yaw)
		m10 = cos(pitch)*sin(roll)
		m11 = cos(pitch)*cos(roll)
		m12 = -sin(pitch)
		m20 = cos(yaw)*sin(pitch)*sin(roll) - cos(roll)*sin(yaw)
		m21 = sin(roll)*sin(yaw) + cos(roll)*cos(yaw)*sin(pitch)
		m22 = cos(pitch)*cos(yaw)

		#print "{0} {1} {2} {3} {4} {5} {6} {7} {8} 1 1 1 1 1 1 ".format(m00, m10, m20, m01, m11, m21, m02, m12, m22)
		print "{0} {1} {2} {3} {4} {5} {6} {7} {8} 1 1 1 1 1 1 ".format(m00, m01, m02, m10, m11, m12, m20, m21, m22)


#[ cos(roll)*cos(yaw) + sin(pitch)*sin(roll)*sin(yaw), cos(roll)*sin(pitch)*sin(yaw) - cos(yaw)*sin(roll), cos(pitch)*sin(yaw)]
#[                               cos(pitch)*sin(roll),                               cos(pitch)*cos(roll),         -sin(pitch)]
#[ cos(yaw)*sin(pitch)*sin(roll) - cos(roll)*sin(yaw), sin(roll)*sin(yaw) + cos(roll)*cos(yaw)*sin(pitch), cos(pitch)*cos(yaw)]
 