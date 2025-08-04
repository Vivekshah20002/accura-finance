"""
Accura Finance - Veritabanı Modelleri
SQLAlchemy ORM modelleri
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Numeric, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
from datetime import datetime, date
import hashlib

Base = declarative_base()

class Company(Base):
    __tablename__ = 'Companies'
    
    CompanyID = Column(Integer, primary_key=True, autoincrement=True)
    CompanyName = Column(String(200), nullable=False)
    TaxNumber = Column(String(50), unique=True, nullable=False)
    TaxOffice = Column(String(100))
    Address = Column(String(500))
    Phone = Column(String(50))
    Email = Column(String(100))
    Website = Column(String(100))
    LogoPath = Column(String(500))
    CreatedDate = Column(DateTime, default=func.now())
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    IsActive = Column(Boolean, default=True)

class User(Base):
    __tablename__ = 'Users'
    
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String(50), unique=True, nullable=False)
    PasswordHash = Column(String(255), nullable=False)
    FullName = Column(String(100), nullable=False)
    Email = Column(String(100))
    Phone = Column(String(50))
    Role = Column(String(50), nullable=False)  # Admin, Muhasebeci, Kullanici
    IsActive = Column(Boolean, default=True)
    LastLogin = Column(DateTime)
    CreatedDate = Column(DateTime, default=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    creator = relationship("User", remote_side=[UserID])
    
    def set_password(self, password):
        """Şifreyi hash'le ve kaydet"""
        self.PasswordHash = hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        """Şifreyi kontrol et"""
        return self.PasswordHash == hashlib.sha256(password.encode()).hexdigest()

class ChartOfAccount(Base):
    __tablename__ = 'ChartOfAccounts'
    
    AccountID = Column(Integer, primary_key=True, autoincrement=True)
    AccountCode = Column(String(20), unique=True, nullable=False)
    AccountName = Column(String(200), nullable=False)
    ParentAccountID = Column(Integer, ForeignKey('ChartOfAccounts.AccountID'))
    AccountType = Column(String(50), nullable=False)  # Aktif, Pasif, Gelir, Gider, Özkaynaklar
    AccountGroup = Column(String(100))
    IsDetailAccount = Column(Boolean, default=False)
    CurrencyCode = Column(String(3), default='TRY')
    IsActive = Column(Boolean, default=True)
    CreatedDate = Column(DateTime, default=func.now())
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    parent = relationship("ChartOfAccount", remote_side=[AccountID])
    children = relationship("ChartOfAccount")
    journal_details = relationship("JournalEntryDetail", back_populates="account")

class CurrentAccount(Base):
    __tablename__ = 'CurrentAccounts'
    
    CurrentAccountID = Column(Integer, primary_key=True, autoincrement=True)
    CurrentAccountCode = Column(String(20), unique=True, nullable=False)
    CurrentAccountName = Column(String(200), nullable=False)
    CurrentAccountType = Column(String(50), nullable=False)  # Musteri, Tedarikci, Personel, Diger
    TaxNumber = Column(String(50))
    TaxOffice = Column(String(100))
    Address = Column(String(500))
    City = Column(String(50))
    District = Column(String(50))
    PostalCode = Column(String(10))
    Phone = Column(String(50))
    Mobile = Column(String(50))
    Email = Column(String(100))
    Website = Column(String(100))
    ContactPerson = Column(String(100))
    PaymentTerm = Column(Integer, default=0)
    CreditLimit = Column(Numeric(18, 2), default=0)
    RiskLimit = Column(Numeric(18, 2), default=0)
    IsActive = Column(Boolean, default=True)
    CreatedDate = Column(DateTime, default=func.now())
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    creator = relationship("User")
    invoices = relationship("Invoice", back_populates="current_account")
    journal_details = relationship("JournalEntryDetail", back_populates="current_account")

class StockCategory(Base):
    __tablename__ = 'StockCategories'
    
    CategoryID = Column(Integer, primary_key=True, autoincrement=True)
    CategoryCode = Column(String(20), unique=True, nullable=False)
    CategoryName = Column(String(100), nullable=False)
    ParentCategoryID = Column(Integer, ForeignKey('StockCategories.CategoryID'))
    Description = Column(String(500))
    IsActive = Column(Boolean, default=True)
    CreatedDate = Column(DateTime, default=func.now())
    
    # Relationships
    parent = relationship("StockCategory", remote_side=[CategoryID])
    children = relationship("StockCategory")
    stock_items = relationship("StockItem", back_populates="category")

class StockItem(Base):
    __tablename__ = 'StockItems'
    
    StockID = Column(Integer, primary_key=True, autoincrement=True)
    StockCode = Column(String(50), unique=True, nullable=False)
    StockName = Column(String(200), nullable=False)
    CategoryID = Column(Integer, ForeignKey('StockCategories.CategoryID'))
    Unit = Column(String(20), nullable=False)
    Barcode = Column(String(50))
    Description = Column(String(500))
    PurchasePrice = Column(Numeric(18, 4), default=0)
    SalePrice = Column(Numeric(18, 4), default=0)
    MinStockLevel = Column(Numeric(18, 2), default=0)
    MaxStockLevel = Column(Numeric(18, 2), default=0)
    CurrentStock = Column(Numeric(18, 2), default=0)
    VATRate = Column(Numeric(5, 2), default=18.00)
    IsActive = Column(Boolean, default=True)
    CreatedDate = Column(DateTime, default=func.now())
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    category = relationship("StockCategory", back_populates="stock_items")
    creator = relationship("User")
    movements = relationship("StockMovement", back_populates="stock_item")
    invoice_details = relationship("InvoiceDetail", back_populates="stock_item")

class CashRegister(Base):
    __tablename__ = 'CashRegisters'
    
    CashRegisterID = Column(Integer, primary_key=True, autoincrement=True)
    CashRegisterCode = Column(String(20), unique=True, nullable=False)
    CashRegisterName = Column(String(100), nullable=False)
    CurrencyCode = Column(String(3), default='TRY')
    OpeningBalance = Column(Numeric(18, 2), default=0)
    CurrentBalance = Column(Numeric(18, 2), default=0)
    ResponsiblePerson = Column(String(100))
    IsActive = Column(Boolean, default=True)
    CreatedDate = Column(DateTime, default=func.now())
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    movements = relationship("CashMovement", back_populates="cash_register")

class Bank(Base):
    __tablename__ = 'Banks'
    
    BankID = Column(Integer, primary_key=True, autoincrement=True)
    BankCode = Column(String(20), unique=True, nullable=False)
    BankName = Column(String(100), nullable=False)
    AccountNumber = Column(String(50))
    IBAN = Column(String(50))
    BranchName = Column(String(100))
    BranchCode = Column(String(20))
    CurrencyCode = Column(String(3), default='TRY')
    OpeningBalance = Column(Numeric(18, 2), default=0)
    CurrentBalance = Column(Numeric(18, 2), default=0)
    ResponsiblePerson = Column(String(100))
    IsActive = Column(Boolean, default=True)
    CreatedDate = Column(DateTime, default=func.now())
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    movements = relationship("BankMovement", back_populates="bank")

class JournalEntry(Base):
    __tablename__ = 'JournalEntries'
    
    JournalEntryID = Column(Integer, primary_key=True, autoincrement=True)
    VoucherNumber = Column(String(50), unique=True, nullable=False)
    VoucherDate = Column(Date, nullable=False)
    Description = Column(String(500))
    TotalDebit = Column(Numeric(18, 2), nullable=False)
    TotalCredit = Column(Numeric(18, 2), nullable=False)
    IsBalanced = Column(Boolean, default=False)
    IsPosted = Column(Boolean, default=False)
    PostedDate = Column(DateTime)
    DocumentType = Column(String(50))
    DocumentNumber = Column(String(50))
    CreatedDate = Column(DateTime, default=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    ApprovedBy = Column(Integer, ForeignKey('Users.UserID'))
    ApprovedDate = Column(DateTime)
    
    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy])
    approver = relationship("User", foreign_keys=[ApprovedBy])
    details = relationship("JournalEntryDetail", back_populates="journal_entry", cascade="all, delete-orphan")

class JournalEntryDetail(Base):
    __tablename__ = 'JournalEntryDetails'
    
    JournalDetailID = Column(Integer, primary_key=True, autoincrement=True)
    JournalEntryID = Column(Integer, ForeignKey('JournalEntries.JournalEntryID'), nullable=False)
    LineNumber = Column(Integer, nullable=False)
    AccountID = Column(Integer, ForeignKey('ChartOfAccounts.AccountID'), nullable=False)
    CurrentAccountID = Column(Integer, ForeignKey('CurrentAccounts.CurrentAccountID'))
    Description = Column(String(500))
    DebitAmount = Column(Numeric(18, 2), default=0)
    CreditAmount = Column(Numeric(18, 2), default=0)
    CurrencyCode = Column(String(3), default='TRY')
    ExchangeRate = Column(Numeric(10, 4), default=1)
    DebitAmountLocal = Column(Numeric(18, 2), default=0)
    CreditAmountLocal = Column(Numeric(18, 2), default=0)
    
    # Relationships
    journal_entry = relationship("JournalEntry", back_populates="details")
    account = relationship("ChartOfAccount", back_populates="journal_details")
    current_account = relationship("CurrentAccount", back_populates="journal_details")

class Invoice(Base):
    __tablename__ = 'Invoices'
    
    InvoiceID = Column(Integer, primary_key=True, autoincrement=True)
    InvoiceNumber = Column(String(50), unique=True, nullable=False)
    InvoiceType = Column(String(20), nullable=False)  # Alis, Satis
    InvoiceDate = Column(Date, nullable=False)
    CurrentAccountID = Column(Integer, ForeignKey('CurrentAccounts.CurrentAccountID'), nullable=False)
    SubTotal = Column(Numeric(18, 2), default=0)
    VATAmount = Column(Numeric(18, 2), default=0)
    DiscountAmount = Column(Numeric(18, 2), default=0)
    TotalAmount = Column(Numeric(18, 2), default=0)
    PaidAmount = Column(Numeric(18, 2), default=0)
    RemainingAmount = Column(Numeric(18, 2), default=0)
    DueDate = Column(Date)
    PaymentTerm = Column(String(100))
    Notes = Column(String(500))
    IsPosted = Column(Boolean, default=False)
    PostedDate = Column(DateTime)
    JournalEntryID = Column(Integer, ForeignKey('JournalEntries.JournalEntryID'))
    CreatedDate = Column(DateTime, default=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    current_account = relationship("CurrentAccount", back_populates="invoices")
    journal_entry = relationship("JournalEntry")
    creator = relationship("User")
    details = relationship("InvoiceDetail", back_populates="invoice", cascade="all, delete-orphan")

class InvoiceDetail(Base):
    __tablename__ = 'InvoiceDetails'
    
    InvoiceDetailID = Column(Integer, primary_key=True, autoincrement=True)
    InvoiceID = Column(Integer, ForeignKey('Invoices.InvoiceID'), nullable=False)
    LineNumber = Column(Integer, nullable=False)
    StockID = Column(Integer, ForeignKey('StockItems.StockID'))
    Description = Column(String(200), nullable=False)
    Quantity = Column(Numeric(18, 2), nullable=False)
    Unit = Column(String(20))
    UnitPrice = Column(Numeric(18, 4), nullable=False)
    DiscountRate = Column(Numeric(5, 2), default=0)
    DiscountAmount = Column(Numeric(18, 2), default=0)
    NetAmount = Column(Numeric(18, 2), nullable=False)
    VATRate = Column(Numeric(5, 2), default=18.00)
    VATAmount = Column(Numeric(18, 2), default=0)
    TotalAmount = Column(Numeric(18, 2), nullable=False)
    
    # Relationships
    invoice = relationship("Invoice", back_populates="details")
    stock_item = relationship("StockItem", back_populates="invoice_details")

class StockMovement(Base):
    __tablename__ = 'StockMovements'
    
    MovementID = Column(Integer, primary_key=True, autoincrement=True)
    MovementNumber = Column(String(50), unique=True, nullable=False)
    MovementDate = Column(Date, nullable=False)
    MovementType = Column(String(20), nullable=False)  # Giris, Cikis, Transfer, Sayim
    StockID = Column(Integer, ForeignKey('StockItems.StockID'), nullable=False)
    WarehouseCode = Column(String(20))
    Quantity = Column(Numeric(18, 2), nullable=False)
    UnitPrice = Column(Numeric(18, 4), default=0)
    TotalValue = Column(Numeric(18, 2), default=0)
    CurrentAccountID = Column(Integer, ForeignKey('CurrentAccounts.CurrentAccountID'))
    InvoiceID = Column(Integer, ForeignKey('Invoices.InvoiceID'))
    Description = Column(String(500))
    CreatedDate = Column(DateTime, default=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    stock_item = relationship("StockItem", back_populates="movements")
    current_account = relationship("CurrentAccount")
    invoice = relationship("Invoice")
    creator = relationship("User")

class CashMovement(Base):
    __tablename__ = 'CashMovements'
    
    CashMovementID = Column(Integer, primary_key=True, autoincrement=True)
    MovementNumber = Column(String(50), unique=True, nullable=False)
    MovementDate = Column(Date, nullable=False)
    CashRegisterID = Column(Integer, ForeignKey('CashRegisters.CashRegisterID'), nullable=False)
    MovementType = Column(String(20), nullable=False)  # Giris, Cikis
    Amount = Column(Numeric(18, 2), nullable=False)
    CurrentAccountID = Column(Integer, ForeignKey('CurrentAccounts.CurrentAccountID'))
    Description = Column(String(500))
    DocumentNumber = Column(String(50))
    JournalEntryID = Column(Integer, ForeignKey('JournalEntries.JournalEntryID'))
    CreatedDate = Column(DateTime, default=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    cash_register = relationship("CashRegister", back_populates="movements")
    current_account = relationship("CurrentAccount")
    journal_entry = relationship("JournalEntry")
    creator = relationship("User")

class BankMovement(Base):
    __tablename__ = 'BankMovements'
    
    BankMovementID = Column(Integer, primary_key=True, autoincrement=True)
    MovementNumber = Column(String(50), unique=True, nullable=False)
    MovementDate = Column(Date, nullable=False)
    BankID = Column(Integer, ForeignKey('Banks.BankID'), nullable=False)
    MovementType = Column(String(20), nullable=False)  # Giris, Cikis
    Amount = Column(Numeric(18, 2), nullable=False)
    CurrentAccountID = Column(Integer, ForeignKey('CurrentAccounts.CurrentAccountID'))
    Description = Column(String(500))
    DocumentNumber = Column(String(50))
    JournalEntryID = Column(Integer, ForeignKey('JournalEntries.JournalEntryID'))
    CreatedDate = Column(DateTime, default=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    bank = relationship("Bank", back_populates="movements")
    current_account = relationship("CurrentAccount")
    journal_entry = relationship("JournalEntry")
    creator = relationship("User")

class Employee(Base):
    __tablename__ = 'Employees'
    
    EmployeeID = Column(Integer, primary_key=True, autoincrement=True)
    EmployeeCode = Column(String(20), unique=True, nullable=False)
    FullName = Column(String(100), nullable=False)
    IdentityNumber = Column(String(11), unique=True)
    Department = Column(String(50))
    Position = Column(String(50))
    HireDate = Column(Date)
    Salary = Column(Numeric(18, 2), default=0)
    Phone = Column(String(50))
    Email = Column(String(100))
    Address = Column(String(500))
    IsActive = Column(Boolean, default=True)
    CreatedDate = Column(DateTime, default=func.now())
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    payrolls = relationship("Payroll", back_populates="employee")

class Payroll(Base):
    __tablename__ = 'Payroll'
    
    PayrollID = Column(Integer, primary_key=True, autoincrement=True)
    PayrollNumber = Column(String(50), unique=True, nullable=False)
    EmployeeID = Column(Integer, ForeignKey('Employees.EmployeeID'), nullable=False)
    PayrollMonth = Column(Integer, nullable=False)
    PayrollYear = Column(Integer, nullable=False)
    BasicSalary = Column(Numeric(18, 2), default=0)
    Overtime = Column(Numeric(18, 2), default=0)
    Bonus = Column(Numeric(18, 2), default=0)
    GrossSalary = Column(Numeric(18, 2), default=0)
    SocialSecurityDeduction = Column(Numeric(18, 2), default=0)
    TaxDeduction = Column(Numeric(18, 2), default=0)
    OtherDeductions = Column(Numeric(18, 2), default=0)
    NetSalary = Column(Numeric(18, 2), default=0)
    IsPaid = Column(Boolean, default=False)
    PaidDate = Column(Date)
    JournalEntryID = Column(Integer, ForeignKey('JournalEntries.JournalEntryID'))
    CreatedDate = Column(DateTime, default=func.now())
    CreatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    employee = relationship("Employee", back_populates="payrolls")
    journal_entry = relationship("JournalEntry")
    creator = relationship("User")

class SystemSetting(Base):
    __tablename__ = 'SystemSettings'
    
    SettingID = Column(Integer, primary_key=True, autoincrement=True)
    SettingKey = Column(String(100), unique=True, nullable=False)
    SettingValue = Column(String(500))
    Description = Column(String(200))
    Category = Column(String(50))
    DataType = Column(String(20))  # String, Number, Boolean, Date
    UpdatedDate = Column(DateTime, default=func.now(), onupdate=func.now())
    UpdatedBy = Column(Integer, ForeignKey('Users.UserID'))
    
    # Relationships
    updater = relationship("User")

class ExchangeRate(Base):
    __tablename__ = 'ExchangeRates'
    
    ExchangeRateID = Column(Integer, primary_key=True, autoincrement=True)
    CurrencyCode = Column(String(3), nullable=False)
    Date = Column(Date, nullable=False)
    BuyingRate = Column(Numeric(10, 4), nullable=False)
    SellingRate = Column(Numeric(10, 4), nullable=False)
    CreatedDate = Column(DateTime, default=func.now())

class AuditLog(Base):
    __tablename__ = 'AuditLog'
    
    AuditID = Column(Integer, primary_key=True, autoincrement=True)
    TableName = Column(String(100), nullable=False)
    RecordID = Column(Integer, nullable=False)
    Action = Column(String(20), nullable=False)  # INSERT, UPDATE, DELETE
    OldValues = Column(Text)
    NewValues = Column(Text)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    ActionDate = Column(DateTime, default=func.now())
    IPAddress = Column(String(50))
    
    # Relationships
    user = relationship("User")

# Database session factory
def create_session(engine):
    """Database session oluştur"""
    Session = sessionmaker(bind=engine)
    return Session()

def create_all_tables(engine):
    """Tüm tabloları oluştur"""
    Base.metadata.create_all(engine)
