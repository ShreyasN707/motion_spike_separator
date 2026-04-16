import os
import cv2

def write_video(outfolder, clip_frames, motion_active, result, img1, clip_count, fps, frame_size):

    if not os.path.exists(outfolder):
        os.mkdir(outfolder)

    # If motion detected → keep adding frames
    if result == "motion":
        motion_active = True
        clip_frames.append(img1)

    else:
        # If motion ended → save clip
        if motion_active and len(clip_frames) > 10:
            output_path = os.path.join(outfolder, f"clip_{clip_count}.mp4")

            out = cv2.VideoWriter(
                output_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                frame_size
            )

            for f in clip_frames:
                out.write(f)

            out.release()
            print(f"Saved clip_{clip_count}.mp4")

            clip_count += 1

        # reset
        motion_active = False
        clip_frames = []

    # return updated state
    return clip_frames, motion_active, clip_count