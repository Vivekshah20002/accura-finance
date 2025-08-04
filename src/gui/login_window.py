"""
Accura Finance - Login Penceresi (Yeni Temiz Tasarım)
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import hashlib
import sys
import os

# Database bağlantısı için
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.database.connection import get_database_manager
    from src.utils.logger import setup_logger
except ImportError as e:
    print(f"Modül import hatası: {e}")

class LoginWindow:
    def __init__(self, parent, on_success_callback):
        self.parent = parent
        self.on_success_callback = on_success_callback
        self.db_manager = get_database_manager()
        self.logger = setup_logger('Login')
        
        self.create_login_window()
    
    def create_login_window(self):
        """Login penceresi oluştur"""
        self.login_window = ctk.CTkToplevel(self.parent)
        self.login_window.title("Accura Finance - Giriş")
        self.login_window.geometry("400x500")
        self.login_window.resizable(False, False)
        
        # Ana pencereyi deaktif et
        self.login_window.transient(self.parent)
        self.login_window.grab_set()
        
        # Pencereyi ortala
        self.center_window()
        
        # Ana frame - temiz beyaz tasarım
        self.main_frame = ctk.CTkFrame(
            self.login_window, 
            corner_radius=0,
            fg_color=("#ffffff", "#2b2b2b")
        )
        self.main_frame.pack(fill="both", expand=True)
        
        self.create_login_form()
    
    def center_window(self):
        """Pencereyi ekranın ortasına yerleştir"""
        self.login_window.update_idletasks()
        width = self.login_window.winfo_width()
        height = self.login_window.winfo_height()
        x = (self.login_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.login_window.winfo_screenheight() // 2) - (height // 2)
        self.login_window.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_login_form(self):
        """Login formu oluştur"""
        # Ana container
        container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Logo ve başlık alanı
        header_frame = ctk.CTkFrame(container, fg_color="transparent")
        header_frame.pack(pady=(0, 30))
        
        # Logo
        logo_label = ctk.CTkLabel(
            header_frame,
            text="💼",
            font=ctk.CTkFont(size=48)
        )
        logo_label.pack(pady=(0, 15))
        
        # Başlık
        title_label = ctk.CTkLabel(
            header_frame,
            text="ACCURA FINANCE",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("#2c3e50", "#ecf0f1")
        )
        title_label.pack(pady=(0, 5))
        
        # Alt başlık
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Muhasebe Programı",
            font=ctk.CTkFont(size=14),
            text_color=("#7f8c8d", "#bdc3c7")
        )
        subtitle_label.pack()
        
        # Form alanları
        form_frame = ctk.CTkFrame(container, fg_color="transparent")
        form_frame.pack(fill="x", pady=(0, 20))
        
        # Kullanıcı adı
        username_label = ctk.CTkLabel(
            form_frame,
            text="Kullanıcı Adı",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        username_label.pack(fill="x", pady=(0, 5))
        
        self.username_entry = ctk.CTkEntry(
            form_frame,
            height=40,
            font=ctk.CTkFont(size=14),
            placeholder_text="admin",
            corner_radius=8
        )
        self.username_entry.pack(fill="x", pady=(0, 15))
        
        # Şifre
        password_label = ctk.CTkLabel(
            form_frame,
            text="Şifre",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        password_label.pack(fill="x", pady=(0, 5))
        
        self.password_entry = ctk.CTkEntry(
            form_frame,
            height=40,
            font=ctk.CTkFont(size=14),
            placeholder_text="admin123",
            show="*",
            corner_radius=8
        )
        self.password_entry.pack(fill="x", pady=(0, 20))
        
        # Hatırla checkbox
        self.remember_var = ctk.BooleanVar()
        remember_checkbox = ctk.CTkCheckBox(
            form_frame,
            text="Beni hatırla",
            variable=self.remember_var,
            font=ctk.CTkFont(size=12)
        )
        remember_checkbox.pack(anchor="w", pady=(0, 25))
        
        # Butonlar
        button_frame = ctk.CTkFrame(container, fg_color="transparent")
        button_frame.pack(fill="x")
        
        # Giriş butonu
        self.login_button = ctk.CTkButton(
            button_frame,
            text="Giriş Yap",
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.login,
            corner_radius=8
        )
        self.login_button.pack(fill="x", pady=(0, 10))
        
        # Demo butonu
        demo_button = ctk.CTkButton(
            button_frame,
            text="Demo ile Dene",
            height=35,
            font=ctk.CTkFont(size=12),
            command=self.demo_login,
            fg_color="transparent",
            border_width=1,
            text_color=("#3498db", "#74b9ff"),
            border_color=("#3498db", "#74b9ff"),
            hover_color=("#ecf0f1", "#2d3436"),
            corner_radius=8
        )
        demo_button.pack(fill="x")
        
        # Alt bilgi
        footer_frame = ctk.CTkFrame(container, fg_color="transparent")
        footer_frame.pack(side="bottom")
        
        footer_label = ctk.CTkLabel(
            footer_frame,
            text="© 2025 Accura Finance v1.0",
            font=ctk.CTkFont(size=10),
            text_color=("#95a5a6", "#7f8c8d")
        )
        footer_label.pack()
        
        # Enter tuşu desteği
        self.username_entry.bind("<Return>", lambda event: self.password_entry.focus())
        self.password_entry.bind("<Return>", lambda event: self.login())
    
    def demo_login(self):
        """Demo giriş - otomatik admin bilgileri"""
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.username_entry.insert(0, "admin")
        self.password_entry.insert(0, "admin123")
        self.login()
    
    def login(self):
        """Giriş işlemi"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showerror("Hata", "Lütfen kullanıcı adı ve şifre giriniz!")
            return
        
        try:
            # Kullanıcı doğrulama
            user = self.authenticate_user(username, password)
            
            if user:
                self.logger.info(f"Başarılı giriş: {username}")
                messagebox.showinfo("Başarılı", f"Hoş geldiniz, {user['FullName']}!")
                
                # Ana pencereye kullanıcı bilgilerini gönder
                self.on_success_callback(user)
                
                # Login penceresini kapat
                self.login_window.destroy()
            else:
                self.logger.warning(f"Başarısız giriş: {username}")
                messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")
        
        except Exception as e:
            self.logger.error(f"Giriş hatası: {e}")
            messagebox.showerror("Hata", f"Giriş yapılırken hata oluştu: {e}")
    
    def authenticate_user(self, username, password):
        """Kullanıcı doğrulama"""
        try:
            # Şifreyi hash'le
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            # Veritabanından kullanıcıyı kontrol et
            query = """
            SELECT UserID, Username, FullName, Email, Role 
            FROM Users 
            WHERE Username = ? AND PasswordHash = ? AND IsActive = 1
            """
            
            result = self.db_manager.execute_query(query, (username, password_hash))
            
            if result and len(result) > 0:
                return result[0]
            else:
                return None
        
        except Exception as e:
            self.logger.error(f"Kullanıcı doğrulama hatası: {e}")
            return None
