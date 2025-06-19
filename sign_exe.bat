@echo off
echo =======================================
echo   QR Scanner - Self-Signing Script
echo =======================================
echo.

REM Check if signtool exists (Windows SDK)
where signtool >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ❌ SignTool not found!
    echo Please install Windows SDK or Visual Studio
    echo Download: https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/
    pause
    exit /b 1
)

REM Create self-signed certificate if doesn't exist
if not exist "QRScannerCert.pfx" (
    echo 🔐 Creating self-signed certificate...
    
    REM Create certificate request
    powershell -Command "New-SelfSignedCertificate -Subject 'CN=QR Scanner Pro Ltd' -Type CodeSigningCert -KeySpec KeyExchange -KeyLength 2048 -Provider 'Microsoft Enhanced Cryptographic Provider v1.0' -CertStoreLocation 'cert:\CurrentUser\My' -KeyUsage DigitalSignature,KeyEncipherment -TextExtension @('2.5.29.37={text}1.3.6.1.5.5.7.3.3') | Export-PfxCertificate -FilePath QRScannerCert.pfx -Password (ConvertTo-SecureString -String 'QRScanner2025' -Force -AsPlainText)"
    
    if %ERRORLEVEL% neq 0 (
        echo ❌ Failed to create certificate!
        pause
        exit /b 1
    )
    
    echo ✅ Certificate created: QRScannerCert.pfx
)

REM Sign the executable
if exist "dist\QRScanner.exe" (
    echo 🖊️ Signing QRScanner.exe...
    
    signtool sign /f QRScannerCert.pfx /p QRScanner2025 /fd SHA256 /tr http://timestamp.sectigo.com /td SHA256 /v "dist\QRScanner.exe"
    
    if %ERRORLEVEL% equ 0 (
        echo ✅ Successfully signed QRScanner.exe!
        
        REM Verify signature
        signtool verify /pa /v "dist\QRScanner.exe"
        
        echo.
        echo 📋 Next steps to reduce false positives:
        echo    1. Submit to VirusTotal: https://www.virustotal.com/gui/home/upload
        echo    2. Report false positive to antivirus vendors
        echo    3. Use signed version for distribution
        
    ) else (
        echo ❌ Failed to sign executable!
    )
else (
    echo ❌ QRScanner.exe not found in dist folder!
    echo Please build the application first using build.bat
)

echo.
pause 