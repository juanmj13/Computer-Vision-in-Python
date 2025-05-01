# rtsp_cam_basic

A simple Python-based tool for working with IP cameras via RTSP, supporting live streaming, motion detection, color tracking, and automatic photo capture. This project is ideal for developers or IoT enthusiasts looking to interact with ONVIF-compatible cameras and perform basic computer vision tasks.

## Features

- 🔍 **RTSP Discovery** using ONVIF
- 📺 **Live Camera Streaming**
- 🎯 **Motion Detection** with adjustable sensitivity
- 🎨 **Color Tracking** using HSV color ranges
- 📸 **Photo Capture** triggered by keyboard input
- 🔐 **Environment-based configuration**

## Project Structure

- `main.py` – Entry point of the application. Handles environment setup and function execution.
- `rtsp.py` – Contains all camera-related functions:
  - `discovery()` – Automatically retrieves the RTSP URL of an ONVIF camera.
  - `liveCam()` – Displays live camera feed with support for manual photo capture.
  - `movementDetectionBasic()` – Detects movement based on frame differences and highlights areas in motion.
  - `trackingColor()` – Tracks objects of a specific color in the video feed.
  - `TakePhoto()` – Captures and saves the current frame to a local folder.

## Requirements

- Python 3.7+
- Compatible IP camera (ONVIF and RTSP support)

### Python Packages

Make sure to install the required dependencies:

```bash
pip install opencv-python onvif-zeep numpy python-dotenv
```


## USAGE

1. Clone my Computer Vision in Python Repositorie
```bash
git clone https://github.com/juanmj13/Computer-Vision-in-Python.git
cd rtsp_cam_basic
```

2. Create a .env file in the root directory with your camera credentials:

```bash
CAMERA_IP=192.168.1.10 #Your Cam IP
CAMERA_PORT=80 #Your Cam Port
CAMERA_USER=admin #Your Cam user
CAMERA_PASSWORD=admin123 #Your Cam Pass
```
3. Run the project:
```bash
python main.py
```

4. In the video windows:
- Press q to quit
- Press t to take a photo (saved in photos/ directory).

## NOTES 
- The functions in rtsp.py are designed to be called from main.py.
- If your RTSP URL already includes the username and password, they will not be inserted again.
- Captured images are saved with a timestamp in the filename under a folder named photos.

## License
This project is open-source and free to use under the MIT License.



