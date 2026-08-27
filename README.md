# Stereo Vision
## Project Idea

This project uses OpenCV to take two images (Left & Right) of the same scenencaptured by two side-by-side cameras and produce:

1. A Disparity Map (the difference in position of the same point between the two images).
2. The real-world Depth of any pixel in the image (i.e., the actual distance between it and the camera, in millimeters).
3. A Point Cloud (a 3D set of points) that reconstructs the scene in 3D space, optionally colored using the original image.

The general idea behind Stereo Vision is: the closer an object is to the camera, the bigger the difference in its position between the left and right images (the disparity), and vice versa. From this relationship, we can calculate the real-world distance using a simple equation :

Depth = (Focal Length × Baseline) / Disparity

-------
## Requirements

- opencv-python
- numpy
- MeshLab or CloudCompare (to view the Point Cloud file)
  
-------

## Dataset

The dataset used contains two folders (im0 and img1), each with:
- im0.png → Left image
- im1.png → Right image
- Calibration parameters for each folder (fx, fy, cx, cy, baseline, doffs)

-----
## Output

The project produces:

- A Disparity Map showing the depth-related differences between the two images.
- A Depth Map representing the estimated distance from the camera.
- A PLY Point Cloud containing the reconstructed 3D points.
- An optional RGB Point Cloud, where points are colored using the original image.

The generated ".ply" file can be opened using MeshLab or CloudCompare to visualize the reconstructed scene in 3D.

------
## Problem I Faced and How I Solved It

When I tried to push the Point Cloud file to GitHub, I couldn't upload it because the file size was too large.
To solve this problem, I modified the code and used downsampling:

                 points_for_ply = points_3d_rgb[::5]

This means we only keep one point out of every 5 (Downsampling), which significantly reduced the file size without affecting the overall shape of the reconstructed scene in the Point Cloud.This keeps one point out of every five points, which significantly reduced the PLY file size while preserving the overall shape of the reconstructed 3D scene.

After applying this change, I was able to upload the Point Cloud successfully to GitHub.

Later, I realized that I could have simply compressed the PLY file into a ZIP archive. This would have preserved all the points and provided a more detailed Point Cloud, while also making the file easier to upload.

Unfortunately, by that time I had already modified the code and uploaded the downsampled version. Using ZIP compression from the beginning would have saved me some time.

Lesson learned: Next time, I will try to think of simpler alternatives before changing the original data or code.

-------
## Point Cloud Video

I recorded a short video showing the reconstructed 3D scene:

Video link: [https://drive.google.com/file/d/1fnzuZxABTvJ5vHgvR5wCgtt-i_Xxrstg/view?usp=sharing]


