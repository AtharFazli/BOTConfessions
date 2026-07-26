"""Build BOTConfessions demo video via Python subprocess."""
import subprocess, os

FFMPEG = r"C:\Users\MyBook Hype AMD\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"
FONT = "'C\\:/Windows/Fonts/arial.ttf'"  # single-quoted for drawtext filter
SEG = r"D:\botconfessions\demo"
OUT = r"D:\botconfessions\demo_video.mp4"
BG = "0x14110e"

def run(*args):
    cmd = [FFMPEG, "-y"] + list(args)
    print(" ".join(cmd[:8]) + "...")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("STDERR:", r.stderr[-500:])
        raise SystemExit(r.returncode)

def scene(img, text_a, text_b, dur, out):
    vf = (
        f"scale=1920:1080:force_original_aspect_ratio=decrease,"
        f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={BG},"
        f"drawtext=text='{text_a}':fontfile={FONT}:fontsize=18:fontcolor=#f59e0b:"
        f"x=(w/2)-text_w/2:y=30:box=1:boxcolor=#00000088:boxborderw=8,"
        f"drawtext=text='{text_b}':fontfile={FONT}:fontsize=14:fontcolor=#ece8e2:"
        f"x=(w/2)-text_w/2:y=56:box=1:boxcolor=#00000088:boxborderw=8"
    )
    run("-loop", "1", "-i", os.path.join(SEG, img), "-vf", vf,
        "-c:v", "libx264", "-crf", "23", "-t", str(dur), "-pix_fmt", "yuv420p",
        os.path.join(SEG, out))

# Title card
run("-f", "lavfi", "-i", f"color={BG}:s=1920x1080:d=3.5", "-vf",
    f"drawtext=text='BOTConfessions':fontfile={FONT}:fontsize=64:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-80,"
    f"drawtext=text='Anonymous On-Chain Confession Board':fontfile={FONT}:fontsize=26:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2,"
    f"drawtext=text='GMT Build Week Hackathon':fontfile={FONT}:fontsize=22:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+50",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "title.mp4"))

scene("01_homepage.png", "Confession Board - Live on BOT Chain Testnet", "16 confessions | Post 0.001 BOT | No names. No history.", 6, "scene1.mp4")
scene("01_homepage.png", "How It Works", "Connect Wallet => Write Confession => Post | Tap Heart (0.001 BOT)", 4, "scene2.mp4")
scene("03_github.png", "Full-Stack DApp on GitHub", "index.html + BOTConfessions.sol | 51 commits", 5, "scene3.mp4")
scene("04_contract.png", "Solidity Smart Contract", "BOT Chain Testnet | 0x04e6db5BE9861fbEd3E7a4192A3444a7D0e07cb4", 5, "scene4.mp4")

# End card
run("-f", "lavfi", "-i", f"color={BG}:s=1920x1080:d=3.5", "-vf",
    f"drawtext=text='Live at':fontfile={FONT}:fontsize=28:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-70,"
    f"drawtext=text='fazly.web.id':fontfile={FONT}:fontsize=52:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-10,"
    f"drawtext=text='github.com/AtharFazli/BOTConfessions':fontfile={FONT}:fontsize=20:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+55,"
    f"drawtext=text='Submission Aug 4, 2026':fontfile={FONT}:fontsize=18:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+100",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    os.path.join(SEG, "end.mp4"))

print("=== All segments built ===")

# Concat
filelist = os.path.join(SEG, "filelist.txt")
with open(filelist, "w") as f:
    for name in ["title.mp4", "scene1.mp4", "scene2.mp4", "scene3.mp4", "scene4.mp4", "end.mp4"]:
        f.write(f"file '{os.path.join(SEG, name)}'\n")

run("-f", "concat", "-safe", "0", "-i", filelist, "-c", "copy", OUT)
print(f"=== DONE: {OUT} ===")
print(f"Size: {os.path.getsize(OUT) / 1024 / 1024:.1f} MB")
