"""
Accura Finance - Cari Hesaplar Modülü
Müşteri ve tedarikçi yönetimi
"""

import customtkinter as ctk

class CustomersFrame(ctk.CTkFrame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.db_manager = main_app.db_manager
        
        self.create_interface()
    
    def create_interface(self):
        """Arayüzü oluştur"""
        # Başlık
        header_frame = ctk.CTkFrame(self, height=60, corner_radius=10)
        header_frame.pack(fill="x", padx=10, pady=(10, 5))
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="👥 CARİ HESAPLAR",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("#1f538d", "#14375e")
        )
        title_label.pack(side="left", padx=20, pady=15)
        
        # İçerik
        content_frame = ctk.CTkFrame(self, corner_radius=10)
        content_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        
        placeholder_label = ctk.CTkLabel(
            content_frame,
            text="CARİ HESAPLAR MODÜLÜ\n\nBu modül henüz geliştirme aşamasındadır.\n\n"
                 "• Müşteri yönetimi\n"
                 "• Tedarikçi yönetimi\n"
                 "• Cari hesap kartları\n"
                 "• Borç/alacak takibi\n"
                 "• Cari hesap raporları",
            font=ctk.CTkFont(size=16),
            justify="center"
        )
        placeholder_label.pack(expand=True)
