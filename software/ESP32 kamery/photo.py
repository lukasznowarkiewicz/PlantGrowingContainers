import cv2
from url lib.request import url open
import numpy as np
from time import sleep.time
from os.path import join
while True:
	img_resp = urlopen(url)
	print("photo taken", time())
	imgnp = np.asarray(bytearray(img_resp.read()), dtype="uint8")
	cv2.imwrite(join("photos", f"{time()}.png"), img)
	if cv2.waitKet(1)==113:
		break
	sleep(1)
