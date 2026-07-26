"""Simple version with BGM only."""
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
    print(" ".join(cmd[:6]) + "...")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-500:])
        raise SystemExit(r.returncode)

# 1. Title card (4s)
run("-f", "lavfi", "-i", f"color={BG}:s=1920x1080:d=4", "-vf",
    f"drawtext=text='BOTConfessions':fontfile={FONT}:fontsize=72:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-80,"
    f"drawtext=text='Anonymous On-Chain Confession Board':fontfile={FONT}:fontsize=28:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-10,"
    f"drawtext=text='GMT Build Week Hackathon':fontfile={FONT}:fontsize=24:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+50",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "t2.mp4"))

# 2. Resize recording
run("-i", SRC,
    "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={BG}",
    "-c:v", "libx264", "-crf", "23", "-preset", "fast",
    "-c:a", "copy",
    os.path.join(SEG, "rec_pad.mp4"))

# 3. End card (4s)
run("-f", "lavfi", "-i", f"color={BG}:s=1920x1080:d=4", "-vf",
    f"drawtext=text='Live at':fontfile={FONT}:fontsize=28:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-70,"
    f"drawtext=text='fazly.web.id':fontfile={FONT}:fontsize=52:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-10,"
    f"drawtext=text='github.com/AtharFazli/BOTConfessions':fontfile={FONT}:fontsize=20:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+55,"
    f"drawtext=text='Submission Aug 4, 2026':fontfile={FONT}:fontsize=18:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+100",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "e2.mp4"))

# 4. Concat video only
with open(os.path.join(SEG, "fl2.txt"), "w") as f:
    for name in ["t2.mp4", "rec_pad.mp4", "e2.mp4"]:
        f.write(f"file '{os.path.join(SEG, name)}'\n")
run("-f", "concat", "-safe", "0", "-i", os.path.join(SEG, "fl2.txt"),
    "-c", "copy",
    os.path.join(SEG, "vc2.mp4"))

# 5. Add BGM (just loop with shortest)
# Use amix with anullsrc to pad if needed
run("-i", os.path.join(SEG, "vc2.mp4"),
    "-i", BGM,
    "-filter_complex",
    "[1:a]volume=0.12[a]",
    "-map", "0:v", "-map", "[a]",
    "-c:v", "copy",
    "-c:a", "aac", "-b:a", "128k", "-shortest",
    "-movflags", "+faststart",
    OUT)

# Check
r = subprocess.run([FFMPEG, "-i", OUT], capture_output=True, text=True)
for line in r.stderr.splitlines():
    if "Duration" in line:
        print("DURATION:", line.strip())
print(f"DONE: {OUT}")
print(f"Size: {os.path.getsize(OUT)/1024/1024:.1f}MB")
