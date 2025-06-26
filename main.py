import cv2
import numpy as np

# Create the webcam object
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FPS, 60)

# Sets the coordinate of which pixel to monitor
pixel_x = 500
pixel_y = 30

# Calculate the average BGR values of the pixel
blue_values = [0]
avg_blue = sum(blue_values) / len(blue_values)
green_values = [0]
avg_green = sum(green_values) / len(green_values)
red_values = [0]
avg_red = sum(red_values) / len(red_values)

while True:
    ret, frame = webcam.read()
    flipped_frame = cv2.flip(frame, 1)

    if ret:
        cv2.imshow("Webcam", flipped_frame)
        pixel_color = flipped_frame[pixel_y, pixel_x]

        # Creates a new frame showing the current color at the pixel
        single_color_frame = np.full((480, 640, 3), pixel_color, dtype=np.uint8)
        cv2.imshow(f"Color of Pixel {pixel_x}, {pixel_y}", single_color_frame)

        # Close the stream when Q is pressed
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

print(f'Blue: {pixel_color[0]} Green: {pixel_color[1]} Red: {pixel_color[2]}')

webcam.release()
cv2.destroyAllWindows()
