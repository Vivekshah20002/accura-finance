-- Accura Finance Veritabanı Şeması
-- Muhasebe Programı Ana Tablolar

-- 1. Şirket Bilgileri
CREATE TABLE Companies (
    CompanyID INT IDENTITY(1,1) PRIMARY KEY,
    CompanyName NVARCHAR(200) NOT NULL,
    TaxNumber NVARCHAR(50) UNIQUE NOT NULL,
    TaxOffice NVARCHAR(100),
    Address NVARCHAR(500),
    Phone NVARCHAR(50),
    Email NVARCHAR(100),
    Website NVARCHAR(100),
    LogoPath NVARCHAR(500),
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedDate DATETIME2 DEFAULT GETDATE(),
    IsActive BIT DEFAULT 1
);

-- 2. Kullanıcılar
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Username NVARCHAR(50) UNIQUE NOT NULL,
    PasswordHash NVARCHAR(255) NOT NULL,
    FullName NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100),
    Phone NVARCHAR(50),
    Role NVARCHAR(50) NOT NULL, -- Admin, Muhasebeci, Kullanici
    IsActive BIT DEFAULT 1,
    LastLogin DATETIME2,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 3. Hesap Planı
CREATE TABLE ChartOfAccounts (
    AccountID INT IDENTITY(1,1) PRIMARY KEY,
    AccountCode NVARCHAR(20) UNIQUE NOT NULL,
    AccountName NVARCHAR(200) NOT NULL,
    ParentAccountID INT,
    AccountType NVARCHAR(50) NOT NULL, -- Aktif, Pasif, Gelir, Gider, Özkaynaklar
    AccountGroup NVARCHAR(100),
    IsDetailAccount BIT DEFAULT 0, -- Detay hesap mı?
    CurrencyCode NVARCHAR(3) DEFAULT 'TRY',
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedDate DATETIME2 DEFAULT GETDATE(),
    FOREIGN KEY (ParentAccountID) REFERENCES ChartOfAccounts(AccountID)
);

-- 4. Cari Hesaplar
CREATE TABLE CurrentAccounts (
    CurrentAccountID INT IDENTITY(1,1) PRIMARY KEY,
    CurrentAccountCode NVARCHAR(20) UNIQUE NOT NULL,
    CurrentAccountName NVARCHAR(200) NOT NULL,
    CurrentAccountType NVARCHAR(50) NOT NULL, -- Musteri, Tedarikci, Personel, Diger
    TaxNumber NVARCHAR(50),
    TaxOffice NVARCHAR(100),
    Address NVARCHAR(500),
    City NVARCHAR(50),
    District NVARCHAR(50),
    PostalCode NVARCHAR(10),
    Phone NVARCHAR(50),
    Mobile NVARCHAR(50),
    Email NVARCHAR(100),
    Website NVARCHAR(100),
    ContactPerson NVARCHAR(100),
    PaymentTerm INT DEFAULT 0, -- Ödeme vadesi (gün)
    CreditLimit DECIMAL(18,2) DEFAULT 0,
    RiskLimit DECIMAL(18,2) DEFAULT 0,
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 5. Stok Kategorileri
CREATE TABLE StockCategories (
    CategoryID INT IDENTITY(1,1) PRIMARY KEY,
    CategoryCode NVARCHAR(20) UNIQUE NOT NULL,
    CategoryName NVARCHAR(100) NOT NULL,
    ParentCategoryID INT,
    Description NVARCHAR(500),
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    FOREIGN KEY (ParentCategoryID) REFERENCES StockCategories(CategoryID)
);

-- 6. Stok Kartları
CREATE TABLE StockItems (
    StockID INT IDENTITY(1,1) PRIMARY KEY,
    StockCode NVARCHAR(50) UNIQUE NOT NULL,
    StockName NVARCHAR(200) NOT NULL,
    CategoryID INT,
    Unit NVARCHAR(20) NOT NULL, -- Adet, Kg, Lt, M, vb.
    Barcode NVARCHAR(50),
    Description NVARCHAR(500),
    PurchasePrice DECIMAL(18,4) DEFAULT 0,
    SalePrice DECIMAL(18,4) DEFAULT 0,
    MinStockLevel DECIMAL(18,2) DEFAULT 0,
    MaxStockLevel DECIMAL(18,2) DEFAULT 0,
    CurrentStock DECIMAL(18,2) DEFAULT 0,
    VATRate DECIMAL(5,2) DEFAULT 18.00,
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (CategoryID) REFERENCES StockCategories(CategoryID),
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 7. Kasalar
CREATE TABLE CashRegisters (
    CashRegisterID INT IDENTITY(1,1) PRIMARY KEY,
    CashRegisterCode NVARCHAR(20) UNIQUE NOT NULL,
    CashRegisterName NVARCHAR(100) NOT NULL,
    CurrencyCode NVARCHAR(3) DEFAULT 'TRY',
    OpeningBalance DECIMAL(18,2) DEFAULT 0,
    CurrentBalance DECIMAL(18,2) DEFAULT 0,
    ResponsiblePerson NVARCHAR(100),
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedDate DATETIME2 DEFAULT GETDATE()
);

-- 8. Bankalar
CREATE TABLE Banks (
    BankID INT IDENTITY(1,1) PRIMARY KEY,
    BankCode NVARCHAR(20) UNIQUE NOT NULL,
    BankName NVARCHAR(100) NOT NULL,
    AccountNumber NVARCHAR(50),
    IBAN NVARCHAR(50),
    BranchName NVARCHAR(100),
    BranchCode NVARCHAR(20),
    CurrencyCode NVARCHAR(3) DEFAULT 'TRY',
    OpeningBalance DECIMAL(18,2) DEFAULT 0,
    CurrentBalance DECIMAL(18,2) DEFAULT 0,
    ResponsiblePerson NVARCHAR(100),
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedDate DATETIME2 DEFAULT GETDATE()
);

-- 9. Yevmiye (Muhasebe Fişleri)
CREATE TABLE JournalEntries (
    JournalEntryID INT IDENTITY(1,1) PRIMARY KEY,
    VoucherNumber NVARCHAR(50) UNIQUE NOT NULL,
    VoucherDate DATE NOT NULL,
    Description NVARCHAR(500),
    TotalDebit DECIMAL(18,2) NOT NULL,
    TotalCredit DECIMAL(18,2) NOT NULL,
    IsBalanced BIT DEFAULT 0,
    IsPosted BIT DEFAULT 0,
    PostedDate DATETIME2,
    DocumentType NVARCHAR(50), -- Fatura, Makbuz, Dekont, vb.
    DocumentNumber NVARCHAR(50),
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    ApprovedBy INT,
    ApprovedDate DATETIME2,
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID),
    FOREIGN KEY (ApprovedBy) REFERENCES Users(UserID)
);

-- 10. Yevmiye Detayları
CREATE TABLE JournalEntryDetails (
    JournalDetailID INT IDENTITY(1,1) PRIMARY KEY,
    JournalEntryID INT NOT NULL,
    LineNumber INT NOT NULL,
    AccountID INT NOT NULL,
    CurrentAccountID INT,
    Description NVARCHAR(500),
    DebitAmount DECIMAL(18,2) DEFAULT 0,
    CreditAmount DECIMAL(18,2) DEFAULT 0,
    CurrencyCode NVARCHAR(3) DEFAULT 'TRY',
    ExchangeRate DECIMAL(10,4) DEFAULT 1,
    DebitAmountLocal DECIMAL(18,2) DEFAULT 0,
    CreditAmountLocal DECIMAL(18,2) DEFAULT 0,
    FOREIGN KEY (JournalEntryID) REFERENCES JournalEntries(JournalEntryID) ON DELETE CASCADE,
    FOREIGN KEY (AccountID) REFERENCES ChartOfAccounts(AccountID),
    FOREIGN KEY (CurrentAccountID) REFERENCES CurrentAccounts(CurrentAccountID)
);

-- 11. Faturalar
CREATE TABLE Invoices (
    InvoiceID INT IDENTITY(1,1) PRIMARY KEY,
    InvoiceNumber NVARCHAR(50) UNIQUE NOT NULL,
    InvoiceType NVARCHAR(20) NOT NULL, -- Alis, Satis
    InvoiceDate DATE NOT NULL,
    CurrentAccountID INT NOT NULL,
    SubTotal DECIMAL(18,2) DEFAULT 0,
    VATAmount DECIMAL(18,2) DEFAULT 0,
    DiscountAmount DECIMAL(18,2) DEFAULT 0,
    TotalAmount DECIMAL(18,2) DEFAULT 0,
    PaidAmount DECIMAL(18,2) DEFAULT 0,
    RemainingAmount DECIMAL(18,2) DEFAULT 0,
    DueDate DATE,
    PaymentTerm NVARCHAR(100),
    Notes NVARCHAR(500),
    IsPosted BIT DEFAULT 0,
    PostedDate DATETIME2,
    JournalEntryID INT,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (CurrentAccountID) REFERENCES CurrentAccounts(CurrentAccountID),
    FOREIGN KEY (JournalEntryID) REFERENCES JournalEntries(JournalEntryID),
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 12. Fatura Detayları
CREATE TABLE InvoiceDetails (
    InvoiceDetailID INT IDENTITY(1,1) PRIMARY KEY,
    InvoiceID INT NOT NULL,
    LineNumber INT NOT NULL,
    StockID INT,
    Description NVARCHAR(200) NOT NULL,
    Quantity DECIMAL(18,2) NOT NULL,
    Unit NVARCHAR(20),
    UnitPrice DECIMAL(18,4) NOT NULL,
    DiscountRate DECIMAL(5,2) DEFAULT 0,
    DiscountAmount DECIMAL(18,2) DEFAULT 0,
    NetAmount DECIMAL(18,2) NOT NULL,
    VATRate DECIMAL(5,2) DEFAULT 18.00,
    VATAmount DECIMAL(18,2) DEFAULT 0,
    TotalAmount DECIMAL(18,2) NOT NULL,
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
    FOREIGN KEY (StockID) REFERENCES StockItems(StockID)
);

-- 13. Stok Hareketleri
CREATE TABLE StockMovements (
    MovementID INT IDENTITY(1,1) PRIMARY KEY,
    MovementNumber NVARCHAR(50) UNIQUE NOT NULL,
    MovementDate DATE NOT NULL,
    MovementType NVARCHAR(20) NOT NULL, -- Giris, Cikis, Transfer, Sayim
    StockID INT NOT NULL,
    WarehouseCode NVARCHAR(20),
    Quantity DECIMAL(18,2) NOT NULL,
    UnitPrice DECIMAL(18,4) DEFAULT 0,
    TotalValue DECIMAL(18,2) DEFAULT 0,
    CurrentAccountID INT,
    InvoiceID INT,
    Description NVARCHAR(500),
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (StockID) REFERENCES StockItems(StockID),
    FOREIGN KEY (CurrentAccountID) REFERENCES CurrentAccounts(CurrentAccountID),
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID),
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 14. Kasa Hareketleri
CREATE TABLE CashMovements (
    CashMovementID INT IDENTITY(1,1) PRIMARY KEY,
    MovementNumber NVARCHAR(50) UNIQUE NOT NULL,
    MovementDate DATE NOT NULL,
    CashRegisterID INT NOT NULL,
    MovementType NVARCHAR(20) NOT NULL, -- Giris, Cikis
    Amount DECIMAL(18,2) NOT NULL,
    CurrentAccountID INT,
    Description NVARCHAR(500),
    DocumentNumber NVARCHAR(50),
    JournalEntryID INT,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (CashRegisterID) REFERENCES CashRegisters(CashRegisterID),
    FOREIGN KEY (CurrentAccountID) REFERENCES CurrentAccounts(CurrentAccountID),
    FOREIGN KEY (JournalEntryID) REFERENCES JournalEntries(JournalEntryID),
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 15. Banka Hareketleri
CREATE TABLE BankMovements (
    BankMovementID INT IDENTITY(1,1) PRIMARY KEY,
    MovementNumber NVARCHAR(50) UNIQUE NOT NULL,
    MovementDate DATE NOT NULL,
    BankID INT NOT NULL,
    MovementType NVARCHAR(20) NOT NULL, -- Giris, Cikis
    Amount DECIMAL(18,2) NOT NULL,
    CurrentAccountID INT,
    Description NVARCHAR(500),
    DocumentNumber NVARCHAR(50),
    JournalEntryID INT,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (BankID) REFERENCES Banks(BankID),
    FOREIGN KEY (CurrentAccountID) REFERENCES CurrentAccounts(CurrentAccountID),
    FOREIGN KEY (JournalEntryID) REFERENCES JournalEntries(JournalEntryID),
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 16. Personel
CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    EmployeeCode NVARCHAR(20) UNIQUE NOT NULL,
    FullName NVARCHAR(100) NOT NULL,
    IdentityNumber NVARCHAR(11) UNIQUE,
    Department NVARCHAR(50),
    Position NVARCHAR(50),
    HireDate DATE,
    Salary DECIMAL(18,2) DEFAULT 0,
    Phone NVARCHAR(50),
    Email NVARCHAR(100),
    Address NVARCHAR(500),
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedDate DATETIME2 DEFAULT GETDATE()
);

-- 17. Bordro
CREATE TABLE Payroll (
    PayrollID INT IDENTITY(1,1) PRIMARY KEY,
    PayrollNumber NVARCHAR(50) UNIQUE NOT NULL,
    EmployeeID INT NOT NULL,
    PayrollMonth INT NOT NULL,
    PayrollYear INT NOT NULL,
    BasicSalary DECIMAL(18,2) DEFAULT 0,
    Overtime DECIMAL(18,2) DEFAULT 0,
    Bonus DECIMAL(18,2) DEFAULT 0,
    GrossSalary DECIMAL(18,2) DEFAULT 0,
    SocialSecurityDeduction DECIMAL(18,2) DEFAULT 0,
    TaxDeduction DECIMAL(18,2) DEFAULT 0,
    OtherDeductions DECIMAL(18,2) DEFAULT 0,
    NetSalary DECIMAL(18,2) DEFAULT 0,
    IsPaid BIT DEFAULT 0,
    PaidDate DATE,
    JournalEntryID INT,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    CreatedBy INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (JournalEntryID) REFERENCES JournalEntries(JournalEntryID),
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);

-- 18. Sistem Ayarları
CREATE TABLE SystemSettings (
    SettingID INT IDENTITY(1,1) PRIMARY KEY,
    SettingKey NVARCHAR(100) UNIQUE NOT NULL,
    SettingValue NVARCHAR(500),
    Description NVARCHAR(200),
    Category NVARCHAR(50),
    DataType NVARCHAR(20), -- String, Number, Boolean, Date
    UpdatedDate DATETIME2 DEFAULT GETDATE(),
    UpdatedBy INT,
    FOREIGN KEY (UpdatedBy) REFERENCES Users(UserID)
);

-- 19. Döviz Kurları
CREATE TABLE ExchangeRates (
    ExchangeRateID INT IDENTITY(1,1) PRIMARY KEY,
    CurrencyCode NVARCHAR(3) NOT NULL,
    Date DATE NOT NULL,
    BuyingRate DECIMAL(10,4) NOT NULL,
    SellingRate DECIMAL(10,4) NOT NULL,
    CreatedDate DATETIME2 DEFAULT GETDATE(),
    UNIQUE(CurrencyCode, Date)
);

-- 20. Audit Log
CREATE TABLE AuditLog (
    AuditID INT IDENTITY(1,1) PRIMARY KEY,
    TableName NVARCHAR(100) NOT NULL,
    RecordID INT NOT NULL,
    Action NVARCHAR(20) NOT NULL, -- INSERT, UPDATE, DELETE
    OldValues NVARCHAR(MAX),
    NewValues NVARCHAR(MAX),
    UserID INT,
    ActionDate DATETIME2 DEFAULT GETDATE(),
    IPAddress NVARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- İndeksler
CREATE INDEX IX_JournalEntries_VoucherDate ON JournalEntries(VoucherDate);
CREATE INDEX IX_JournalEntries_VoucherNumber ON JournalEntries(VoucherNumber);
CREATE INDEX IX_JournalEntryDetails_AccountID ON JournalEntryDetails(AccountID);
CREATE INDEX IX_JournalEntryDetails_CurrentAccountID ON JournalEntryDetails(CurrentAccountID);
CREATE INDEX IX_Invoices_InvoiceDate ON Invoices(InvoiceDate);
CREATE INDEX IX_Invoices_CurrentAccountID ON Invoices(CurrentAccountID);
CREATE INDEX IX_StockMovements_MovementDate ON StockMovements(MovementDate);
CREATE INDEX IX_StockMovements_StockID ON StockMovements(StockID);
CREATE INDEX IX_CashMovements_MovementDate ON CashMovements(MovementDate);
CREATE INDEX IX_BankMovements_MovementDate ON BankMovements(MovementDate);
CREATE INDEX IX_CurrentAccounts_CurrentAccountCode ON CurrentAccounts(CurrentAccountCode);
CREATE INDEX IX_StockItems_StockCode ON StockItems(StockCode);
CREATE INDEX IX_ChartOfAccounts_AccountCode ON ChartOfAccounts(AccountCode);
