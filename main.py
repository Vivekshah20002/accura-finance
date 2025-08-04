"""
Accura Finance - Ana Başlatıcı
Tam kapsamlı muhasebe programı
"""

import sys
import os
import traceback
from pathlib import Path

# Proje kök dizinini sys.path'e ekle
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def main():
    """Ana fonksiyon"""
    try:
        # GUI modülünü import et
        from src.gui.main_window import AccuraFinanceApp
        
        # Uygulamayı başlat
        app = AccuraFinanceApp()
        app.run()
        
    except ImportError as e:
        print("HATA: Gerekli Python paketleri bulunamadı!")
        print(f"Detay: {e}")
        print("\nÇözüm:")
        print("1. Gerekli paketleri yükleyin:")
        print("   pip install -r requirements.txt")
        print("\n2. Eğer paketler yüklüyse, Python environment'ını kontrol edin")
        input("\nDevam etmek için Enter tuşuna basın...")
        
    except Exception as e:
        print("KRITIK HATA: Uygulama başlatılamadı!")
        print(f"Hata: {e}")
        print("\nDetaylı hata bilgisi:")
        traceback.print_exc()
        input("\nDevam etmek için Enter tuşuna basın...")

if __name__ == "__main__":
    main()
