#!/bin/bash
# Build BOTConfessions demo video
FF="/c/Users/MyBook Hype AMD/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1.1-full_build/bin/ffmpeg.exe"
FONT="C:/Windows/Fonts/arial.ttf"
BG="0x14110e"
SEG="D:/botconfessions/demo"
OUT="D:/botconfessions/demo_video.mp4"

echo "Using ffmpeg: $FF"

# Write text files to avoid colon escaping issues in drawtext
echo "BOTConfessions" > "$SEG/t_title.txt"
echo "Anonymous On-Chain Confession Board" > "$SEG/t_sub.txt"
echo "GMT Build Week Hackathon" > "$SEG/t_hack.txt"
echo "Confession Board - Live on BOT Chain Testnet" > "$SEG/t_s1a.txt"
echo "16 confessions so far | Post: 0.001 BOT | No names" > "$SEG/t_s1b.txt"
echo "How It Works" > "$SEG/t_s2a.txt"
echo "Connect Wallet | Write Confession | Post | Tap Heart" > "$SEG/t_s2b.txt"
echo "Full-Stack DApp on GitHub" > "$SEG/t_s3a.txt"
echo "index.html + BOTConfessions.sol | 51 commits" > "$SEG/t_s3b.txt"
echo "Solidity Smart Contract" > "$SEG/t_s4a.txt"
echo "BOT Chain | Testnet 0x04e6db..." > "$SEG/t_s4b.txt"
echo "Live at" > "$SEG/t_e1.txt"
echo "fazly.web.id" > "$SEG/t_e2.txt"
echo "github.com/AtharFazli/BOTConfessions" > "$SEG/t_e3.txt"
echo "Submission: Aug 4, 2026" > "$SEG/t_e4.txt"

# ---- Title card (3s) ----
"$FF" -y -f lavfi -i "color=$BG:s=1920x1080:d=3.5" \
  -vf "drawtext=textfile=$SEG/t_title.txt:fontfile=$FONT:fontsize=64:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-80,\
       drawtext=textfile=$SEG/t_sub.txt:fontfile=$FONT:fontsize=26:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2,\
       drawtext=textfile=$SEG/t_hack.txt:fontfile=$FONT:fontsize=22:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+50" \
  -c:v libx264 -crf 23 -pix_fmt yuv420p "$SEG/title.mp4"

# ---- Screenshot scene function ----
scene() {
  local img=$1 textfile_a=$2 textfile_b=$3 dur=$4 out=$5
  $FF -y -loop 1 -i "$SEG/$img" \
    -vf "scale='min(1000,iw)':-1:force_original_aspect_ratio=decrease,pad=1920:1080:(1920-iw)/2:(1080-ih)/2:color=$BG,\
         drawtext=textfile=$textfile_a:fontfile=$FONT:fontsize=18:fontcolor=#f59e0b:x=(w/2)-text_w/2:y=30:box=1:boxcolor=#00000088:boxborderw=8,\
         drawtext=textfile=$textfile_b:fontfile=$FONT:fontsize=14:fontcolor=#ece8e2:x=(w/2)-text_w/2:y=56:box=1:boxcolor=#00000088:boxborderw=8" \
    -c:v libx264 -crf 23 -t "$dur" -pix_fmt yuv420p "$SEG/$out" || exit 1
}

scene "01_homepage.png" "$SEG/t_s1a.txt" "$SEG/t_s1b.txt" 6 "scene1.mp4"
scene "01_homepage.png" "$SEG/t_s2a.txt" "$SEG/t_s2b.txt" 4 "scene2.mp4"
scene "03_github.png" "$SEG/t_s3a.txt" "$SEG/t_s3b.txt" 5 "scene3.mp4"
scene "04_contract.png" "$SEG/t_s4a.txt" "$SEG/t_s4b.txt" 5 "scene4.mp4"

# ---- End card (3s) ----
$FF -y -f lavfi -i "color=$BG:s=1920x1080:d=3.5" \
  -vf "drawtext=textfile=$SEG/t_e1.txt:fontfile=$FONT:fontsize=28:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-70,\
       drawtext=textfile=$SEG/t_e2.txt:fontfile=$FONT:fontsize=52:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-10,\
       drawtext=textfile=$SEG/t_e3.txt:fontfile=$FONT:fontsize=20:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+55,\
       drawtext=textfile=$SEG/t_e4.txt:fontfile=$FONT:fontsize=18:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+100" \
  -c:v libx264 -crf 23 -pix_fmt yuv420p "$SEG/end.mp4" || exit 1

echo "=== All segments built ==="

# ---- Concat ----
rm -f "$SEG/filelist.txt"
for f in title.mp4 scene1.mp4 scene2.mp4 scene3.mp4 scene4.mp4 end.mp4; do
  echo "file '$SEG/$f'" >> "$SEG/filelist.txt"
done

$FF -y -f concat -safe 0 -i "$SEG/filelist.txt" -c copy "$OUT" || exit 1

echo "=== DONE: $OUT ==="
ls -lh "$OUT"
