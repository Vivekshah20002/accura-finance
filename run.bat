@echo off
echo ======================================
echo     ACCURA FINANCE MUHASEBE PROGRAMI
echo ======================================
echo.

echo Uygulama baslatiliyor...
.venv\Scripts\python.exe main.py

if %errorlevel% neq 0 (
    echo.
    echo HATA: Uygulama baslatma hatasi!
    echo.
    echo Olasi cozumler:
    echo 1. install.bat dosyasini calistirin
    echo 2. Python yuklu oldugundan emin olun
    echo 3. Gerekli paketlerin yuklu oldugundan emin olun
    echo.
    pause
)
