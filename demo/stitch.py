"""Final stitch: title -> recording -> end card."""
import subprocess, os

FFMPEG = r"C:\Users\MyBook Hype AMD\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"
SEG = r"D:\botconfessions\demo"
SRC = r"C:\Users\MyBook Hype AMD\Videos\OBS\2026-07-26 08-11-23.mp4"
OUT = r"D:\botconfessions\BOTConfessions_Demo.mp4"
FONT = "'C\\:/Windows/Fonts/arial.ttf'"

def run(*args):
    cmd = [FFMPEG, "-y"] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-500:])
        raise SystemExit(r.returncode)

# Resize recording to 1920x1080 with dark bg padding
print("Resizing recording...")
run("-i", SRC,
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,"
           "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x14110e",
    "-c:v", "libx264", "-crf", "23", "-preset", "fast",
    "-c:a", "aac", "-b:a", "128k",
    os.path.join(SEG, "recording_resized.mp4"))

# Make filelist for concat
filelist = os.path.join(SEG, "filelist_final.txt")
with open(filelist, "w") as f:
    for name in ["title.mp4", "recording_resized.mp4", "end.mp4"]:
        full = os.path.join(SEG, name)
        f.write(f"file '{full}'\n")

# Concat
print("Concatenating...")
run("-f", "concat", "-safe", "0", "-i", filelist, "-c", "copy", OUT,
    "-movflags", "+faststart")

print(f"DONE: {OUT}")
size_mb = os.path.getsize(OUT) / 1024 / 1024
print(f"{size_mb:.1f} MB")
