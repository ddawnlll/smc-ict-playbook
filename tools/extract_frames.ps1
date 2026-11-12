param(
  [string]$SrcDir = "C:\Users\dresden\Documents\edge\imperial-research",
  [string]$OutRoot = "C:\Users\dresden\Documents\edge\frames",
  [int]$NumFrames = 14,
  [int]$Width = 640
)

$ErrorActionPreference = "Continue"
New-Item -ItemType Directory -Force -Path $OutRoot | Out-Null

$ffprobe = "ffprobe"; $ffmpeg = "ffmpeg"

Get-ChildItem "$SrcDir\*.mp4" | Sort-Object Name | ForEach-Object {
  $file = $_
  # derive video id from trailing [id] in filename
  if ($file.BaseName -match '\[([A-Za-z0-9_\-]{11})\]') { $vid = $matches[1] }
  else { $vid = $file.BaseName -replace '[^A-Za-z0-9_\-]', '_' }

  $dir = Join-Path $OutRoot $vid
  if (Test-Path $dir) { Remove-Item $dir -Recurse -Force }
  New-Item -ItemType Directory -Force -Path $dir | Out-Null

  $dur = [double](& $ffprobe -v error -show_entries format=duration -of csv=p=0 $file.FullName)
  if (-not $dur) { Write-Host "SKIP (no duration): $($file.Name)"; return }

  $step = $dur / $NumFrames
  # even sample: one frame every $step seconds
  $vf = "fps=1/$step,scale=${Width}:-2"
  & $ffmpeg -hide_banner -loglevel error -y -i $file.FullName -vf $vf -q:v 3 (Join-Path $dir "f%02d.jpg")

  $n = (Get-ChildItem "$dir\*.jpg" -ErrorAction SilentlyContinue).Count
  Write-Host ("{0}  dur={1}s  frames={2}" -f $vid, [math]::Round($dur,1), $n)
}
