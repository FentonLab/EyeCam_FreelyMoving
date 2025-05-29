# EyeCam_FreelyMoving
Eye movement and location tracking for mice in freely moving arena

Includes:

building instructions for eye camera
code to run eye camera
Eye video pre-processing
DeepLabCut model for tracking pupil 
Jupyter notebook for plotting horizontal and vertical eye movements
bonsai code for locomotion camera

## How to build Eye Camera
Components:
- Camera: https://www.adafruit.com/product/1937
- Raspberry pi 4 board: https://www.adafruit.com/product/4295
- Extension cable 2 m: https://www.adafruit.com/product/2144?gQT=1
- 3D printed parts for holder, mouse dome
- 2 brass screws
- IR LED, cut-tape: https://www.digikey.com/en/products/detail/VSMY3890X01-GS08/751-VSMY3890X01-GS08CT-ND/16684747?utm_source=netcomponents&utm_medium=aggregator&utm_campaign=buynow 

The eye camera runs on a Raspberry Pi 4 board. Connect the extension cable to the _CAMERA IN_ port on the Raspberry Pi board, and the SpyCam to the extension cable. 
Build the camera holder as follows:

![eyecam](https://github.com/user-attachments/assets/4ebeb071-77f1-46f8-8c04-64c380a73682)

## Pupil-tracking

## Locomotion camera
![locomotion_camera](https://github.com/user-attachments/assets/47f818b3-0822-471d-a1c3-0718c76c6db8)
