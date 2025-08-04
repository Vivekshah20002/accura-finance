@echo off
echo ======================================
echo     ACCURA FINANCE KURULUM
echo ======================================
echo.

echo Python surumu kontrol ediliyor...
python --version
if %errorlevel% neq 0 (
    echo HATA: Python bulunamadi!
    echo Lutfen Python 3.9 veya ustunu yukleyin.
    pause
    exit /b 1
)

echo.
echo Gerekli paketler yukleniyor...
pip install --upgrade pip
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo HATA: Paket yukleme basarisiz!
    pause
    exit /b 1
)

echo.
echo ======================================
echo     KURULUM TAMAMLANDI!
echo ======================================
echo.
echo Uygulamayi baslatmak icin:
echo   python main.py
echo.
pause
