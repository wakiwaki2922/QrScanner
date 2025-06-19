@echo off
echo Building QR Scanner...

pip install -r requirements.txt
pip install pyinstaller

if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

pyinstaller QRScanner.spec --clean

if exist "dist\QRScanner.exe" (
    echo Build successful: dist\QRScanner.exe
) else (
    echo Build failed!
)

pause 