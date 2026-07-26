"""Final video with voiceover + BGM + fade transitions."""
import subprocess, os

FF = r"C:\Users\MyBook Hype AMD\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"
SEG = r"D:\botconfessions\demo"
SRC = r"C:\Users\MyBook Hype AMD\Videos\OBS\2026-07-26 08-11-23.mp4"
VO = os.path.join(SEG, "voiceover.mp3")
BGM = os.path.join(SEG, "bgm.mp3")
OUT = r"D:\botconfessions\BOTConfessions_Demo_Final.mp4"
FONT = "'C\\:/Windows/Fonts/arial.ttf'"
BG = "0x14110e"

def run(*a):
    cmd = [FF, "-y"] + list(a)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-600:])
        raise SystemExit(r.returncode)

TD = 4    # title
RD = 53.8 # recording
ED = 4    # end
XF = 0.6

# 1. Title animated
run("-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:d={TD}:r=30",
    "-f", "lavfi", "-i", f"color=c=0x00000000:s=1920x1080:d={TD}:r=30,format=rgba",
    "-filter_complex",
    f"[1]drawtext=text='BOTConfessions':fontfile={FONT}:fontsize=76:fontcolor=white:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-80,fade=t=in:d=0.8:alpha=1[tx1];"
    f"[1]drawtext=text='Anonymous On-Chain Confession Board':fontfile={FONT}:fontsize=26:fontcolor=#ece8e2:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-10,fade=t=in:d=0.8:alpha=1:start_time=0.8[tx2];"
    f"[1]drawtext=text='GMT Build Week Hackathon':fontfile={FONT}:fontsize=22:fontcolor=#9c927e:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+50,fade=t=in:d=0.8:alpha=1:start_time=1.6[tx3];"
    f"[tx1][tx2]overlay[o1];[o1][tx3]overlay[txt];[0][txt]overlay[title_out]",
    "-map", "[title_out]",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p", "-shortest",
    os.path.join(SEG, "title_final.mp4"))

# 2. Pad recording
run("-i", SRC, "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,"
    f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={BG},setpts=PTS-STARTPTS,fps=30",
    "-c:v", "libx264", "-crf", "23", "-preset", "fast", "-an",
    os.path.join(SEG, "rec_30fps.mp4"))

# 3. End card animated
run("-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:d={ED}:r=30",
    "-f", "lavfi", "-i", f"color=c=0x00000000:s=1920x1080:d={ED}:r=30,format=rgba",
    "-filter_complex",
    f"[1]drawtext=text='Live at':fontfile={FONT}:fontsize=26:fontcolor=#ece8e2:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-70,fade=t=in:d=0.6:alpha=1[t1];"
    f"[1]drawtext=text='fazly.web.id':fontfile={FONT}:fontsize=56:fontcolor=#f59e0b:"
    f"x=(w-text_w)/2:y=(h-text_h)/2-10,fade=t=in:d=0.6:alpha=1:start_time=0.3[t2];"
    f"[1]drawtext=text='github.com/AtharFazli/BOTConfessions':fontfile={FONT}:fontsize=22:fontcolor=#9c927e:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+55,fade=t=in:d=0.6:alpha=1:start_time=0.6[t3];"
    f"[1]drawtext=text='Submission Aug 4, 2026':fontfile={FONT}:fontsize=18:fontcolor=#9c927e:"
    f"x=(w-text_w)/2:y=(h-text_h)/2+100,fade=t=in:d=0.6:alpha=1:start_time=0.9[t4];"
    f"[t1][t2]overlay[o1];[o1][t3]overlay[o2];[o2][t4]overlay[endtxt];[0][endtxt]overlay[end_out]",
    "-map", "[end_out]", "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p", "-shortest",
    os.path.join(SEG, "end_final.mp4"))

print("=== Segments ready. Building xfade chain ===")

# 4. xfade title -> recording
off1 = TD - XF
dur1 = off1 + RD
run("-i", os.path.join(SEG, "title_final.mp4"),
    "-i", os.path.join(SEG, "rec_30fps.mp4"),
    "-filter_complex", f"[0][1]xfade=transition=fade:duration={XF}:offset={off1}[vid]",
    "-map", "[vid]", "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "xfade1.mp4"))

# 5. xfade -> end
off2 = dur1 - XF
run("-i", os.path.join(SEG, "xfade1.mp4"),
    "-i", os.path.join(SEG, "end_final.mp4"),
    "-filter_complex", f"[0][1]xfade=transition=fade:duration={XF}:offset={off2}[vid]",
    "-map", "[vid]", "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "xfade2.mp4"))

print("=== Adding audio tracks ===")

# 6. Add voiceover + BGM
# Get video duration first
r = subprocess.run([FF, "-i", os.path.join(SEG, "xfade2.mp4")], capture_output=True, text=True)
vdur = 0
for l in r.stderr.splitlines():
    if "Duration" in l:
        import re
        m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', l)
        if m:
            vdur = int(m[1])*3600 + int(m[2])*60 + float(m[3])

# Voiceover: make sure it loops if needed (usually 7-8s)
# BGM: fill remaining time at lower volume
run(
    "-i", os.path.join(SEG, "xfade2.mp4"),
    "-i", VO,
    "-i", BGM,
    "-filter_complex",
    f"[1:a]adelay=0|0,volume=1.0[vo];"
    f"[2:a]volume=0.12[bgm];"
    f"[vo][bgm]amix=inputs=2:duration=first[mix]",
    "-map", "0:v", "-map", "[mix]",
    "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest",
    "-movflags", "+faststart",
    OUT
)

r = subprocess.run([FF, "-i", OUT], capture_output=True, text=True)
for l in r.stderr.splitlines():
    if "Duration" in l: print("DURATION:", l.strip())
print(f"DONE: {OUT}")
print(f"Size: {os.path.getsize(OUT)/1024/1024:.1f}MB")
