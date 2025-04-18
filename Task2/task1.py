import cv2
import numpy as np

def detect_shapes(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
    
    cv2.imshow("Shape Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_shapes("shapes.png")
