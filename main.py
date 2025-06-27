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

# Calculate the average BGR values of the pixel
color_values = []

while True:
    ret, frame = webcam.read()
    flipped_frame = cv2.flip(frame, 1)

    if ret:
        cv2.rectangle(flipped_frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 3)
        cv2.imshow("Webcam", flipped_frame)



        pixels = {}
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                pixel = flipped_frame[y, x]
                color_values.append(pixel)

       # if len(color_values) > 60:
        #    color_values.pop(0)

        blue = sum([int(c[0]) for c in color_values]) // len(color_values)
        green = sum([int(c[1]) for c in color_values]) // len(color_values)
        red = sum([int(c[2]) for c in color_values]) // len(color_values)

        # Creates a new frame showing the current color at the pixel
        #current_color_frame = np.full((480, 640, 3), pixel, dtype=np.uint8)
        #cv2.imshow(f"Current Color of Pixel {pixel_x}, {pixel_y}", current_color_frame)

        # Creates a new frame showing the current color at the pixel
        average_color_frame = np.full((480, 640, 3), (blue, green, red), dtype=np.uint8)
        cv2.imshow(f"Average Color", average_color_frame)
        color_values.clear()

        # Close the stream when Q is pressed
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

#print(f'Blue: {pixel[0]} Green: {pixel[1]} Red: {pixel[2]}')

webcam.release()
cv2.destroyAllWindows()
