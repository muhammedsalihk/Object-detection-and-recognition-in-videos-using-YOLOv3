# Object-detection-and-recognition-in-videos-using-Yolo-v3

## Introduction
Detecting and recognising objects in video streams can be done in multiple ways. A few years ago, a multi step approach where the objects are first detected and localised using a neural network and subsequently classified using another CNN would have been the go to approach. But with the advent of the YOLO (You only look once) model, thanks to Joseph Redmon, this has been turned into an end to end deep learning problem where the entire process could be done using a single pass through a neural network.

In this project, we are building a video analytics tool that can do frame by frame object detection and recognition and then output a video with the detected objects (i.e. the bounding boxes) and its classes. We are using the latest version of the YOLO model, v3.

## Methodology
Here, we use a prebuilt implementation of Yolo v3 using a package named ImageAI. The front end of the app is built using Streamlit. 

The video to be analysed can be selected from and on clicking the appropriate button, the output video is generated and saved.

The weights for the pretrained Yolov3 network can be downloaded [here](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5).

## Implementation
The webapp has been built using streamlit and can be run using the command 
```
streamlit run st.py
```
![App1](https://github.com/muhammedsalihk/Object-detection-and-recognition-in-videos-using-Yolo-v3/blob/master/Images/App%201.png)

On clicking ‘Detect objects and see output’, the output video with the analysis results is played automatically in the default media player. A copy of it is also saved as a file named ‘output-1.avi’
