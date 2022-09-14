import cv2
import os 
from progress_bar import progress_bar

bar = u"\u2588"

def frame_extractor(input_path, output_path=None):
    if not os.path.exists(input_path):
        print(f"{input_path}: path doesn't exist's")
        return

    if output_path is None:
        output_path = "..\\tmp\\" + os.path.splitext(os.path.basename(input_path))[0]

    if not os.path.exists(output_path):
        os.mkdir(output_path)
    vid = cv2.VideoCapture(input_path)
    current_frame = 0
    total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print(input_path)
    print("Extracting Frames...")
    progress_bar(0, total_frames)
    while True:
        success, frame = vid.read()
        if not success:
            break
        cv2.imwrite(f"{output_path}\\frame_{current_frame}.jpg", frame)
        current_frame += 1
        progress_bar(current_frame, total_frames)
    print(f"Total Frames Extracted: {total_frames}")

def bulk_frame_extractor(input_path, output_path=None):
    if output_path is None:
        output_path = "..\\tmp\\frame_extractor_output"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for path in input_path:
        filename = os.path.basename(path)
        frame_extractor(path, f"{output_path}\\{filename}")


def frame_extractor_from_directory(input_path, output_path=None):    
    if os.path.exists(input_path) and os.path.isdir(input_path):
        files = [file for (root, dir, file) in os.walk(input_path)][0]
        bulk_frame_extractor([f"{input_path}\\{x}" for x in files], output_path)
    else: 
        print(f"{input_path}: path doesn't exist's or isn't a directory")

     

if __name__ == "__main__":
    frame_extractor_from_directory("..\\resources\\samples")
    
