import cv2
import numpy as np

# Define a function to be called when a trackbar is moved (does nothing in this case).
def nothing(x):
    pass

# Create a window to display the GUI.
cv2.namedWindow("frame")

# Create trackbars for H, S, and V components with initial values.
cv2.createTrackbar("H", "frame", 0, 179, nothing)
cv2.createTrackbar("S", "frame", 255, 255, nothing)
cv2.createTrackbar("V", "frame", 255, 255, nothing)

# Create an empty HSV image to be updated based on trackbar values.
img_hsv = np.zeros((250, 500, 3), np.uint8)

# Start an infinite loop for real-time interaction.
while True:
    # Get the current values of the H, S, and V trackbars.
    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    # Update the entire HSV image with the chosen H, S, and V values.
    img_hsv[:] = (h, s, v)

    # Convert the HSV image to BGR (color) format.
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    # Display the BGR image in the GUI window.
    cv2.imshow("frame", img_bgr)

    # Wait for a key press for 1 millisecond and check if the user pressed the 'Esc' key (27) to exit the loop.
    key = cv2.waitKey(1)
    if key == 27:
        break

# Close all OpenCV windows and exit the program.
cv2.destroyAllWindows()
