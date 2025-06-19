@echo off
echo =====================================
echo   QR Scanner - Build Script
echo =====================================
echo.

echo [1/3] Checking requirements...
if not exist "QRScanner.spec" (
    echo ❌ QRScanner.spec not found!
    pause
    exit /b 1
)

if not exist "icon.ico" (
    echo ❌ icon.ico not found!
    pause
    exit /b 1
)

echo ✅ All required files found

echo.
echo [2/3] Building application with PyInstaller...
echo 🧹 Cleaning previous builds...
rmdir /s /q build 2>nul
rmdir /s /q __pycache__ 2>nul

echo 🔨 Starting optimized build...
pyinstaller QRScanner.spec --clean

if %ERRORLEVEL% neq 0 (
    echo ❌ Build failed!
    pause
    exit /b 1
)

echo.
echo [3/3] Build completed successfully! 🎉

if exist "dist\QRScanner.exe" (
    echo ✅ Executable created: dist\QRScanner.exe
    echo    Size: 
    dir "dist\QRScanner.exe" | find "QRScanner.exe"
    echo.
    echo Run the application?
    echo 1. Yes - Run now
    echo 2. No - Just show location
    echo 3. Open dist folder
    echo.
    set /p choice="Enter your choice (1-3): "
    
    if "!choice!"=="1" (
        echo Starting QRScanner.exe...
        start "" "dist\QRScanner.exe"
    ) else if "!choice!"=="3" (
        echo Opening dist folder...
        start "" "dist"
    ) else (
        echo Application is ready at: dist\QRScanner.exe
    )
) else (
    echo ❌ Executable not found in dist folder
)

echo.
pause 