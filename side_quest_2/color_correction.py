import cv2
import numpy as np


img = cv2.imread("crabs.png")              # load image

# White Balance Correction
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
L, A, B = cv2.split(lab)

A = A.astype(np.float32)
B = B.astype(np.float32)

# Correct the underwater color cast
A = A - (np.mean(A) - 128)
B = B - (np.mean(B) - 128)

A = np.clip(A, 0, 255).astype(np.uint8)
B = np.clip(B, 0, 255).astype(np.uint8)

white_balanced = cv2.cvtColor(cv2.merge([L, A, B]),cv2.COLOR_LAB2BGR)

# 3. Red Channel Restoration
b, g, r = cv2.split(white_balanced)

# Enhance the red channel, which is strongly
# attenuated in underwater images
red_enhanced = cv2.equalizeHist(r)
red_strength = .4
r_new = cv2.addWeighted(r,1 - red_strength,red_enhanced,red_strength,0)
red_corrected = cv2.merge([b, g, r_new])

#CLAHE Contrast Enhancement
lab = cv2.cvtColor(red_corrected, cv2.COLOR_BGR2LAB)
L, A, B = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.5,tileGridSize=(16, 16))
L_enhanced = clahe.apply(L)
contrast_enhanced = cv2.cvtColor(cv2.merge([L_enhanced, A, B]),cv2.COLOR_LAB2BGR)

# Sharpening
blur = cv2.GaussianBlur(contrast_enhanced,(3, 3),0)
final_output = cv2.addWeighted(contrast_enhanced,1.8,blur,-0.8,0)

# Save Output
cv2.imwrite("corrected_crabs_colored.png",final_output)
print("Color correction completed successfully.")
print("Output saved as corrected_crabs_colored.png")