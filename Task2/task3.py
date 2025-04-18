import cv2
import numpy as np

def remove_background():
    cap = cv2.VideoCapture(0)
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        fg_mask = bg_subtractor.apply(frame)
        cv2.imshow("Background Removal", fg_mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

remove_background()
