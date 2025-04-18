import cv2
import os
from datetime import datetime

def add_subtitle(frame, text, position, font, font_scale, font_color, thickness):
    cv2.putText(frame, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

def save_frame(frame, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"frame_{timestamp}.png"
    filepath = os.path.join(directory, filename)
    
    cv2.imwrite(filepath, frame)
    print(f"Frame saved as {filepath}")

def main():
    # Load video
    video_path = r"Projects\test_video.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    subtitle_text = input("Enter the subtitle text: ")
    subtitle_position = (int(input("Enter x position of the subtitle: ")), int(input("Enter y position of the subtitle: ")))
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = float(input("Enter the font scale (e.g., 1 for normal size): "))
    font_color = (int(input("Enter B value for font color (0-255): ")), 
                  int(input("Enter G value for font color (0-255): ")),
                  int(input("Enter R value for font color (0-255): ")))
    font_thickness = int(input("Enter the font thickness: "))

    save_directory = input("Enter the directory to save frames: ")
    print("Press 's' to save the current frame. Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("end of video reached.")
            break

        add_subtitle(frame, subtitle_text, subtitle_position, font, font_scale, font_color, font_thickness)

        cv2.imshow("Video with Subtitles", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            save_frame(frame, save_directory)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
