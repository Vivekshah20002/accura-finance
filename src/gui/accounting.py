"""
Accura Finance - Muhasebe Modülü
Yevmiye, hesap planı ve muhasebe işlemleri
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date

class AccountingFrame(ctk.CTkFrame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.db_manager = main_app.db_manager
        
        self.create_accounting_interface()
    
    def create_accounting_interface(self):
        """Muhasebe arayüzünü oluştur"""
        # Grid yapılandırması
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Başlık
        self.create_header()
        
        # Tab widget
        self.create_tabs()
    
    def create_header(self):
        """Başlık alanı"""
        header_frame = ctk.CTkFrame(self, height=60, corner_radius=10)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        header_frame.grid_propagate(False)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="📝 MUHASEBE İŞLEMLERİ",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("#1f538d", "#14375e")
        )
        title_label.pack(side="left", padx=20, pady=15)
    
    def create_tabs(self):
        """Tab yapısı oluştur"""
        # Tab widget
        self.tabview = ctk.CTkTabview(self, corner_radius=10)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))
        
        # Tab'ları ekle
        self.tabview.add("Hesap Planı")
        self.tabview.add("Yevmiye")
        self.tabview.add("Defteri Kebir")
        self.tabview.add("Mizan")
        
        # Tab içeriklerini oluştur
        self.create_chart_of_accounts_tab()
        self.create_journal_tab()
        self.create_ledger_tab()
        self.create_trial_balance_tab()
    
    def create_chart_of_accounts_tab(self):
        """Hesap planı sekmesi"""
        tab = self.tabview.tab("Hesap Planı")
        
        # Placeholder içerik
        placeholder_label = ctk.CTkLabel(
            tab,
            text="HESAP PLANI\n\nBu modül henüz geliştirme aşamasındadır.\n\n"
                 "• Hesap planı yönetimi\n"
                 "• Yeni hesap ekleme\n"
                 "• Hesap düzenleme\n"
                 "• Hesap silme\n"
                 "• Hesap raporları",
            font=ctk.CTkFont(size=16),
            justify="center"
        )
        placeholder_label.pack(expand=True)
    
    def create_journal_tab(self):
        """Yevmiye sekmesi"""
        tab = self.tabview.tab("Yevmiye")
        
        placeholder_label = ctk.CTkLabel(
            tab,
            text="YEVMİYE DEFTERİ\n\nBu modül henüz geliştirme aşamasındadır.\n\n"
                 "• Yevmiye kayıtları\n"
                 "• Yeni kayıt ekleme\n"
                 "• Kayıt düzenleme\n"
                 "• Kayıt silme\n"
                 "• Yevmiye raporları",
            font=ctk.CTkFont(size=16),
            justify="center"
        )
        placeholder_label.pack(expand=True)
    
    def create_ledger_tab(self):
        """Defteri kebir sekmesi"""
        tab = self.tabview.tab("Defteri Kebir")
        
        placeholder_label = ctk.CTkLabel(
            tab,
            text="DEFTERİ KEBİR\n\nBu modül henüz geliştirme aşamasındadır.\n\n"
                 "• Hesap hareketleri\n"
                 "• Hesap bakiyeleri\n"
                 "• Hesap detayları\n"
                 "• Hareket sorgulama\n"
                 "• Kebir raporları",
            font=ctk.CTkFont(size=16),
            justify="center"
        )
        placeholder_label.pack(expand=True)
    
    def create_trial_balance_tab(self):
        """Mizan sekmesi"""
        tab = self.tabview.tab("Mizan")
        
        placeholder_label = ctk.CTkLabel(
            tab,
            text="MİZAN\n\nBu modül henüz geliştirme aşamasındadır.\n\n"
                 "• Mizan raporu\n"
                 "• Dönemsel mizan\n"
                 "• Detaylı mizan\n"
                 "• Özet mizan\n"
                 "• Mizan analizi",
            font=ctk.CTkFont(size=16),
            justify="center"
        )
        placeholder_label.pack(expand=True)
