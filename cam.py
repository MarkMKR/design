# loop over the frames from the video stream
import datetime

import args as args
import cv2
import imutils
from imutils.video import VideoStream

while True:
	# grab the frame from the threaded video stream and resize it

	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()