import cv2
import numpy as np

image1=cv2.imread("Images/SMVITM_CS/1.jpg")
image1=cv2.resize(image1,(400,600))

image2=cv2.imread("Images/SMVITM_CS/2.jpg")
image2=cv2.resize(image2,(400,600))

image3=cv2.imread("Images/SMVITM_CS/3.jpg")
image3=cv2.resize(image3,(400,600))

image4=cv2.imread("Images/SMVITM_CS/7.jpg")
image4=cv2.resize(image4,(400,600))

image5=cv2.imread("Images/SMVITM_CS/8.jpg")
image5=cv2.resize(image5,(400,600))

image6=cv2.imread("Images/SMVITM_CS/9.jpg")
image6=cv2.resize(image6,(400,600))

hstack1=np.hstack([image1,image2,image3])
hstack2=np.hstack([image4,image5,image6])

cv2.imwrite("Images/SMVITM_CS/Row1.jpg", hstack1)
cv2.imwrite("Images/SMVITM_CS/Row2.jpg", hstack2)
v_stack = np.vstack([hstack1,hstack2])
cv2.imshow("vhcollage",v_stack)
