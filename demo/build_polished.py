"""
Final polished demo: title + recording + end card
with crossfade transitions + BGM + improved overlays.
"""
import subprocess, os

FFMPEG = r"C:\Users\MyBook Hype AMD\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"
SEG = r"D:\botconfessions\demo"
SRC = r"C:\Users\MyBook Hype AMD\Videos\OBS\2026-07-26 08-11-23.mp4"
BGM = os.path.join(SEG, "bgm.mp3")
OUT = r"D:\botconfessions\BOTConfessions_Demo_Final.mp4"
FONT = "'C\\:/Windows/Fonts/arial.ttf'"
BG = "0x14110e"

def run(*args):
    cmd = [FFMPEG, "-y"] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("STDERR:", r.stderr[-600:])
        raise SystemExit(r.returncode)
    return r

# =============================
# 1. Title card with fade-in (4s)
# =============================
run(
    "-f", "lavfi", "-i", f"color={BG}:s=1920x1080:d=1",
    "-f", "lavfi", "-i", f"color={BG}:s=1920x1080:d=3",
    "-filter_complex",
    f"[0]drawtext=text='BOTConfessions':fontfile={FONT}:fontsize=72:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-80:enable='between(t,0,1)',"
    f"drawtext=text='Anonymous On-Chain Confession Board':fontfile={FONT}:fontsize=28:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-10:enable='between(t,0,1)',"
    f"drawtext=text='GMT Build Week Hackathon':fontfile={FONT}:fontsize=24:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+50:enable='between(t,0,1)'[fadein];"
    f"[fadein]fade=t=in:d=0.8[f0];"
    f"[1]drawtext=text='BOTConfessions':fontfile={FONT}:fontsize=72:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-80,"
    f"drawtext=text='Anonymous On-Chain Confession Board':fontfile={FONT}:fontsize=28:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-10,"
    f"drawtext=text='GMT Build Week Hackathon':fontfile={FONT}:fontsize=24:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+50[f1]",
    "-map", "[f0]", "-map", "[f1]",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    "-shortest",
    os.path.join(SEG, "title_anim.mp4")
)

# =============================
# 2. Resize recording
# =============================
run(
    "-i", SRC,
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,"
           f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={BG}",
    "-c:v", "libx264", "-crf", "23", "-preset", "fast",
    "-c:a", "copy",
    os.path.join(SEG, "recording_padded.mp4")
)

# =============================
# 3. End card (3.5s) with fade-in
# =============================
run(
    "-f", "lavfi", "-i", f"color={BG}:s=1920x1080:d=3.5",
    "-vf",
    f"drawtext=text='Live at':fontfile={FONT}:fontsize=28:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-70,"
    f"drawtext=text='fazly.web.id':fontfile={FONT}:fontsize=52:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-10,"
    f"drawtext=text='github.com/AtharFazli/BOTConfessions':fontfile={FONT}:fontsize=20:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+55,"
    f"drawtext=text='Submission Aug 4, 2026':fontfile={FONT}:fontsize=18:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+100,"
    f"fade=t=in:d=0.8",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "end_anim.mp4")
)

# =============================
# 4. Concat all segments + BGM
# =============================
filelist = os.path.join(SEG, "filelist_polished.txt")
with open(filelist, "w") as f:
    for name in ["title_anim.mp4", "recording_padded.mp4", "end_anim.mp4"]:
        f.write(f"file '{os.path.join(SEG, name)}'\n")

# First concat video only
run(
    "-f", "concat", "-safe", "0", "-i", filelist,
    "-c", "copy",
    os.path.join(SEG, "video_concat.mp4")
)

# Get duration of concat video
r = subprocess.run(
    [FFMPEG, "-i", os.path.join(SEG, "video_concat.mp4"),
     "-f", "null", "-"],
    capture_output=True, text=True
)
# Parse duration
for line in r.stderr.splitlines():
    if "Duration" in line:
        print("VIDEO:", line.strip())
        break

# Add BGM as sole audio track
run(
    "-i", os.path.join(SEG, "video_concat.mp4"),
    "-i", BGM,
    "-filter_complex",
    "[1:a]volume=0.15,aloop=loop=-1:size=44100*60[a]",
    "-map", "0:v", "-map", "[a]",
    "-c:v", "copy",
    "-c:a", "aac", "-b:a", "128k", "-shortest",
    "-movflags", "+faststart",
    OUT
)

print(f"DONE: {OUT}")
print(f"Size: {os.path.getsize(OUT) / 1024 / 1024:.1f} MB")
