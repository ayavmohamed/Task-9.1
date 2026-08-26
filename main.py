import cv2

#im0
# Load images in grayscale
left_image = cv2.imread("dataset/im0/im0.png", cv2.IMREAD_GRAYSCALE)
right_image = cv2.imread("dataset/im0/im1.png", cv2.IMREAD_GRAYSCALE)

# Print image information
print("Left image shape:", left_image.shape)
print("Right image shape:", right_image.shape)

# StereoBM parameters
num_disparities = 272                # Multiples of 16
block_size = 15                      # Odd number

# Create StereoBM matcher
stereo = cv2.StereoBM_create(
    numDisparities=num_disparities,
    blockSize=block_size
)

# Compute disparity map
disparity = stereo.compute(left_image, right_image)
print("Disparity map shape:", disparity.shape)

# Normalize disparity for visualization
disparity_normalized = cv2.normalize(disparity,None,0,255,cv2.NORM_MINMAX,cv2.CV_8U)

# Display disparity map
cv2.namedWindow("Disparity Map", cv2.WINDOW_NORMAL)
cv2.imshow("Disparity Map", disparity_normalized)

# Save disparity map
cv2.imwrite("disparity_im0.png", disparity_normalized)

# Create windows
cv2.namedWindow("Left Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Right Image", cv2.WINDOW_NORMAL)


# Display images in GRAYSCALE
cv2.imshow("Left Image", left_image)
cv2.imshow("Right Image", right_image)

cv2.waitKey(0)
cv2.destroyAllWindows()