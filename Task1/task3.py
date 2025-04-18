import cv2
import numpy as np

canvas_left = np.full((512, 512, 3),255, dtype=np.uint8)
canvas_right = np.full((512, 512, 3),255, dtype=np.uint8) 

center = (256, 256)
num_circles = 10
color = (0, 0, 255) 
for i in range(1, num_circles + 1):
    radius = i * 20
    cv2.circle(canvas_left, center, radius, color, 2)

num_lines = 20
for i in range(num_lines):
    angle = i * (360 // num_lines)
    x = int(256 + 256 * np.cos(np.radians(angle)))
    y = int(256 + 256 * np.sin(np.radians(angle)))
    cv2.line(canvas_right, center, (x, y), color, 2)


cv2.imshow("Circles",canvas_left)
cv2.imshow("Right",canvas_right)

cv2.waitKey(0)
cv2.destroyAllWindows()