import os
import cv2
from video_frame import frame_extractor
from diff_detection import diff_calculator
from video_writer import write_video

video_path='test1.mp4'
frames_folder='frames'
outfolder='output'
motion_active = False
clip_frames = []
clip_count = 0
fps = 30 


frame_extractor(video_path,frames_folder)

frame_files=sorted(os.listdir(frames_folder))

for i in range(len(frame_files)-1):
    frame1_path=os.path.join(frames_folder,frame_files[i])
    frame2_path=os.path.join(frames_folder,frame_files[i+1])

    img1=cv2.imread(frame1_path)
    img2=cv2.imread(frame2_path)

    frame_size=(img1.shape[1],img1.shape[0])

    print(f'Comparing {frame_files[i]} → {frame_files[i+1]}')

    result=diff_calculator(img1,img2)

    clip_frames, motion_active, clip_count = write_video(
        "clips",
        clip_frames,
        motion_active,
        result,
        img1,
        clip_count,
        fps,
        frame_size
    )

print(f'done compiling frames {len(frame_files)}')