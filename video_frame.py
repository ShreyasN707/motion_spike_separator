import cv2
import os

def frame_extractor(video_path,output_folder='frames'):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    cap=cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Cannot open video")
        exit()

    frame_count=0

    while True:
        ret,frame=cap.read()

        if not ret:
            break
        filename=f"frame_{frame_count:06d}.png"
        filepath = os.path.join(output_folder, filename)

        cv2.imwrite(filepath, frame)

        frame_count+=1

    cap.release()
    print(f"Extracted frames : {frame_count}")