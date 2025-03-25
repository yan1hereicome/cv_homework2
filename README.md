# cv_homework2
# Cartoonify Image using OpenCV

Convert any image into a cartoon-style image using OpenCV and Python!

## 📌 Features
- Converts an image into a cartoon-like effect.
- Uses edge detection and bilateral filtering to enhance colors.
- Simple and lightweight implementation.

## 🛠 Requirements
Ensure you have the following installed:

- Python 3.x
- OpenCV
- NumPy

Install dependencies using:
```bash
pip install opencv-python numpy
```

## 📂 Project Structure
```
|-- cartoonify.py  # Main Python script
|-- input.jpg      # Input image (replace with your own image)
|-- README.md      # Project documentation
```

## 🚀 Usage
1. Place an image named `input.jpg` in the same directory as the script.
2. Run the script:
   ```bash
   python cartoonify.py
   ```
3. The cartoon-styled image will be displayed.

## 📝 Code Explanation
```python
import cv2
import numpy as np

# Load the image
image = cv2.imread("input.jpg")

# Resize for better processing
image = cv2.resize(image, (600, 600))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median blur
gray_blur = cv2.medianBlur(gray, 5)

# Edge detection using adaptive thresholding
edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth colors
color = cv2.bilateralFilter(image, 9, 250, 250)

# Combine edges with color image
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Display result
cv2.imshow("Cartoon Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 🎨 Example Output
| Original Image | Cartoon Image |
|---------------|--------------|
| ![Original](https://via.placeholder.com/200) | ![Cartoon](https://via.placeholder.com/200) |

## 🔥 Contributing
Feel free to improve this project by submitting a pull request!

## 📜 License
This project is licensed under the MIT License.

