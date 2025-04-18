import cv2
import numpy as np


def display_image(image, window_name="Image"):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(image):
    path = input("Enter the file path to save the image: ")
    cv2.imwrite(path, image)
    print(f"Image saved at {path}")

def resize_image(image):
    choice = input("Enter 'd' to specify dimensions or 's' to specify a scale factor: ").lower()
    
    if choice == 'd':
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        resized_image = cv2.resize(image, (width, height))
    elif choice == 's':
        scale_factor = float(input("Enter the scale factor (e.g., 0.5 for half size): "))
        resized_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
    else:
        print("Invalid choice.")
        return image
    
    display_image(resized_image, "Resized Image")
    return resized_image

def rotate_image(image):
    angle = int(input("Enter the angle of rotation (positive for clockwise, negative for anticlockwise): "))
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    
    display_image(rotated_image, "Rotated Image")
    return rotated_image

def flip_image(image):
    print("1: Horizontal Flip\n2: Vertical Flip\n3: Both")
    choice = int(input("Choose the flip option: "))
    
    if choice == 1:
        flipped_image = cv2.flip(image, 1)
    elif choice == 2:
        flipped_image = cv2.flip(image, 0)
    elif choice == 3:
        flipped_image = cv2.flip(image, -1)
    else:
        print("Invalid choice.")
        return image
    
    display_image(flipped_image, "Flipped Image")
    return flipped_image

def convert_to_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(grayscale_image, "Grayscale Image")
    return grayscale_image

def convert_to_hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    display_image(hsv_image, "HSV Image")
    return hsv_image

def blur_image(image):
    blur_strength = int(input("Enter the kernel size for blurring (odd number, e.g., 3, 5, 7): "))
    blurred_image = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)
    display_image(blurred_image, "Blurred Image")

def split_channels(image):
    B, G, R = cv2.split(image)
    
    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return B, G, R

def detect_color(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    print("Specify the target color range:")
    lower_hue = int(input("Enter lower hue (0-179): "))
    lower_saturation = int(input("Enter lower saturation (0-255): "))
    lower_value = int(input("Enter lower value (0-255): "))
    upper_hue = int(input("Enter upper hue (0-179): "))
    upper_saturation = int(input("Enter upper saturation (0-255): "))
    upper_value = int(input("Enter upper value (0-255): "))

    lower_color = np.array([lower_hue, lower_saturation, lower_value])
    upper_color = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    result_image = cv2.bitwise_and(image, image, mask=mask)

    display_image(result_image, "Detected Color Image")
    

def main():
    path="space.jpeg"
    image = cv2.imread(path)

    while True:
        print("\n--- Image Processing Menu ---")
        print("1: Resize Image")
        print("2: Rotate Image")
        print("3: Flip Image")
        print("4: Convert to Grayscale")
        print("5: Convert to HSV")
        print("6: Blur Image")
        print("7: Split RGB Channels")
        print("8: Detect Color")
        print("9: Save Image")
        print("10: Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1 and image is not None:
            image = resize_image(image)
        elif choice == 2 and image is not None:
            image = rotate_image(image)
        elif choice == 3 and image is not None:
            image = flip_image(image)
        elif choice == 4 and image is not None:
            convert_to_grayscale(image)
        elif choice == 5 and image is not None:
            convert_to_hsv(image)
        elif choice == 6 and image is not None:
            blur_image(image)
        elif choice == 7 and image is not None:
            split_channels(image)
        elif choice == 8 and image is not None:
            detect_color(image)
        elif choice == 9 and image is not None:
            save_image(image)
        elif choice == 10:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice or no image loaded. Please try again.")

if __name__ == "__main__":
    main()
