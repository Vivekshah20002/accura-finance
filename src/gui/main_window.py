"""
Accura Finance - Ana Uygulama Penceresi
Modern CustomTkinter tabanlı arayüz
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os
from datetime import datetime, date
import threading
import logging

# Proje modüllerini import et
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.database.connection import get_database_manager
    from src.utils.config import ConfigManager
    from src.utils.logger import setup_logger
    from src.gui.login_window import LoginWindow
except ImportError as e:
    print(f"Modül import hatası: {e}")
    # Alternatif import yolu dene
    try:
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
        from src.database.connection import get_database_manager
        from src.utils.config import ConfigManager
        from src.utils.logger import setup_logger
        from src.gui.login_window import LoginWindow
    except ImportError as e2:
        print(f"Alternatif import da başarısız: {e2}")
        ConfigManager = None

# GUI modüllerini lazy import
DashboardFrame = None
AccountingFrame = None
InventoryFrame = None
CustomersFrame = None
ReportsFrame = None
SettingsFrame = None

# Modern tema ayarları
ctk.set_appearance_mode("light")  # "light" veya "dark"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class AccuraFinanceApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.current_user = None
        self.db_manager = None
        
        # ConfigManager kontrolü
        if ConfigManager is not None:
            self.config_manager = ConfigManager()
        else:
            self.config_manager = None
            print("Uyarı: ConfigManager yüklenemedi, varsayılan ayarlar kullanılacak")
            
        self.logger = setup_logger('AccuraFinance') if 'setup_logger' in globals() else None
        
        # Ana pencere yapılandırması
        self.setup_main_window()
        
        # Veritabanı bağlantısını kontrol et
        self.check_database_connection()
        
        # Login penceresi göster
        self.show_login()
    
    def setup_main_window(self):
        """Ana pencere ayarları"""
        self.root.title("🏢 Accura Finance - Profesyonel Muhasebe Çözümü v1.0")
        self.root.geometry("1500x950")
        self.root.minsize(1300, 850)
        
        # Modern tema renkleri
        ctk.set_appearance_mode("light")  
        ctk.set_default_color_theme("blue")
        
        # İkon ayarla (varsa)
        try:
            icon_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'icon.ico')
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except:
            pass
        
        # Pencere kapanma olayı
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Ana layout'u oluştur
        self.create_main_layout()
        
        # Başlangıçta ana içeriği gizle
        self.hide_main_content()
    
    def create_main_layout(self):
        """Ana layout oluştur"""
        # Grid yapılandırması
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        
        # Üst toolbar
        self.create_toolbar()
        
        # Sol sidebar
        self.create_sidebar()
        
        # Ana içerik alanı
        self.create_main_content()
        
        # Alt durum çubuğu
        self.create_status_bar()
    
    def create_toolbar(self):
        """Üst araç çubuğu"""
        self.toolbar = ctk.CTkFrame(self.root, height=60, corner_radius=0)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=0, pady=0)
        self.toolbar.grid_columnconfigure(1, weight=1)
        
        # Logo ve başlık
        title_frame = ctk.CTkFrame(self.toolbar, fg_color="transparent")
        title_frame.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        
        title_label = ctk.CTkLabel(
            title_frame, 
            text="💰 ACCURA FINANCE", 
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("#1f538d", "#14375e")
        )
        title_label.pack(side="left")
        
        # Kullanıcı bilgileri ve çıkış
        self.user_frame = ctk.CTkFrame(self.toolbar, fg_color="transparent")
        self.user_frame.grid(row=0, column=1, sticky="e", padx=20, pady=10)
        
        self.user_label = ctk.CTkLabel(self.user_frame, text="", font=ctk.CTkFont(size=12))
        self.user_label.pack(side="left", padx=(0, 10))
        
        self.logout_btn = ctk.CTkButton(
            self.user_frame,
            text="Çıkış",
            width=80,
            height=30,
            command=self.logout,
            fg_color=("#d32f2f", "#b71c1c"),
            hover_color=("#b71c1c", "#8b0000")
        )
        self.logout_btn.pack(side="right")
    
    def create_sidebar(self):
        """Sol menü çubuğu"""
        self.sidebar = ctk.CTkFrame(self.root, width=250, corner_radius=0)
        self.sidebar.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.sidebar.grid_propagate(False)
        
        # Menü başlığı
        menu_title = ctk.CTkLabel(
            self.sidebar, 
            text="MENÜ", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        menu_title.pack(pady=(20, 10))
        
        # Menü öğeleri
        self.menu_buttons = {}
        self.create_menu_buttons()
    
    def create_menu_buttons(self):
        """Menü butonlarını oluştur"""
        menu_items = [
            ("📊 Dashboard", "dashboard", "Ana sayfa ve özet bilgiler"),
            ("📝 Muhasebe", "accounting", "Yevmiye, hesap planı, raporlar"),
            ("👥 Cari Hesaplar", "customers", "Müşteri ve tedarikçi yönetimi"),
            ("📦 Stok Yönetimi", "inventory", "Stok kartları ve hareketleri"),
            ("💰 Kasa & Banka", "cashbank", "Kasa ve banka işlemleri"),
            ("🧾 Faturalar", "invoices", "Alış/satış faturaları"),
            ("👤 Personel", "personnel", "Personel ve bordro yönetimi"),
            ("📈 Raporlar", "reports", "Mali raporlar ve analizler"),
            ("⚙️ Ayarlar", "settings", "Sistem ve şirket ayarları")
        ]
        
        for text, key, tooltip in menu_items:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                width=220,
                height=40,
                anchor="w",
                font=ctk.CTkFont(size=14),
                command=lambda k=key: self.show_module(k),
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray80", "gray20")
            )
            btn.pack(pady=5, padx=15)
            self.menu_buttons[key] = btn
            
            # Tooltip ekle
            self.create_tooltip(btn, tooltip)
    
    def create_tooltip(self, widget, text):
        """Tooltip oluştur"""
        def on_enter(event):
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25
            
            self.tooltip = tk.Toplevel(widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")
            
            label = tk.Label(
                self.tooltip,
                text=text,
                background="lightyellow",
                relief="solid",
                borderwidth=1,
                font=("Arial", 9)
            )
            label.pack()
        
        def on_leave(event):
            if hasattr(self, 'tooltip'):
                self.tooltip.destroy()
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
    
    def create_main_content(self):
        """Ana içerik alanı"""
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.main_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # İçerik frame'leri için sözlük
        self.content_frames = {}
        
        # Dashboard frame'ini oluştur (varsayılan)
        self.create_dashboard_frame()
    
    def create_dashboard_frame(self):
        """Dashboard frame oluştur"""
        if 'dashboard' not in self.content_frames:
            try:
                from src.gui.dashboard import DashboardFrame
                self.content_frames['dashboard'] = DashboardFrame(self.main_frame, self)
            except Exception as e:
                self.logger.error(f"Dashboard oluşturma hatası: {e}")
                # Hata durumunda basit frame oluştur
                frame = ctk.CTkFrame(self.main_frame)
                label = ctk.CTkLabel(
                    frame, 
                    text="Dashboard yüklenemedi\nBasit görünüm",
                    font=ctk.CTkFont(size=16),
                    justify="center"
                )
                label.pack(expand=True)
                self.content_frames['dashboard'] = frame
    
    def create_status_bar(self):
        """Alt durum çubuğu"""
        self.status_bar = ctk.CTkFrame(self.root, height=30, corner_radius=0)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew", padx=0, pady=0)
        self.status_bar.grid_columnconfigure(1, weight=1)
        
        # Sol taraf - durum mesajı
        self.status_label = ctk.CTkLabel(
            self.status_bar, 
            text="Hazır", 
            font=ctk.CTkFont(size=11)
        )
        self.status_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        # Sağ taraf - tarih ve saat
        self.datetime_label = ctk.CTkLabel(
            self.status_bar, 
            text="", 
            font=ctk.CTkFont(size=11)
        )
        self.datetime_label.grid(row=0, column=1, sticky="e", padx=10, pady=5)
        
        # Tarih/saat güncelleme
        self.update_datetime()
    
    def update_datetime(self):
        """Tarih ve saati güncelle"""
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.datetime_label.configure(text=current_time)
        self.root.after(1000, self.update_datetime)
    
    def check_database_connection(self):
        """Veritabanı bağlantısını kontrol et"""
        try:
            if 'get_database_manager' in globals():
                self.db_manager = get_database_manager()
                
                # Veritabanını oluştur (yoksa)
                if not self.db_manager.create_database_if_not_exists():
                    self.show_error("Veritabanı oluşturulamadı!")
                    return False
                
                # Bağlantıyı test et
                if not self.db_manager.test_connection():
                    self.show_error("Veritabanı bağlantısı başarısız!")
                    return False
                
                # Tabloları oluştur
                self.initialize_database()
                
                if self.logger:
                    self.logger.info("Veritabanı bağlantısı başarılı")
                print("Veritabanı bağlantısı başarılı")
                return True
            else:
                print("Uyarı: get_database_manager fonksiyonu bulunamadı")
                self.db_manager = None
                return False
            
        except Exception as e:
            if self.logger:
                self.logger.error(f"Veritabanı bağlantı hatası: {e}")
            else:
                print(f"Veritabanı bağlantı hatası: {e}")
            self.show_error(f"Veritabanı hatası: {e}")
            return False
    
    def initialize_database(self):
        """Veritabanını başlat"""
        try:
            # SQL script'lerini çalıştır
            script_dir = os.path.join(os.path.dirname(__file__), '..', 'database')
            
            # Tabloları oluştur (IF NOT EXISTS kontrolü ile)
            tables_script = os.path.join(script_dir, 'create_tables.sql')
            if os.path.exists(tables_script):
                try:
                    self.db_manager.execute_script(tables_script)
                    if self.logger:
                        self.logger.info("Veritabanı tabloları kontrol edildi")
                except Exception as e:
                    # Tablo zaten varsa hatayı yok say
                    if "already an object named" in str(e):
                        print("Veritabanı tabloları zaten mevcut")
                        if self.logger:
                            self.logger.info("Veritabanı tabloları zaten mevcut")
                    else:
                        raise e
            
            # Başlangıç verilerini ekle
            data_script = os.path.join(script_dir, 'initial_data.sql')
            if os.path.exists(data_script):
                # Sadece ilk kurulumda çalıştır
                try:
                    result = self.db_manager.execute_query(
                        "SELECT COUNT(*) as count FROM Users WHERE Username = 'admin'"
                    )
                    if result and result[0]['count'] == 0:
                        self.db_manager.execute_script(data_script)
                        if self.logger:
                            self.logger.info("Başlangıç verileri eklendi")
                        print("Başlangıç verileri eklendi")
                    else:
                        print("Admin kullanıcısı zaten mevcut")
                except Exception as e:
                    print(f"Başlangıç verileri kontrol hatası: {e}")
            
        except Exception as e:
            if self.logger:
                self.logger.error(f"Veritabanı başlatma hatası: {e}")
            else:
                print(f"Veritabanı başlatma hatası: {e}")
    
    def show_login(self):
        """Login penceresi göster"""
        self.login_window = LoginWindow(self.root, self.on_login_success)
    
    def on_login_success(self, user_data):
        """Login başarılı olduğunda"""
        self.current_user = user_data
        self.user_label.configure(text=f"Hoş geldiniz, {user_data['FullName']}")
        
        # Ana içeriği göster
        self.show_main_content()
        
        # Dashboard'u göster
        self.show_module('dashboard')
        
        # Status bar'ı güncelle
        self.status_label.configure(text="Giriş başarılı")
        
        self.logger.info(f"Kullanıcı giriş yaptı: {user_data['Username']}")
    
    def show_main_content(self):
        """Ana içeriği göster"""
        self.sidebar.grid(row=1, column=0, sticky="nsew")
        self.main_frame.grid(row=1, column=1, sticky="nsew")
    
    def hide_main_content(self):
        """Ana içeriği gizle"""
        self.sidebar.grid_remove()
        self.main_frame.grid_remove()
    
    def show_module(self, module_key):
        """Modül göster"""
        # Tüm frame'leri gizle
        for frame in self.content_frames.values():
            frame.pack_forget()
        
        # İstenen frame'i göster veya oluştur
        if module_key not in self.content_frames:
            self.create_content_frame(module_key)
        
        if module_key in self.content_frames:
            self.content_frames[module_key].pack(fill="both", expand=True)
            self.status_label.configure(text=f"{module_key.title()} modülü açıldı")
        
        # Menü butonlarının rengini güncelle
        self.update_menu_selection(module_key)
    
    def create_content_frame(self, module_key):
        """İçerik frame oluştur"""
        try:
            if module_key == 'dashboard':
                from src.gui.dashboard import DashboardFrame
                self.content_frames[module_key] = DashboardFrame(self.main_frame, self)
            elif module_key == 'accounting':
                from src.gui.accounting import AccountingFrame
                self.content_frames[module_key] = AccountingFrame(self.main_frame, self)
            elif module_key == 'customers':
                from src.gui.customers import CustomersFrame
                self.content_frames[module_key] = CustomersFrame(self.main_frame, self)
            elif module_key == 'inventory':
                from src.gui.inventory import InventoryFrame
                self.content_frames[module_key] = InventoryFrame(self.main_frame, self)
            elif module_key == 'reports':
                from src.gui.reports import ReportsFrame
                self.content_frames[module_key] = ReportsFrame(self.main_frame, self)
            elif module_key == 'settings':
                from src.gui.settings import SettingsFrame
                self.content_frames[module_key] = SettingsFrame(self.main_frame, self)
            else:
                # Geçici placeholder frame
                frame = ctk.CTkFrame(self.main_frame)
                label = ctk.CTkLabel(
                    frame, 
                    text=f"{module_key.upper()} MODÜLÜ\n\nBu modül henüz geliştirilme aşamasındadır.",
                    font=ctk.CTkFont(size=16),
                    justify="center"
                )
                label.pack(expand=True)
                self.content_frames[module_key] = frame
        
        except Exception as e:
            self.logger.error(f"Modül oluşturma hatası ({module_key}): {e}")
            # Hata durumunda basit bir frame oluştur
            frame = ctk.CTkFrame(self.main_frame)
            label = ctk.CTkLabel(
                frame, 
                text=f"HATA: {module_key} modülü yüklenemedi\n{str(e)}",
                font=ctk.CTkFont(size=14),
                text_color="red"
            )
            label.pack(expand=True)
            self.content_frames[module_key] = frame
    
    def update_menu_selection(self, selected_key):
        """Menü seçimini güncelle"""
        for key, button in self.menu_buttons.items():
            if key == selected_key:
                button.configure(
                    fg_color=("#3b8ed0", "#1f538d"),
                    text_color=("white", "white")
                )
            else:
                button.configure(
                    fg_color="transparent",
                    text_color=("gray10", "gray90")
                )
    
    def logout(self):
        """Çıkış yap"""
        if messagebox.askyesno("Çıkış", "Oturumu kapatmak istediğinizden emin misiniz?"):
            self.current_user = None
            self.user_label.configure(text="")
            self.hide_main_content()
            self.show_login()
            self.status_label.configure(text="Çıkış yapıldı")
            self.logger.info("Kullanıcı çıkış yaptı")
    
    def on_closing(self):
        """Uygulama kapanırken"""
        if messagebox.askyesno("Çıkış", "Uygulamayı kapatmak istediğinizden emin misiniz?"):
            self.logger.info("Uygulama kapatılıyor")
            self.root.destroy()
    
    def show_error(self, message):
        """Hata mesajı göster"""
        messagebox.showerror("Hata", message)
    
    def show_info(self, message):
        """Bilgi mesajı göster"""
        messagebox.showinfo("Bilgi", message)
    
    def show_warning(self, message):
        """Uyarı mesajı göster"""
        messagebox.showwarning("Uyarı", message)
    
    def run(self):
        """Uygulamayı başlat"""
        self.logger.info("Accura Finance uygulaması başlatılıyor")
        self.root.mainloop()

def main():
    """Ana fonksiyon"""
    try:
        app = AccuraFinanceApp()
        app.run()
    except Exception as e:
        logging.error(f"Uygulama başlatma hatası: {e}")
        messagebox.showerror("Kritik Hata", f"Uygulama başlatılamadı:\n{e}")

if __name__ == "__main__":
    main()
