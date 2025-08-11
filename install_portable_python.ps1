$pythonVer = "3.13.5"
$pythonUrl = "https://www.python.org/ftp/python/$pythonVer/python-$pythonVer-embed-amd64.zip"
$pipUrl = "https://bootstrap.pypa.io/get-pip.py"
$tempPath = ".\temp"

# Create neccessary folders
if (-Not (Test-Path $tempPath)) {
    New-Item -ItemType Directory -Path $tempPath | Out-Null
}

# Set temporary location as main
Set-Location $tempPath

# Download+Unpack Python and save it to temporary folder
Write-Host "> Downloading Python v$pythonVer..."
Invoke-WebRequest -Uri $pythonUrl -OutFile "python-$pythonVer-embed.zip"
Write-Host "> Unpacking Python..."
Expand-Archive -Path "python-$pythonVer-embed.zip" -DestinationPath ".\python-win"

# Write _pth file to make portable
$pthFile = (Get-ChildItem python-win -Filter "python*._pth" | Select-Object -First 1).FullName
$zipName = (Get-ChildItem python-win -Filter "python*.zip" | Select-Object -First 1).Name
Set-Content -Path $pthFile -Value @"
$zipName
..
libs
import site
"@

# Download and install pip
Write-Host "> Downloading pip..."
Invoke-WebRequest -Uri $pipUrl -OutFile "get-pip.py"
Write-Host "> Installing pip..."
python-win/python.exe get-pip.py

# Download requirements.txt
Write-Host "> Downloading requirements..."
python-win/python.exe -m pip install -r ../requirements.txt --target python-win/libs

# Moving python-portable folder to project
Move-Item -Path ".\python-win" -Destination "..\python-win" -Force

# Cleaning 
Set-Location ".."
Remove-Item -Path $tempPath -Recurse