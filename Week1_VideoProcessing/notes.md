
# Week 1 – Video Processing

## Overview
This task focused on learning basic video processing workflows using FFmpeg. The workflow involved extracting image frames from a video, reconstructing the frames back into a video, and adding background music to the final output.

---

## Tasks Completed

- Downloaded and processed a sample video
- Extracted image frames using FFmpeg
- Reconstructed video from extracted frames
- Added audio track to generated video
- Learned basic video preprocessing techniques for computer vision workflows

---

## Tools Used

- FFmpeg
- macOS Terminal
- Pixabay Music

---

## Commands Used

### Extract Frames

```bash
ffmpeg -i input.mp4 frames/frame_%04d.jpg
```

### Reconstruct Video

```bash
ffmpeg -framerate 30 -i frames/frame_%04d.jpg reconstructed.mp4
```

### Add Audio

```bash
ffmpeg -i reconstructed.mp4 -i music.mp3 -shortest final_output.mp4
```

---

## Folder Structure

```text
Week1_VideoProcessing/
│
├── frames/
│   ├── frame_0001.jpg
│   ├── frame_0050.jpg
│   └── frame_0100.jpg
│
├── input.mp4
├── music.mp3
├── final_output.mp4
└── README.md
```

---

## Output

Successfully created a processed output video with extracted frames and background music using FFmpeg.
