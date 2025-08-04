"""
Accura Finance - Login Penceresi
Kullanıcı giriş ekranı
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import hashlib
import sys
import os

# Proje modüllerini import et
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

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
        # Gradient arka plan efekti için üst frame
        gradient_frame = ctk.CTkFrame(
            self.main_frame, 
            fg_color=("#f1f8ff", "#1a1a2e"),
            corner_radius=15,
            border_width=2,
            border_color=("#e3f2fd", "#16213e")
        )
        gradient_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Logo ve başlık alanı
        header_frame = ctk.CTkFrame(gradient_frame, fg_color="transparent")
        header_frame.pack(pady=(40, 30), fill="x")
        
        # Modern logo ve ikon kombinasyonu
        logo_container = ctk.CTkFrame(header_frame, fg_color="transparent")
        logo_container.pack(pady=(0, 20))
        
        # Ana logo ikon
        logo_label = ctk.CTkLabel(
            logo_container,
            text="�",
            font=ctk.CTkFont(size=70)
        )
        logo_label.pack()
        
        # Decorative icons
        icons_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        icons_frame.pack(pady=(0, 15))
        
        icon_text = "📊 💰 📈"
        icons_label = ctk.CTkLabel(
            icons_frame,
            text=icon_text,
            font=ctk.CTkFont(size=20)
        )
        icons_label.pack()
        
        # Modern başlık
        title_label = ctk.CTkLabel(
            header_frame,
            text="ACCURA FINANCE",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color=("#0d47a1", "#64b5f6")
        )
        title_label.pack()
        
        # Alt başlık gradyan efekti
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="💎 Profesyonel Muhasebe Çözümü 💎",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#1976d2", "#42a5f5")
        )
        subtitle_label.pack(pady=(8, 0))
        
        # Modern form alanı
        form_frame = ctk.CTkFrame(
            gradient_frame, 
            fg_color=("#ffffff", "#2b2b2b"),
            corner_radius=12,
            border_width=1,
            border_color=("#e0e0e0", "#404040")
        )
        form_frame.pack(pady=30, fill="x", padx=40)
        
        # Form içeriği
        form_content = ctk.CTkFrame(form_frame, fg_color="transparent")
        form_content.pack(pady=30, padx=30, fill="x")
        
        # Kullanıcı adı - Modern stil
        username_container = ctk.CTkFrame(form_content, fg_color="transparent")
        username_container.pack(fill="x", pady=(0, 20))
        
        username_label = ctk.CTkLabel(
            username_container,
            text="👤 Kullanıcı Adı",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#1565c0", "#90caf9")
        )
        username_label.pack(anchor="w", pady=(0, 8))
        
        self.username_entry = ctk.CTkEntry(
            username_container,
            height=50,
            font=ctk.CTkFont(size=15),
            placeholder_text="admin",
            corner_radius=10,
            border_width=2,
            border_color=("#bbdefb", "#1976d2")
        )
        self.username_entry.pack(fill="x")
        
        # Şifre - Modern stil
        password_container = ctk.CTkFrame(form_content, fg_color="transparent")
        password_container.pack(fill="x", pady=(0, 25))
        
        password_label = ctk.CTkLabel(
            password_container,
            text="🔒 Şifre",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#1565c0", "#90caf9")
        )
        password_label.pack(anchor="w", pady=(0, 8))
        
        self.password_entry = ctk.CTkEntry(
            password_container,
            height=50,
            font=ctk.CTkFont(size=15),
            placeholder_text="admin123",
            show="*",
            corner_radius=10,
            border_width=2,
            border_color=("#bbdefb", "#1976d2")
        )
        self.password_entry.pack(fill="x")
        
        # Modern checkbox
        options_frame = ctk.CTkFrame(form_content, fg_color="transparent")
        options_frame.pack(fill="x", pady=(0, 20))
        
        self.remember_var = ctk.BooleanVar()
        remember_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="🔄 Beni hatırla",
            variable=self.remember_var,
            font=ctk.CTkFont(size=14),
            checkbox_width=20,
            checkbox_height=20
        )
        remember_checkbox.pack(anchor="w")
        
        # Modern buton alanı
        button_frame = ctk.CTkFrame(form_content, fg_color="transparent")
        button_frame.pack(fill="x", pady=(10, 0))
        
        # Ana giriş butonu - Gradyan efekti
        self.login_button = ctk.CTkButton(
            button_frame,
            text="🚀 GİRİŞ YAP",
            height=55,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.login,
            fg_color=("#1565c0", "#1976d2"),
            hover_color=("#0d47a1", "#1565c0"),
            corner_radius=12,
            border_width=0
        )
        self.login_button.pack(fill="x", pady=(0, 15))
        
        # Demo buton
        demo_button = ctk.CTkButton(
            button_frame,
            text="🎯 Demo ile Dene",
            height=45,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.demo_login,
            fg_color=("#43a047", "#66bb6a"),
            hover_color=("#2e7d32", "#43a047"),
            corner_radius=10
        )
        demo_button.pack(fill="x")
        
        # Alt bilgi alanı
        footer_frame = ctk.CTkFrame(gradient_frame, fg_color="transparent")
        footer_frame.pack(pady=(0, 20), fill="x")
        
        # Versiyon bilgisi
        version_label = ctk.CTkLabel(
            footer_frame,
            text="⭐ Accura Finance v1.0 ⭐",
            font=ctk.CTkFont(size=12),
            text_color=("gray50", "gray60")
        )
        version_label.pack()
        
        # Copyright
        copyright_label = ctk.CTkLabel(
            footer_frame,
            text="© 2025 - Tüm hakları saklıdır",
            font=ctk.CTkFont(size=10),
            text_color=("gray40", "gray50")
        )
        copyright_label.pack(pady=(5, 0))
        
        # Enter tuşu ile giriş
        self.username_entry.bind("<Return>", lambda event: self.password_entry.focus())
        self.password_entry.bind("<Return>", lambda event: self.login())
    
    def demo_login(self):
        """Demo giriş - otomatik admin bilgileri"""
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.username_entry.insert(0, "admin")
        self.password_entry.insert(0, "admin123")
        self.login()
        
        version_label = ctk.CTkLabel(
            info_frame,
            text="Sürüm 1.0.0 | © 2025 Accura Finance",
            font=ctk.CTkFont(size=10),
            text_color=("gray50", "gray50")
        )
        version_label.pack()
        
        # Enter tuşu ile giriş
        self.login_window.bind('<Return>', lambda event: self.login())
        
        # Varsayılan odak
        self.username_entry.focus()
        
        # Varsayılan admin kullanıcısı (geliştirme için)
        self.username_entry.insert(0, "admin")
        self.password_entry.focus()
    
    def login(self):
        """Giriş işlemi"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username:
            messagebox.showerror("Hata", "Kullanıcı adı boş olamaz!")
            self.username_entry.focus()
            return
        
        if not password:
            messagebox.showerror("Hata", "Şifre boş olamaz!")
            self.password_entry.focus()
            return
        
        # Giriş butonunu deaktif et
        self.login_button.configure(state="disabled", text="Giriş yapılıyor...")
        self.login_window.update()
        
        try:
            # Kullanıcıyı veritabanından kontrol et
            user = self.authenticate_user(username, password)
            
            if user:
                self.logger.info(f"Başarılı giriş: {username}")
                
                # Başarılı giriş
                self.login_window.destroy()
                self.on_success_callback(user)
            else:
                self.logger.warning(f"Başarısız giriş: {username}")
                messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")
                self.password_entry.delete(0, 'end')
                self.password_entry.focus()
        
        except Exception as e:
            self.logger.error(f"Giriş hatası: {e}")
            messagebox.showerror("Hata", f"Giriş sırasında bir hata oluştu:\n{str(e)}")
        
        finally:
            # Giriş butonunu aktif et
            self.login_button.configure(state="normal", text="GİRİŞ YAP")
    
    def authenticate_user(self, username, password):
        """Kullanıcı doğrulama"""
        try:
            # Şifreyi hash'le
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            # Veritabanından kullanıcıyı sorgula
            query = """
            SELECT UserID, Username, FullName, Email, Role, IsActive, LastLogin
            FROM Users 
            WHERE Username = ? AND PasswordHash = ? AND IsActive = 1
            """
            
            result = self.db_manager.execute_query(query, (username, password_hash))
            
            if result and len(result) > 0:
                user = result[0]
                
                # Son giriş tarihini güncelle
                update_query = "UPDATE Users SET LastLogin = GETDATE() WHERE UserID = ?"
                self.db_manager.execute_query(update_query, (user['UserID'],), fetch=False)
                
                return user
            
            return None
            
        except Exception as e:
            self.logger.error(f"Kullanıcı doğrulama hatası: {e}")
            raise
    
    def forgot_password(self, event=None):
        """Şifre sıfırlama"""
        messagebox.showinfo(
            "Şifre Sıfırlama",
            "Şifre sıfırlama işlemi için sistem yöneticinizle iletişime geçiniz.\n\n"
            "Geliştirme aşamasında varsayılan admin şifresi: admin123"
        )
    
    def on_closing(self):
        """Pencere kapanma olayı"""
        self.login_window.destroy()
        self.parent.quit()

# Test için
if __name__ == "__main__":
    root = ctk.CTk()
    root.withdraw()  # Ana pencereyi gizle
    
    def test_callback(user):
        print(f"Giriş başarılı: {user}")
        root.quit()
    
    login = LoginWindow(root, test_callback)
    root.mainloop()
