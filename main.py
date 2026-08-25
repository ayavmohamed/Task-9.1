import cv2

#im0
# Load images in grayscale
left_image = cv2.imread("dataset/im0/im0.png", cv2.IMREAD_GRAYSCALE)
right_image = cv2.imread("dataset/im0/im1.png", cv2.IMREAD_GRAYSCALE)

# Print image information
print("Left image shape:", left_image.shape)
print("Right image shape:", right_image.shape)


# Create and resize windows
cv2.namedWindow("Left Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Right Image", cv2.WINDOW_NORMAL)

# Display images in GRAYSCALE
cv2.imshow("Left Image", left_image)
cv2.imshow("Right Image", right_image)

cv2.waitKey(0)
cv2.destroyAllWindows()