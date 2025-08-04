"""
Accura Finance - Dashboard
Ana sayfa ve özet bilgiler
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from datetime import datetime, timedelta, date
import sys
import os

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.db_manager = main_app.db_manager
        
        self.create_dashboard()
        self.load_dashboard_data()
    
    def create_dashboard(self):
        """Dashboard arayüzünü oluştur"""
        # Ana container
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Başlık
        self.create_header()
        
        # Ana içerik
        self.create_main_content()
    
    def create_header(self):
        """Başlık alanı"""
        header_frame = ctk.CTkFrame(self, height=80, corner_radius=10)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        header_frame.grid_propagate(False)
        
        # Başlık metni - Modern gradyan tasarım
        title_container = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_container.pack(side="left", padx=20, pady=20)
        
        title_label = ctk.CTkLabel(
            title_container,
            text="🏢 DASHBOARD",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=("#0d47a1", "#64b5f6")
        )
        title_label.pack()
        
        subtitle_label = ctk.CTkLabel(
            title_container,
            text="💼 Finansal Kontrol Merkezi",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("#1976d2", "#42a5f5")
        )
        subtitle_label.pack()
        
        # Tarih ve bilgi alanı - Modern
        info_container = ctk.CTkFrame(header_frame, fg_color="transparent")
        info_container.pack(side="right", padx=20, pady=20)
        
        today = datetime.now().strftime("%d %B %Y")
        date_label = ctk.CTkLabel(
            info_container,
            text=f"📅 {today}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#1565c0", "#90caf9")
        )
        date_label.pack()
        
        time_label = ctk.CTkLabel(
            info_container,
            text=f"🕐 {datetime.now().strftime('%H:%M')}",
            font=ctk.CTkFont(size=12),
            text_color=("gray60", "gray40")
        )
        time_label.pack()
    
    def create_main_content(self):
        """Ana içerik alanı"""
        # Scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))
        self.scrollable_frame.grid_columnconfigure((0, 1), weight=1)
        
        # Özet kartlar
        self.create_summary_cards()
        
        # Grafikler
        self.create_charts_section()
        
        # Son işlemler
        self.create_recent_transactions()
        
        # Hızlı erişim
        self.create_quick_access()
    
    def create_summary_cards(self):
        """Modern özet kart alanı"""
        # Ana başlık
        title_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        
        main_title = ctk.CTkLabel(
            title_frame,
            text="📊 Finansal Özet",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=("#0d47a1", "#64b5f6")
        )
        main_title.pack(side="left", padx=20)
        
        # Kartlar container
        cards_container = ctk.CTkFrame(
            self.scrollable_frame, 
            corner_radius=15,
            fg_color=("#f8f9fa", "#2d2d2d"),
            border_width=1,
            border_color=("#e9ecef", "#3d3d3d")
        )
        cards_container.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 25))
        cards_container.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        # Kartlar
        self.summary_cards = {}
        
        # Toplam Satış - Yeşil gradient
        self.summary_cards['sales'] = self.create_modern_card(
            cards_container, "💰", "Toplam Satış", "0 ₺", "Bu ay ↗", 0, 0, 
            ("#4caf50", "#66bb6a"), ("#e8f5e8", "#2d4a2d")
        )
        
        # Toplam Alış - Kırmızı gradient  
        self.summary_cards['purchases'] = self.create_modern_card(
            cards_container, "🛒", "Toplam Alış", "0 ₺", "Bu ay ↗", 0, 1,
            ("#f44336", "#ef5350"), ("#ffebee", "#4a2d2d")
        )
        
        # Kasa Bakiyesi - Mavi gradient
        self.summary_cards['cash'] = self.create_modern_card(
            cards_container, "💵", "Kasa Bakiyesi", "0 ₺", "Toplam 💎", 0, 2,
            ("#2196f3", "#42a5f5"), ("#e3f2fd", "#2d3a4a")
        )
        
        # Banka Bakiyesi - Mor gradient
        self.summary_cards['bank'] = self.create_modern_card(
            cards_container, "🏦", "Banka Bakiyesi", "0 ₺", "Toplam 🏆", 0, 3,
            ("#9c27b0", "#ab47bc"), ("#f3e5f5", "#4a2d4a")
        )
    
    def create_modern_card(self, parent, icon, title, value, subtitle, row, col, main_color, bg_color):
        """Modern gradient kart oluştur"""
        # Ana kart frame
        card = ctk.CTkFrame(
            parent, 
            corner_radius=12,
            fg_color=bg_color,
            border_width=2,
            border_color=main_color
        )
        card.grid(row=row, column=col, padx=12, pady=15, sticky="ew")
        
        # İçerik container
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Üst alan - İkon ve başlık
        top_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        top_frame.pack(fill="x", pady=(0, 10))
        
        # İkon - Büyük ve parlak
        icon_label = ctk.CTkLabel(
            top_frame,
            text=icon,
            font=ctk.CTkFont(size=32)
        )
        icon_label.pack(side="left")
        
        # Başlık
        title_label = ctk.CTkLabel(
            top_frame,
            text=title,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=main_color
        )
        title_label.pack(side="right", anchor="e")
        
        # Değer - Büyük ve vurgulu
        value_label = ctk.CTkLabel(
            content_frame,
            text=value,
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=main_color
        )
        value_label.pack(anchor="w", pady=(0, 5))
        
        # Alt bilgi
        subtitle_label = ctk.CTkLabel(
            content_frame,
            text=subtitle,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=("gray50", "gray60")
        )
        subtitle_label.pack(anchor="w")
        
        return {
            'card': card,
            'value_label': value_label,
            'subtitle_label': subtitle_label
        }
    
    def create_charts_section(self):
        """Grafik alanı"""
        charts_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
        charts_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        charts_frame.grid_columnconfigure((0, 1), weight=1)
        
        # Başlık
        charts_title = ctk.CTkLabel(
            charts_frame,
            text="📊 Grafikler",
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="w"
        )
        charts_title.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(15, 10))
        
        # Sol grafik - Aylık Satış/Alış
        self.create_monthly_chart(charts_frame, 1, 0)
        
        # Sağ grafik - Cari Hesap Dağılımı
        self.create_pie_chart(charts_frame, 1, 1)
    
    def create_monthly_chart(self, parent, row, col):
        """Aylık satış/alış grafiği"""
        chart_frame = ctk.CTkFrame(parent, corner_radius=8)
        chart_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # Grafik başlığı
        chart_title = ctk.CTkLabel(
            chart_frame,
            text="Son 6 Ay Satış/Alış Karşılaştırması",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        chart_title.pack(pady=(10, 5))
        
        # Matplotlib figure
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor('#f0f0f0')
        ax.set_facecolor('#f8f8f8')
        
        # Örnek veri (gerçek verilerle değiştirilecek)
        months = ['Ağu', 'Eyl', 'Eki', 'Kas', 'Ara', 'Oca']
        sales = [150000, 180000, 220000, 190000, 250000, 200000]
        purchases = [120000, 140000, 180000, 150000, 200000, 160000]
        
        x = range(len(months))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], sales, width, label='Satış', color='#2e7d32', alpha=0.8)
        ax.bar([i + width/2 for i in x], purchases, width, label='Alış', color='#d32f2f', alpha=0.8)
        
        ax.set_xlabel('Aylar')
        ax.set_ylabel('Tutar (₺)')
        ax.set_xticks(x)
        ax.set_xticklabels(months)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Format y ekseni
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
        
        plt.tight_layout()
        
        # Canvas oluştur
        canvas = FigureCanvasTkAgg(fig, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=(0, 10))
    
    def create_pie_chart(self, parent, row, col):
        """Cari hesap dağılım grafiği"""
        chart_frame = ctk.CTkFrame(parent, corner_radius=8)
        chart_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # Grafik başlığı
        chart_title = ctk.CTkLabel(
            chart_frame,
            text="Cari Hesap Dağılımı",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        chart_title.pack(pady=(10, 5))
        
        # Matplotlib figure
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor('#f0f0f0')
        
        # Örnek veri
        labels = ['Müşteriler', 'Tedarikçiler', 'Personel', 'Diğer']
        sizes = [45, 30, 15, 10]
        colors = ['#2e7d32', '#d32f2f', '#1976d2', '#7b1fa2']
        explode = (0.1, 0, 0, 0)
        
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
               autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')
        
        plt.tight_layout()
        
        # Canvas oluştur
        canvas = FigureCanvasTkAgg(fig, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=(0, 10))
    
    def create_recent_transactions(self):
        """Son işlemler"""
        transactions_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
        transactions_frame.grid(row=2, column=0, sticky="nsew", padx=(0, 10), pady=(0, 20))
        transactions_frame.grid_columnconfigure(0, weight=1)
        
        # Başlık
        trans_title = ctk.CTkLabel(
            transactions_frame,
            text="📋 Son İşlemler",
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="w"
        )
        trans_title.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 10))
        
        # Tablo frame
        table_frame = ctk.CTkFrame(transactions_frame, fg_color="transparent")
        table_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 20))
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Tablo oluştur
        self.create_transactions_table(table_frame)
    
    def create_transactions_table(self, parent):
        """İşlemler tablosu"""
        # Tablo başlıkları
        headers = ["Tarih", "İşlem Tipi", "Açıklama", "Tutar"]
        
        # Başlık satırı
        header_frame = ctk.CTkFrame(parent, corner_radius=5)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        header_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        for i, header in enumerate(headers):
            label = ctk.CTkLabel(
                header_frame,
                text=header,
                font=ctk.CTkFont(size=12, weight="bold"),
                anchor="center"
            )
            label.grid(row=0, column=i, padx=5, pady=10)
        
        # Örnek veriler
        sample_data = [
            ["01.01.2025", "Satış Faturası", "ABC Ticaret - F001", "15.000 ₺"],
            ["31.12.2024", "Alış Faturası", "XYZ Tedarik - AF001", "-8.500 ₺"],
            ["30.12.2024", "Kasa Girişi", "Nakit Tahsilat", "5.000 ₺"],
            ["29.12.2024", "Banka Çıkışı", "Kira Ödemesi", "-12.000 ₺"],
            ["28.12.2024", "Satış Faturası", "DEF Ltd. - F002", "22.500 ₺"]
        ]
        
        # Veri satırları
        for i, row_data in enumerate(sample_data):
            row_frame = ctk.CTkFrame(parent, corner_radius=5, fg_color=("gray95", "gray15"))
            row_frame.grid(row=i+1, column=0, sticky="ew", pady=2)
            row_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
            
            for j, cell_data in enumerate(row_data):
                color = ("gray10", "gray90")
                if j == 3:  # Tutar sütunu
                    if "-" in cell_data:
                        color = ("#d32f2f", "#d32f2f")
                    else:
                        color = ("#2e7d32", "#2e7d32")
                
                label = ctk.CTkLabel(
                    row_frame,
                    text=cell_data,
                    font=ctk.CTkFont(size=11),
                    text_color=color,
                    anchor="center"
                )
                label.grid(row=0, column=j, padx=5, pady=8)
    
    def create_quick_access(self):
        """Hızlı erişim butonları"""
        quick_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
        quick_frame.grid(row=2, column=1, sticky="nsew", padx=(10, 0), pady=(0, 20))
        quick_frame.grid_columnconfigure(0, weight=1)
        
        # Başlık
        quick_title = ctk.CTkLabel(
            quick_frame,
            text="⚡ Hızlı Erişim",
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="w"
        )
        quick_title.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 10))
        
        # Butonlar
        buttons_frame = ctk.CTkFrame(quick_frame, fg_color="transparent")
        buttons_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 20))
        buttons_frame.grid_columnconfigure(0, weight=1)
        
        quick_buttons = [
            ("📝 Yeni Fatura", "invoice", self.new_invoice),
            ("💰 Kasa İşlemi", "cash", self.cash_operation),
            ("🏦 Banka İşlemi", "bank", self.bank_operation),
            ("👥 Yeni Cari", "customer", self.new_customer),
            ("📦 Stok Girişi", "stock", self.stock_entry),
            ("📊 Mizan Raporu", "report", self.balance_report)
        ]
        
        for i, (text, key, command) in enumerate(quick_buttons):
            btn = ctk.CTkButton(
                buttons_frame,
                text=text,
                font=ctk.CTkFont(size=12, weight="bold"),
                height=40,
                command=command,
                corner_radius=8
            )
            btn.grid(row=i, column=0, sticky="ew", pady=5)
    
    def load_dashboard_data(self):
        """Dashboard verilerini yükle"""
        try:
            # Toplam satış
            sales_data = self.get_monthly_sales()
            if sales_data:
                formatted_sales = self.format_currency(sales_data)
                self.summary_cards['sales']['value_label'].configure(text=formatted_sales)
            
            # Toplam alış
            purchases_data = self.get_monthly_purchases()
            if purchases_data:
                formatted_purchases = self.format_currency(purchases_data)
                self.summary_cards['purchases']['value_label'].configure(text=formatted_purchases)
            
            # Kasa bakiyesi
            cash_balance = self.get_cash_balance()
            if cash_balance:
                formatted_cash = self.format_currency(cash_balance)
                self.summary_cards['cash']['value_label'].configure(text=formatted_cash)
            
            # Banka bakiyesi
            bank_balance = self.get_bank_balance()
            if bank_balance:
                formatted_bank = self.format_currency(bank_balance)
                self.summary_cards['bank']['value_label'].configure(text=formatted_bank)
        
        except Exception as e:
            print(f"Dashboard veri yükleme hatası: {e}")
    
    def get_monthly_sales(self):
        """Bu ayın toplam satışını getir"""
        try:
            today = date.today()
            first_day = date(today.year, today.month, 1)
            
            query = """
            SELECT COALESCE(SUM(TotalAmount), 0) as TotalSales
            FROM Invoices 
            WHERE InvoiceType = 'Satis' 
            AND InvoiceDate >= ? 
            AND InvoiceDate <= ?
            """
            
            result = self.db_manager.execute_query(query, (first_day, today))
            return result[0]['TotalSales'] if result else 0
        except:
            return 0
    
    def get_monthly_purchases(self):
        """Bu ayın toplam alışını getir"""
        try:
            today = date.today()
            first_day = date(today.year, today.month, 1)
            
            query = """
            SELECT COALESCE(SUM(TotalAmount), 0) as TotalPurchases
            FROM Invoices 
            WHERE InvoiceType = 'Alis' 
            AND InvoiceDate >= ? 
            AND InvoiceDate <= ?
            """
            
            result = self.db_manager.execute_query(query, (first_day, today))
            return result[0]['TotalPurchases'] if result else 0
        except:
            return 0
    
    def get_cash_balance(self):
        """Toplam kasa bakiyesini getir"""
        try:
            query = "SELECT COALESCE(SUM(CurrentBalance), 0) as TotalCash FROM CashRegisters WHERE IsActive = 1"
            result = self.db_manager.execute_query(query)
            return result[0]['TotalCash'] if result else 0
        except:
            return 0
    
    def get_bank_balance(self):
        """Toplam banka bakiyesini getir"""
        try:
            query = "SELECT COALESCE(SUM(CurrentBalance), 0) as TotalBank FROM Banks WHERE IsActive = 1"
            result = self.db_manager.execute_query(query)
            return result[0]['TotalBank'] if result else 0
        except:
            return 0
    
    def format_currency(self, amount):
        """Para birimi formatla"""
        if amount is None:
            amount = 0
        return f"{amount:,.2f} ₺".replace(",", ".")
    
    # Hızlı erişim fonksiyonları
    def new_invoice(self):
        """Yeni fatura"""
        self.main_app.show_module('invoices')
    
    def cash_operation(self):
        """Kasa işlemi"""
        self.main_app.show_module('cashbank')
    
    def bank_operation(self):
        """Banka işlemi"""
        self.main_app.show_module('cashbank')
    
    def new_customer(self):
        """Yeni cari"""
        self.main_app.show_module('customers')
    
    def stock_entry(self):
        """Stok girişi"""
        self.main_app.show_module('inventory')
    
    def balance_report(self):
        """Mizan raporu"""
        self.main_app.show_module('reports')
