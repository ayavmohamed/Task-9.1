# Side Quest 2: Underwater Color Correction

## Overview
This repository branch (side_quest_2) contains the solution for the underwater color correction quest. The goal is to enhance an underwater image of crabs, restore natural colors, and make fine structural details clearly visible.

---

## The Problem with Underwater Images
#### 1. Selective Light Absorption
Water acts as a natural color filter. Red wavelengths (620-750 nm) are absorbed within the first 3-5 meters, orange and yellow follow suit at 5-15 meters, leaving only blue-green light to dominate deeper waters. This is why everything looks eerily blue-green below the surface.

#### 2. Light Scattering
Suspended particles like plankton, sediment, and organic matter scatter light in all directions, creating a hazy, low-contrast appearance similar to fog on land. This phenomenon reduces visibility and blurs fine details.

#### 3. Color Cast and White Balance Issues
The absence of a natural white-light reference underwater makes white balance difficult for cameras, often producing images with severe color casts that don’t accurately represent the scene.

---
### The Solution

Our implementation tackles these challenges through a sophisticated six-stage processing pipeline.

1. Balance Correction (LAB color space)
2. Red Channel Restoration
3. Limited Adaptive Histogram Equalization (CLAHE)
4. Dehazing via Dark Channel Prior
5. Adaptive Unsharp Masking
6. Gamma Correction

----
### A summary of every statge

#### 1. Balance Correction (LAB Color Space):
A technique used to fix unnatural color casts (like heavy blue, green, or yellow tints). By separating lightness from color channels in LAB space, it balances the color distribution to make photos look natural.

#### 2. Red Channel Restoration:
A targeted channel-enhancement method. In environments where red light is easily lost or absorbed (like underwater or low-light scenes), boosting and blending the red channel restores warm hues and natural skin/body tones.

#### 3. Contrast Limited Adaptive Histogram Equalization (CLAHE):
An advanced contrast technique that works on small local regions of an image rather than the whole image at once. It boosts hidden details in dark or low-contrast areas without blowing out bright regions or over-amplifying noise.

#### 4. Dehazing via Dark Channel Prior:
A popular algorithm for removing fog, smoke, or underwater haze. It estimates light scattering in the atmosphere/water and removes it to reveal the clear scene behind it.

#### 5. Adaptive Unsharp Masking:
A classic sharpening technique that detects object boundaries and lines by comparing the original image with a blurred version. It increases edge contrast to make fine textures, lines, and details look crisp and sharp.

#### 6. Gamma Correction:

A non-linear adjustment used to control overall image brightness and display response. It brightens dark shadows or tones down harsh highlights to achieve a balanced, eye-pleasing exposure.

---
## Applied Techniques & Methodology

Since our input image is straightforward, we skipped the full heavy pipeline and implemented a lean 4-step image processing pipeline that directly solves our main issues (Color Cast, Loss of Red, Low Contrast, and Blurry Edges):

#### 1. White Balance Correction (LAB Color Space)
* Converts the image from standard BGR to the LAB color space (where L is Lightness/Luminance, A is Green-Red balance, and B is Blue-Yellow balance). It shifts the A and B channels to center around 128.
* This balances the overall color distribution and removes the heavy green-blue color cast without ruining the natural underwater background colors.

#### 2. Red Channel Restoration
* Extracts the red channel (which is severely faded underwater), applies histogram equalization to expand its range, and blends .4 of this enhanced red back into the image using cv2.addWeighted().
* Since red light degrades fastest underwater, restoring this specific channel brings back the natural warm hues and realistic body tones of the crabs.

#### 3. Contrast Enhancement (CLAHE)
* Applies Contrast Limited Adaptive Histogram Equalization (CLAHE) with clipLimit=2.0 and tileGridSize=(8,8) exclusively to the Luminance (L) channel in LAB space.
* Traditional histogram equalization blows out bright areas. CLAHE operates on small local grid sections, boosting local contrast to make the crabs stand out clearly against the tile floor while preventing over-exposure.

#### 4. Image Sharpening (Unsharp Masking)
* Blurs the enhanced image with a small 3*3 Gaussian Blur and subtracts it from the original image to extract fine edge details.
* This sharpens micro-details—such as the crab legs, shells, and background tile lines—making the subject crisp and defined.

---

### References 

This website helped me alot [https://opencv.org/underwater-image-enhancement-using-opencv/#h-2-the-solution-a-multi-stage-enhancement-pipeline]

