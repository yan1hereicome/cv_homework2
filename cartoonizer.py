import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Resize the image for better processing (optional)
image = cv2.resize(image, (600, 600))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a median blur to smooth the image
gray_blur = cv2.medianBlur(gray, 5)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                              cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth colors
color = cv2.bilateralFilter(image, 9, 250, 250)

# Combine edges with the color image using bitwise AND
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Show the result
cv2.imshow("Cartoon Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
