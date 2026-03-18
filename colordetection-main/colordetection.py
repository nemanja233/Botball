import cv2
#load the webcam
cap=cv2.VideoCapture(0)
# Increasing the size of frame 
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1288)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)


# Putting frame in while to continuously read frames
while True:
    _,frame=cap.read()

    # Convert to hsv
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Setting pixel at center
    height,width,_=frame.shape 
    cx=int(width/2)
    cy=int(height/2)

    # Picking pixel value
    pixel_center=hsv_frame[cy,cx]
    hue_value=pixel_center[0]

    #Setting color ranges - hsvcolorpicker.py file can be used as reference
    color="Undefined"
    if hue_value<5:
     color="RED"
    elif hue_value<22:
     color="ORANGE"
    elif hue_value<33:
     color="YELLOW"
    elif hue_value<78:
     color="GREEN"
    elif hue_value<131:
     color="BLUE"
    elif hue_value<170:
     color="VIOLET" 
    else:
        color="RED"

    # Extract the BGR color values of the center pixel.
    pixel_center_bgr=frame[cy,cx]
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    
    # Define text to display
    text = f"Color: {color}"

    # Define the box parameters
    box_color = (255, 255, 255)  # White box color
    box_thickness = -1  # Negative value fills the rectangle completely

    # Get text size
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 1)[0]
    text_x = 10
    text_y = 70

    # Draw the white box
    cv2.rectangle(frame, (text_x - 5, text_y - text_size[1] - 5),
                  (text_x + text_size[0] + 5, text_y + 5), box_color, box_thickness)

    # Put text on the frame
    cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (b, g, r), 2)
    # Draw a circle at the center of the frame.
    cv2.circle(frame,(cx,cy),5,(25,25,25),3)


    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)  
    if key==27: # Ascii value of a esccape key on keyboard
        break 

# Release the video capture and destroy all OpenCV windows.
cap.release()
cv2.destroyAllWindows()
