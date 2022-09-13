import cv2
import os 
from progress_bar import progress_bar

bar = u"\u2588"

def frame_extractor(input_path, output_path=None):
    if not os.path.exists(input_path):
        print("path doesn't exist's")
        exit(0)

    if output_path is None:
        output_path = "..\\tmp\\" + os.path.splitext(os.path.basename(input_path))[0]

    if not os.path.exists(output_path):
        os.mkdir(output_path)
    vid = cv2.VideoCapture(input_path)
    current_frame = 0
    total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Extracting Frames...")
    progress_bar(0, total_frames)
    while True:
        success, frame = vid.read()
        if not success:
            break
        cv2.imwrite(f"{output_path}\\frame_{current_frame}.jpg", frame)
        current_frame += 1
        progress_bar(current_frame, total_frames)

if __name__ == "__main__":
    frame_extractor("..\\resources\\samples\\sample_frame_extractor.mp4")
    
