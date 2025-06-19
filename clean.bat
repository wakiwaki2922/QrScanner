@echo off
echo =====================================
echo   QR Scanner - Cleanup Script
echo =====================================
echo.

echo [1/5] Deleting PyInstaller build files...
if exist "build" (
    rmdir /s /q "build"
    echo ✅ Deleted build/ folder
) else (
    echo ⚠️  build/ folder not found
)

echo.
echo [2/5] Deleting PyInstaller dist files...
if exist "dist" (
    rmdir /s /q "dist"
    echo ✅ Deleted dist/ folder
) else (
    echo ⚠️  dist/ folder not found
)

echo.
echo [3/5] Deleting PyInstaller spec backup...
if exist "*.spec.backup" (
    del /q "*.spec.backup"
    echo ✅ Deleted spec backup files
)

echo.
echo [4/5] Deleting Python cache files...
if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo ✅ Deleted __pycache__/ folder
)
if exist "*.pyc" (
    del /q "*.pyc"
    echo ✅ Deleted .pyc files
)

echo.
echo [5/5] Deleting temporary icon files...
if exist "icon_preview.png" (
    del /q "icon_preview.png"
    echo ✅ Deleted icon_preview.png
)

echo.
echo =====================================
echo   Cleanup completed! 🎉
echo =====================================
echo.
echo Files remaining:
dir /b *.py *.txt *.ico *.spec *.md 2>nul
echo.
echo To rebuild the application:
echo   pyinstaller QRScanner.spec
echo.
pause 