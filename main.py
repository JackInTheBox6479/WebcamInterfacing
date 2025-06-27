import cv2
import numpy as np

# Create the webcam object
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FPS, 60)

# Sets the coordinate of which pixels to monitor
xmin = 20
xmax = 120
ymin = 20
ymax = 120

# Empty set to hold the pixel color values
color_values = []

while True:
    ret, frame = webcam.read()
    flipped_frame = cv2.flip(frame, 1)

    if ret:
        # Draws read rectangle and displays frame
        cv2.rectangle(flipped_frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 3)
        cv2.imshow("Webcam", flipped_frame)

        #Adds the color value for each pixel in the range
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                pixel = flipped_frame[y, x]
                color_values.append(pixel)

        #Deteremines the average color values
        blue = sum([int(c[0]) for c in color_values]) // len(color_values)
        green = sum([int(c[1]) for c in color_values]) // len(color_values)
        red = sum([int(c[2]) for c in color_values]) // len(color_values)

        # Creates a new frame showing the average color in the designated range
        average_color_frame = np.full((480, 640, 3), (blue, green, red), dtype=np.uint8)
        cv2.imshow(f"Average Color", average_color_frame)
        color_values.clear()

        # Close the stream when Q is pressed
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()
