import cv2 as cv
import numpy as np


def region_selection(image):
    
    mask = np.zeros_like(image)   
    ignore_mask_color = 255
    # creating a polygon to focus only on the road in the picture
    # we have created this polygon in accordance to how the camera was placed
    rows, cols = image.shape[:2]
    bottom_left  = [cols * 0.1, rows * 0.93]
    top_left     = [cols * 0.4, rows * 0.78]
    bottom_right = [cols * 0.9, rows * 0.95]
    top_right    = [cols * 0.6, rows * 0.78]
    vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
    # filling the polygon with white color and generating the final mask
    cv.fillPoly(mask, vertices, ignore_mask_color)
    # performing Bitwise AND on the input image and mask to get only the edges on the road
    masked_image = cv.bitwise_and(image, mask)
    return masked_image


def average_slope_intercept(lines):
    """
    Find the slope and intercept of the left and right lanes of each image.
    Parameters:
        lines: output from Hough Transform
    """
    left_lines    = [] #(slope, intercept)
    left_weights  = [] #(length,)
    right_lines   = [] #(slope, intercept)
    right_weights = [] #(length,)
     
    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            # calculating slope of a line
            slope = (y2 - y1) / (x2 - x1)
            # calculating intercept of a line
            intercept = y1 - (slope * x1)
            # calculating length of a line
            length = np.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
            # slope of left lane is negative and for right lane slope is positive
            if slope < 0:
                left_lines.append((slope, intercept))
                left_weights.append((length))
            else:
                right_lines.append((slope, intercept))
                right_weights.append((length))
    # 
    left_lane  = np.dot(left_weights,  left_lines) / np.sum(left_weights)  if len(left_weights) > 0 else None
    right_lane = np.dot(right_weights, right_lines) / np.sum(right_weights) if len(right_weights) > 0 else None
    return left_lane, right_lane

def pixel_points(y1, y2, line):
    """
    Converts the slope and intercept of each line into pixel points.
        Parameters:
            y1: y-value of the line's starting point.
            y2: y-value of the line's end point.
            line: The slope and intercept of the line.
    """
    if line is None:
        return None
    slope, intercept = line
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    y1 = int(y1)
    y2 = int(y2)
    return ((x1, y1), (x2, y2))
def draw_line(img,edge):
    rho = 1             
    # Angle resolution of the accumulator in radians.
    theta = np.pi/180   
    # Only lines that are greater than threshold will be returned.
    threshold = 20      
    # Line segments shorter than that are rejected.
    minLineLength = 20  
    # Maximum allowed gap between points on the same line to link them
    maxLineGap = 500    
    # function returns an array containing dimensions of straight lines 
    # appearing in the input image

    # Probabilistic Hough Line Transform
    lines=cv.HoughLinesP(edge, rho = rho, theta = theta, threshold = threshold,minLineLength = minLineLength, maxLineGap = maxLineGap)

    left_lane, right_lane = average_slope_intercept(lines)
    y1 = img.shape[0]
    
    y2 = y1 * 0.756
    left_line  = pixel_points(y1, y2, left_lane)
    right_line = pixel_points(y1, y2, right_lane)
    color=[0,255,0] 
    thickness=6
    # line_image = np.zeros_like(img)
    for line in (left_line,right_line):
        if line is not None:
            cv.line(img, *line,  color, thickness)
    # return cv.addWeighted( line_image, 1.0,img, 1.0, 0.0)
    # return cv.add(line_image,img)
    
    

video=cv.VideoCapture('test_video.mp4')
frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 

size = (frame_width, frame_height) 
video_final=cv.VideoWriter('results/videoplayback.mp4',cv.VideoWriter_fourcc(*'mp4v',),60, size)

while(True):
    flag,img=video.read()

    if flag==False: break
    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    canny=cv.Canny(img_gray,125,175)
    edge=region_selection(canny)
    final=draw_line(img,edge)
    cv.imshow('image',img)
    # video_final.write(final)
    if cv.waitKey(2) & 0xFF==ord('d'):
        break

# flag,img=video.read()
# img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# canny=cv.Canny(img,125,175)
# cv.imshow('image',region_selection(canny))
# cv.imshow('image',canny)
# cv.waitKey(0)

cv.destroyAllWindows()