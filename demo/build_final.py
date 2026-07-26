"""Final polished: xfade transitions + animated text overlay + BGM."""
import subprocess, os

FF = r"C:\Users\MyBook Hype AMD\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"
SEG = r"D:\botconfessions\demo"
SRC = r"C:\Users\MyBook Hype AMD\Videos\OBS\2026-07-26 08-11-23.mp4"
BGM = os.path.join(SEG, "bgm.mp3")
OUT = r"D:\botconfessions\BOTConfessions_Demo_Final.mp4"
FONT = "'C\\:/Windows/Fonts/arial.ttf'"
BG = "0x14110e"

def run(*a):
    cmd = [FF, "-y"] + list(a)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-700:])
        raise SystemExit(r.returncode)

TD = 4     # title duration
RD = 53.8  # recording duration
ED = 4     # end duration
XF = 0.6   # crossfade duration

# --- 1. Title with fade-in text ---
# Generate as 3 streams: bg color + text overlay, then overlay text fades in
run(
    "-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:d={TD}:r=30",
    "-f", "lavfi", "-i", f"color=c=0x00000000:s=1920x1080:d={TD}:r=30,format=rgba",
    "-filter_complex",
    # White text on transparent bg, then fade in
    f"[1]drawtext=text='BOTConfessions':fontfile={FONT}:fontsize=76:fontcolor=white:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-80,"
    f"fade=t=in:d=0.8:alpha=1[tx1];"
    f"[1]drawtext=text='Anonymous On-Chain Confession Board':fontfile={FONT}:fontsize=26:fontcolor=#ece8e2:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-10,"
    f"fade=t=in:d=0.8:alpha=1:start_time=0.8[tx2];"
    f"[1]drawtext=text='GMT Build Week Hackathon':fontfile={FONT}:fontsize=22:fontcolor=#9c927e:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+50,"
    f"fade=t=in:d=0.8:alpha=1:start_time=1.6[tx3];"
    f"[tx1][tx2]overlay[ov1];[ov1][tx3]overlay[txt];"
    f"[0][txt]overlay[title_out]",
    "-map", "[title_out]",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    "-shortest",
    os.path.join(SEG, "title_final.mp4")
)

# --- 2. Pad recording ---
run(
    "-i", SRC,
    "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,"
           f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={BG},"
           f"setpts=PTS-STARTPTS,fps=30",
    "-c:v", "libx264", "-crf", "23", "-preset", "fast",
    "-an",
    os.path.join(SEG, "rec_30fps.mp4")
)

# --- 3. End card with animated text ---
run(
    "-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:d={ED}:r=30",
    "-f", "lavfi", "-i", f"color=c=0x00000000:s=1920x1080:d={ED}:r=30,format=rgba",
    "-filter_complex",
    f"[1]drawtext=text='Live at':fontfile={FONT}:fontsize=26:fontcolor=#ece8e2:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-70,"
    f"fade=t=in:d=0.6:alpha=1[t1];"
    f"[1]drawtext=text='fazly.web.id':fontfile={FONT}:fontsize=56:fontcolor=#f59e0b:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-10,"
    f"fade=t=in:d=0.6:alpha=1:start_time=0.3[t2];"
    f"[1]drawtext=text='github.com/AtharFazli/BOTConfessions':fontfile={FONT}:fontsize=22:fontcolor=#9c927e:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+55,"
    f"fade=t=in:d=0.6:alpha=1:start_time=0.6[t3];"
    f"[1]drawtext=text='Submission Aug 4, 2026':fontfile={FONT}:fontsize=18:fontcolor=#9c927e:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+100,"
    f"fade=t=in:d=0.6:alpha=1:start_time=0.9[t4];"
    f"[t1][t2]overlay[o1];[o1][t3]overlay[o2];[o2][t4]overlay[endtxt];"
    f"[0][endtxt]overlay[end_out]",
    "-map", "[end_out]",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    "-shortest",
    os.path.join(SEG, "end_final.mp4")
)

print("=== Segments ready, building xfade chain ===")

# --- 4. xfade title -> recording ---
# Title: 4s. xfade starts at offset=3.4 (0.6s crossfade)
off1 = TD - XF  # 3.4
dur1 = off1 + RD  # 3.4 + 53.8 = 57.2

run(
    "-i", os.path.join(SEG, "title_final.mp4"),
    "-i", os.path.join(SEG, "rec_30fps.mp4"),
    "-filter_complex",
    f"[0][1]xfade=transition=fade:duration={XF}:offset={off1}[vid]",
    "-map", "[vid]",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "xfade1.mp4")
)

# --- 5. xfade previous -> end card ---
# Second xfade: input0 = xfade1 (57.2s), input1 = end_final (4s)
# Transition at end of recording: 57.2 - XF = 56.6
off2 = dur1 - XF  # 56.6

run(
    "-i", os.path.join(SEG, "xfade1.mp4"),
    "-i", os.path.join(SEG, "end_final.mp4"),
    "-filter_complex",
    f"[0][1]xfade=transition=fade:duration={XF}:offset={off2}[vid]",
    "-map", "[vid]",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "xfade2.mp4")
)

# --- 6. Add BGM ---
run(
    "-i", os.path.join(SEG, "xfade2.mp4"),
    "-i", BGM,
    "-filter_complex", "[1:a]volume=0.12[a]",
    "-map", "0:v", "-map", "[a]",
    "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest",
    "-movflags", "+faststart",
    OUT
)

# Result
r = subprocess.run([FF, "-i", OUT], capture_output=True, text=True)
for l in r.stderr.splitlines():
    if "Duration" in l: print("VIDEO:", l.strip())
print(f"DONE: {OUT}")
print(f"Size: {os.path.getsize(OUT)/1024/1024:.1f}MB")
