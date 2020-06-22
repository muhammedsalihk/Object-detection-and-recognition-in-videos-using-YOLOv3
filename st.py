import time
import streamlit as st
import io
import tempfile, sqlite3
import os 
import cv2
import subprocess, sys
from imageai.Detection import VideoObjectDetection

def detect_text(file, output_name):

    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("yolo.h5")
    detector.loadModel()

    
    video_path = detector.detectObjectsFromVideo(input_file_path= file,
                                    output_file_path= output_name
                                    , frames_per_second=29, log_progress=True)
    return video_path


def file_selector(folder_path=os.getcwd()):
    filenames = os.listdir(folder_path)
    file_format = []
    for file in filenames:
        if file[-3:] == 'mp4':
            file_format.append(file)
    selected_filename = st.selectbox('Select a video', file_format)
    return os.path.join(folder_path, selected_filename)



def main():

    st.title('Video - Object Recognition')
    st.text('Built by Muhammed Salih')

    home = os.getcwd()
    opener ="open" if sys.platform == "darwin" else "xdg-open"

    filename = file_selector()
    st.write('You selected `%s`' % filename)
    if st.button('View video'):
        subprocess.call([opener, filename])
    
    if st.button('Detect objects and see output'):
        with st.spinner('Processing'):
            output = detect_text(filename, 'output-1')
        st.success('Done! Waiting for the output file to open')
        time.sleep(1)
        subprocess.call([opener, output])


if __name__ == '__main__':
		main()
