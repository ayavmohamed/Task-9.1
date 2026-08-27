import numpy as np
import cv2 as cv

#im0
# Load images in grayscale
left_image = cv.imread("dataset/im0/im0.png", cv.IMREAD_GRAYSCALE)
right_image = cv.imread("dataset/im0/im1.png", cv.IMREAD_GRAYSCALE)

# Print image information
print("Left image shape:", left_image.shape)
print("Right image shape:", right_image.shape)

# Create StereoBM matcher
stereo = cv.StereoBM_create(numDisparities=272,blockSize=15)

# Compute disparity map
disparity = stereo.compute(left_image, right_image)
print("Disparity map shape:", disparity.shape)

# Calibration parameters from calib.txt
fx = 3979.911
fy = 3979.911
cx = 1244.772
cy = 1019.507
baseline = 193.001
doffs = 124.343

# Convert disparity to real values
disparity_real = disparity.astype(float) / 16.0
valid = disparity_real > 0                  # Get valid disparity pixels
y_coords, x_coords = np.where(valid)        # Pixel coordinates
d = disparity_real[valid]                   # Get valid disparity values

Z = (fx * baseline) / (d + doffs)           # Calculate depth
X = (x_coords - cx) * Z / fx                # Calculate 3D coordinates
Y = (y_coords - cy) * Z / fy

points_3d = np.column_stack((X, Y, Z))       # Store 3D points as N x 3 array

print("3D points shape:", points_3d.shape)

# Save point cloud as PLY
def save_ply(filename, points):
    with open(filename, "w") as file:
        file.write("ply\n")
        file.write("format ascii 1.0\n")
        file.write(f"element vertex {len(points)}\n")
        file.write("property float x\n")
        file.write("property float y\n")
        file.write("property float z\n")
        file.write("end_header\n")

        for point in points:
            file.write(f"{point[0]} {point[1]} {point[2]}\n")

save_ply("point_cloud_im0.ply", points_3d)

print("Point cloud saved as point_cloud_im0.ply")

# Calculate depth from disparity
def calculate_depth(disparity_value):
    depth = (fx * baseline) / (disparity_value + doffs)
    return depth

# Select a pixel
x = 1500
y = 1000

disparity_value = disparity[y, x] / 16.0

depth = calculate_depth(disparity_value)

print("Pixel:", (x, y))
print("Disparity:", disparity_value)
print("Depth:", depth, "mm")

# Normalize disparity for visualization
disparity_normalized = cv.normalize(disparity,None,0,255,cv.NORM_MINMAX,cv.CV_8U)

# Display disparity map
cv.namedWindow("Disparity Map", cv.WINDOW_NORMAL)
cv.imshow("Disparity Map", disparity_normalized)

# Save disparity map
cv.imwrite("disparity_im0.png", disparity_normalized)

# Create windows
cv.namedWindow("Left Image", cv.WINDOW_NORMAL)
cv.namedWindow("Right Image", cv.WINDOW_NORMAL)

# Display images in GRAYSCALE
cv.imshow("Left Image", left_image)
cv.imshow("Right Image", right_image)

cv.waitKey(0)
cv.destroyAllWindows()