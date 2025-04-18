import cv2
import numpy as np

def scan_document(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            break

    cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)
    cv2.imshow("Scanned Document", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

scan_document("document.jpg")
