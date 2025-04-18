import cv2
import numpy as np
import math

def detect_angles(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"{int(angle)} deg", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Angle Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_angles("Obtuse-Angle.png")
