import cv2
import numpy as np

def grade_omr(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    answers = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 100 < area < 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            answers += 1

    cv2.putText(image, f"Marked Answers: {answers}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("OMR Grading", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

grade_omr("omr_sheet.jpg")
