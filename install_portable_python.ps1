# install_portable_python.ps1
$ErrorActionPreference = "Stop"

$pythonVer = "3.13.5"
$pythonUrl = "https://www.python.org/ftp/python/$pythonVer/python-$pythonVer-embed-amd64.zip"
$pipUrl    = "https://bootstrap.pypa.io/get-pip.py"

# Work from this script's folder
$Root   = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $Root

$outDir = Join-Path $Root "python-win"
$zip    = Join-Path $Root "python-embed.zip"
$getpip = Join-Path $Root "get-pip.py"

# Fresh install location
if (Test-Path $outDir) {
  Remove-Item $outDir -Recurse -Force
}

Write-Host "> Downloading Python $pythonVer..."
Invoke-WebRequest -Uri $pythonUrl -OutFile $zip

Write-Host "> Unpacking to $outDir..."
Expand-Archive -Path $zip -DestinationPath $outDir -Force

# Prepare ._pth (enable site + libs) BEFORE pip
$pthFile = Get-ChildItem $outDir -Filter "python*._pth" | Select-Object -First 1
if (-not $pthFile) { throw "Could not find python*._pth in $outDir" }
$zipName = (Get-ChildItem $outDir -Filter "python*.zip" | Select-Object -First 1).Name
New-Item -ItemType Directory -Path (Join-Path $outDir "libs") -Force | Out-Null

Set-Content -Path $pthFile.FullName -Value @"
$zipName
..
libs
import site
"@

Write-Host "> Downloading get-pip.py..."
Invoke-WebRequest -Uri $pipUrl -OutFile $getpip

Write-Host "> Installing pip..."
& (Join-Path $outDir "python.exe") $getpip

# Install requirements if present
$req = Join-Path $Root "requirements.txt"
if (Test-Path $req) {
  Write-Host "> Installing requirements to python-win/libs..."
  & (Join-Path $outDir "python.exe") -m pip install -r $req --target (Join-Path $outDir "libs")
} else {
  Write-Host "> requirements.txt not found; skipping."
}

# Cleanup
Remove-Item $zip -Force -ErrorAction SilentlyContinue
Remove-Item $getpip -Force -ErrorAction SilentlyContinue

Write-Host "> Done. Python at: $outDir\python.exe"
