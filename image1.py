import cv2
# Load the image in RGB format
image_path = 'image.jpg' # Replace with the path to your image
image = cv2.imread(image_path)
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Display image information
print("Image Information:")
print(f"Image Shape: {image.shape}")
print(f"Image Height: {image.shape[0]} pixels")
print(f"Image Width: {image.shape[1]} pixels")
# Display the grayscale image
cv2.namedWindow('Grayscale Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Grayscale Image', 900, 600)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0) # Wait for a key press to close the image window
cv2.destroyAllWindows()
