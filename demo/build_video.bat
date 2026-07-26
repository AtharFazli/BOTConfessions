@echo off
setlocal enabledelayedexpansion

set FFMPEG=ffmpeg
set OUT="D:\botconfessions\demo_video.mp4"
set BGCOLOR=0x14110e

REM --- check images exist ---
if not exist "D:\botconfessions\demo\01_homepage.png" (echo Missing images & exit /b 1)
echo All images found, building...

REM --- Generate title card (3s) ---
%FFMPEG% -y -f lavfi -i color=%BGCOLOR%:s=1920x1080:d=3 -vf ^
  "drawtext=text='BOTConfessions':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=64:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2-60,^
   drawtext=text='Anonymous On-Chain Confession Board':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=26:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2+20,^
   drawtext=text='GMT Build Week Hackathon':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=22:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+70" ^
  -c:v libx264 -crf 23 -pix_fmt yuv420p "D:\botconfessions\demo\seg_title.mp4"

REM --- Scene 1: Homepage (5s) ---
%FFMPEG% -y -loop 1 -i "D:\botconfessions\demo\01_homepage.png" -vf ^
  "scale=iw*min(1080/ih, 900/iw)*0.85:ih*min(1080/ih, 900/iw)*0.85, pad=1920:1080:(1920-iw)/2:(1080-ih)/2:color=%BGCOLOR%,^
   drawtext=text='Confession Board - Live on Testnet':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=18:fontcolor=#f59e0b:x=(w/2)-text_w/2:y=30:box=1:boxcolor=#00000088:boxborderw=8" ^
  -c:v libx264 -crf 23 -t 5 -pix_fmt yuv420p "D:\botconfessions\demo\seg_scene1.mp4"

REM --- Scene 2: Compose area text (4s)--- 
REM Same image but focused description
%FFMPEG% -y -loop 1 -i "D:\botconfessions\demo\01_homepage.png" -vf ^
  "scale=iw*min(1080/ih, 900/iw)*0.85:ih*min(1080/ih, 900/iw)*0.85, pad=1920:1080:(1920-iw)/2:(1080-ih)/2:color=%BGCOLOR%,^
   drawtext=text='Connect Wallet → Confess (0.001 BOT) | Heart Confessions':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=16:fontcolor=#ece8e2:x=(w/2)-text_w/2:y=30:box=1:boxcolor=#00000088:boxborderw=8" ^
  -c:v libx264 -crf 23 -t 4 -pix_fmt yuv420p "D:\botconfessions\demo\seg_scene2.mp4"

REM --- Scene 3: GitHub repo (4s)---
%FFMPEG% -y -loop 1 -i "D:\botconfessions\demo\03_github.png" -vf ^
  "scale=iw*min(1080/ih, 1200/iw)*0.8:ih*min(1080/ih, 1200/iw)*0.8, pad=1920:1080:(1920-iw)/2:(1080-ih)/2:color=%BGCOLOR%,^
   drawtext=text='GitHub Repo: full-stack dapp':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=18:fontcolor=#f59e0b:x=(w/2)-text_w/2:y=30:box=1:boxcolor=#00000088:boxborderw=8,^
   drawtext=text='AtharFazli/BOTConfessions':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=16:fontcolor=#ece8e2:x=(w/2)-text_w/2:y=58:box=1:boxcolor=#00000088:boxborderw=8" ^
  -c:v libx264 -crf 23 -t 4 -pix_fmt yuv420p "D:\botconfessions\demo\seg_scene3.mp4"

REM --- Scene 4: Contract code (4s)---
%FFMPEG% -y -loop 1 -i "D:\botconfessions\demo\04_contract.png" -vf ^
  "scale=iw*min(1080/ih, 1200/iw)*0.8:ih*min(1080/ih, 1200/iw)*0.8, pad=1920:1080:(1920-iw)/2:(1080-ih)/2:color=%BGCOLOR%,^
   drawtext=text='Solidity Smart Contract':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=18:fontcolor=#f59e0b:x=(w/2)-text_w/2:y=30:box=1:boxcolor=#00000088:boxborderw=8,^
   drawtext=text='BOTChain | View at scan.botchain.ai':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=16:fontcolor=#ece8e2:x=(w/2)-text_w/2:y=58:box=1:boxcolor=#00000088:boxborderw=8" ^
  -c:v libx264 -crf 23 -t 4 -pix_fmt yuv420p "D:\botconfessions\demo\seg_scene4.mp4"

REM --- End card (3s)---
%FFMPEG% -y -f lavfi -i color=%BGCOLOR%:s=1920x1080:d=3 -vf ^
  "drawtext=text='Live at':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=30:fontcolor=#ece8e2:x=(w-text_w)/2:y=(h-text_h)/2-60,^
   drawtext=text='fazly.web.id':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=50:fontcolor=#f59e0b:x=(w-text_w)/2:y=(h-text_h)/2,^
   drawtext=text='github.com/AtharFazli/BOTConfessions':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=22:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+60,^
   drawtext=text='Submission Aug 4, 2026':fontfile=C\\:/Windows/Fonts/arial.ttf:fontsize=18:fontcolor=#9c927e:x=(w-text_w)/2:y=(h-text_h)/2+110" ^
  -c:v libx264 -crf 23 -pix_fmt yuv420p "D:\botconfessions\demo\seg_end.mp4"

echo --- Segments built, concatenating ---

REM --- Make file list for concat ---
del "D:\botconfessions\demo\filelist.txt" 2>nul
(for %%f in (
  "D:\botconfessions\demo\seg_title.mp4"
  "D:\botconfessions\demo\seg_scene1.mp4"
  "D:\botconfessions\demo\seg_scene2.mp4"
  "D:\botconfessions\demo\seg_scene3.mp4"
  "D:\botconfessions\demo\seg_scene4.mp4"
  "D:\botconfessions\demo\seg_end.mp4"
) do (
  echo file '%%~ff'
)) > "D:\botconfessions\demo\filelist.txt"

type "D:\botconfessions\demo\filelist.txt"

REM --- Concat everything ---
%FFMPEG% -y -f concat -safe 0 -i "D:\botconfessions\demo\filelist.txt" -c copy %OUT%

echo --- Done! ---
dir %OUT%
