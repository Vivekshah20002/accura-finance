-- Accura Finance Başlangıç Verileri
-- İlk kullanım için gerekli veriler

-- 1. Varsayılan Şirket Bilgisi
INSERT INTO Companies (CompanyName, TaxNumber, TaxOffice, Address, Phone, Email)
VALUES ('Örnek Şirket A.Ş.', '1234567890', 'Ankara Vergi Dairesi', 'Çankaya/ANKARA', '0312-123-45-67', 'info@ornek.com');

-- 2. Varsayılan Admin Kullanıcısı (şifre: admin123)
INSERT INTO Users (Username, PasswordHash, FullName, Email, Role)
VALUES ('admin', 'sha256$salt$hash', 'Sistem Yöneticisi', 'admin@accura.com', 'Admin');

-- 3. Ana Hesap Grupları
INSERT INTO ChartOfAccounts (AccountCode, AccountName, ParentAccountID, AccountType, AccountGroup) VALUES
('1', 'DÖNEN VARLIKLAR', NULL, 'Aktif', 'Ana Grup'),
('10', 'HAZIR DEĞERLER', 1, 'Aktif', 'Grup'),
('100', 'KASA', 10, 'Aktif', 'Grup'),
('101', 'ALINAN ÇEKLER', 10, 'Aktif', 'Grup'),
('102', 'BANKALAR', 10, 'Aktif', 'Grup'),
('108', 'DİĞER HAZIR DEĞERLER', 10, 'Aktif', 'Grup'),

('12', 'TİCARİ ALACAKLAR', 1, 'Aktif', 'Grup'),
('120', 'ALICILAR', 12, 'Aktif', 'Grup'),
('121', 'ALACAK SENETLERİ', 12, 'Aktif', 'Grup'),
('122', 'ALACAK SENETLERİ REESKONTU', 12, 'Aktif', 'Grup'),
('126', 'VERİLEN DEPOZİTO VE TEMİNATLAR', 12, 'Aktif', 'Grup'),
('128', 'ŞÜPHELİ TİCARİ ALACAKLAR', 12, 'Aktif', 'Grup'),
('129', 'ŞÜPHELİ TİCARİ ALACAKLAR KARŞILIĞI', 12, 'Aktif', 'Grup'),

('15', 'STOKLAR', 1, 'Aktif', 'Grup'),
('150', 'İLK MADDE VE MALZEME', 15, 'Aktif', 'Grup'),
('151', 'YARI MAMULLER', 15, 'Aktif', 'Grup'),
('152', 'MAMULLER', 15, 'Aktif', 'Grup'),
('153', 'TİCARİ MALLAR', 15, 'Aktif', 'Grup'),
('157', 'DİĞER STOKLAR', 15, 'Aktif', 'Grup'),
('158', 'STOK DEĞER DÜŞÜKLÜĞÜ KARŞILIĞI', 15, 'Aktif', 'Grup'),

('18', 'GELECEK AYLARA AİT GİDERLER VE GELİR TAHAKKUKLARI', 1, 'Aktif', 'Grup'),
('180', 'GELECEK AYLARA AİT GİDERLER', 18, 'Aktif', 'Grup'),
('181', 'GELİR TAHAKKUKLARI', 18, 'Aktif', 'Grup'),

('19', 'DİĞER DÖNEN VARLIKLAR', 1, 'Aktif', 'Grup'),
('190', 'VERİLEN AVANSLAR', 19, 'Aktif', 'Grup'),
('191', 'PERSONELE VERİLEN AVANSLAR', 19, 'Aktif', 'Grup'),
('192', 'DİĞER ÇEŞİTLİ ALACAKLAR', 19, 'Aktif', 'Grup'),
('193', 'PERSONELE BORÇLAR', 19, 'Aktif', 'Grup'),
('195', 'PEŞIN ÖDENEN VERGİLER VE FONLAR', 19, 'Aktif', 'Grup'),
('196', 'DİĞER KDV', 19, 'Aktif', 'Grup'),

-- DURAN VARLIKLAR
('2', 'DURAN VARLIKLAR', NULL, 'Aktif', 'Ana Grup'),
('22', 'MADDİ DURAN VARLIKLAR', 2, 'Aktif', 'Grup'),
('220', 'ARAZİ VE ARSALAR', 22, 'Aktif', 'Grup'),
('221', 'YER ALTI VE YER ÜSTÜ DÜZENLERİ', 22, 'Aktif', 'Grup'),
('222', 'BİNALAR', 22, 'Aktif', 'Grup'),
('223', 'TESİS MAKİNE VE CİHAZLAR', 22, 'Aktif', 'Grup'),
('224', 'TAŞITLAR', 22, 'Aktif', 'Grup'),
('225', 'DEMİRBAŞLAR', 22, 'Aktif', 'Grup'),
('226', 'DİĞER MADDİ DURAN VARLIKLAR', 22, 'Aktif', 'Grup'),
('227', 'BİRİKMİŞ AMORTİSMANLAR', 22, 'Aktif', 'Grup'),
('228', 'MADDİ DURAN VARLIK DEĞER DÜŞÜKLÜĞÜ KARŞILIĞI', 22, 'Aktif', 'Grup'),

-- KISA VADELİ YABANCI KAYNAKLAR
('3', 'KISA VADELİ YABANCI KAYNAKLAR', NULL, 'Pasif', 'Ana Grup'),
('30', 'MALİ BORÇLAR', 3, 'Pasif', 'Grup'),
('300', 'BANKA KREDİLERİ', 30, 'Pasif', 'Grup'),
('301', 'FINANSAL KİRALAMA İŞLEMLERİNDEN BORÇLAR', 30, 'Pasif', 'Grup'),
('302', 'ERTELENEN FİNANSMAN GİDERLERİ', 30, 'Pasif', 'Grup'),
('303', 'UZUN VADELİ KREDİLERİN ANAPARA TAKSIT VE FAİZLERİ', 30, 'Pasif', 'Grup'),

('32', 'TİCARİ BORÇLAR', 3, 'Pasif', 'Grup'),
('320', 'SATICILAR', 32, 'Pasif', 'Grup'),
('321', 'BORÇ SENETLERİ', 32, 'Pasif', 'Grup'),
('322', 'BORÇ SENETLERİ REESKONTU', 32, 'Pasif', 'Grup'),
('326', 'ALINAN DEPOZİTO VE TEMİNATLAR', 32, 'Pasif', 'Grup'),

('33', 'DİĞER BORÇLAR', 3, 'Pasif', 'Grup'),
('330', 'ORTAKLARA BORÇLAR', 33, 'Pasif', 'Grup'),
('331', 'PERSONELE BORÇLAR', 33, 'Pasif', 'Grup'),
('332', 'DİĞER ÇEŞİTLİ BORÇLAR', 33, 'Pasif', 'Grup'),
('335', 'ORTAKLARDAN ALACAKLAR', 33, 'Pasif', 'Grup'),
('336', 'PERSONELDEN ALACAKLAR', 33, 'Pasif', 'Grup'),

('36', 'ALINAN AVANSLAR', 3, 'Pasif', 'Grup'),
('360', 'MÜŞTERİLERDEN ALINAN AVANSLAR', 36, 'Pasif', 'Grup'),
('361', 'VERİLEN SİPARİŞLER İÇİN ALINAN AVANSLAR', 36, 'Pasif', 'Grup'),

('37', 'YILSONU GİDER TAHAKKUKLARI', 3, 'Pasif', 'Grup'),
('370', 'DÖNEM SONU GİDER TAHAKKUKLARI', 37, 'Pasif', 'Grup'),

('38', 'BORÇ VE GİDER KARŞILIKLARI', 3, 'Pasif', 'Grup'),
('380', 'KISA VADELİ BORÇ KARŞILIKLARI', 38, 'Pasif', 'Grup'),

('39', 'GELİR TAHAKKUKLARI', 3, 'Pasif', 'Grup'),
('391', 'GELECEKKİ YILLARA AİT GELİRLER', 39, 'Pasif', 'Grup'),

-- GELİRLER
('6', 'GELİRLER', NULL, 'Gelir', 'Ana Grup'),
('60', 'BRÜT SATIŞ GELİRLERİ', 6, 'Gelir', 'Grup'),
('600', 'YURTİÇİ SATIŞLAR', 60, 'Gelir', 'Grup'),
('601', 'YURTDIŞI SATIŞLAR', 60, 'Gelir', 'Grup'),
('602', 'DİĞER GELİRLER', 60, 'Gelir', 'Grup'),

('61', 'SATIŞ İNDİRİMLERİ', 6, 'Gelir', 'Grup'),
('610', 'SATIŞTAN İADELER', 61, 'Gelir', 'Grup'),
('611', 'SATIŞ İSKONTOLARI', 61, 'Gelir', 'Grup'),
('612', 'DİĞER İNDİRİMLER', 61, 'Gelir', 'Grup'),

-- GİDERLER
('7', 'GİDERLER', NULL, 'Gider', 'Ana Grup'),
('70', 'MAL VE HİZMET ALIM GİDERLERİ', 7, 'Gider', 'Grup'),
('700', 'YURTİÇİ ALIŞLAR', 70, 'Gider', 'Grup'),
('701', 'YURTDIŞI ALIŞLAR', 70, 'Gider', 'Grup'),
('702', 'ALIŞ İADELERİ', 70, 'Gider', 'Grup'),
('703', 'ALIŞ İSKONTOLARI', 70, 'Gider', 'Grup'),

('75', 'DİĞER FAALİYET GİDERLERİ', 7, 'Gider', 'Grup'),
('750', 'ARAŞTIRMA VE GELİŞTİRME GİDERLERİ', 75, 'Gider', 'Grup'),
('751', 'DİĞER ÇEŞİTLİ GİDERLER', 75, 'Gider', 'Grup'),

('76', 'PERSONEL GİDERLERİ', 7, 'Gider', 'Grup'),
('760', 'PERSONEL ÜCRET VE GİDERLERİ', 76, 'Gider', 'Grup'),
('761', 'DIŞARIDAN SAĞLANAN FAYDA VE HİZMETLER', 76, 'Gider', 'Grup'),

('77', 'GENEL YÖNETİM GİDERLERİ', 7, 'Gider', 'Grup'),
('770', 'GENEL YÖNETİM GİDERLERİ', 77, 'Gider', 'Grup'),

('78', 'FİNANSMAN GİDERLERİ', 7, 'Gider', 'Grup'),
('780', 'FİNANSMAN GİDERLERİ', 78, 'Gider', 'Grup');

-- 4. Stok Kategorileri
INSERT INTO StockCategories (CategoryCode, CategoryName, Description) VALUES
('01', 'Hammadde', 'Üretimde kullanılan hammaddeler'),
('02', 'Yarı Mamul', 'Üretim sürecindeki yarı mamuller'),
('03', 'Mamul', 'Tamamlanmış ürünler'),
('04', 'Ticari Mal', 'Alım-satım yapılan ticari mallar'),
('05', 'Yardımcı Malzeme', 'Üretimde yardımcı olarak kullanılan malzemeler'),
('06', 'Ambalaj Malzemesi', 'Ambalajlama için kullanılan malzemeler'),
('07', 'Ofis Malzemeleri', 'Büro ve ofis malzemeleri'),
('08', 'Temizlik Malzemeleri', 'Temizlik ve hijyen malzemeleri'),
('09', 'Diğer', 'Diğer çeşitli malzemeler');

-- 5. Varsayılan Kasa
INSERT INTO CashRegisters (CashRegisterCode, CashRegisterName, CurrencyCode, OpeningBalance, CurrentBalance, ResponsiblePerson) VALUES
('KASA01', 'Ana Kasa TL', 'TRY', 0, 0, 'Muhasebe'),
('KASA02', 'Döviz Kasası USD', 'USD', 0, 0, 'Muhasebe'),
('KASA03', 'Döviz Kasası EUR', 'EUR', 0, 0, 'Muhasebe');

-- 6. Sistem Ayarları
INSERT INTO SystemSettings (SettingKey, SettingValue, Description, Category, DataType) VALUES
('CompanyName', 'Accura Finance', 'Şirket Adı', 'Company', 'String'),
('VATRate', '18.00', 'Varsayılan KDV Oranı', 'Tax', 'Number'),
('CurrencyCode', 'TRY', 'Ana Para Birimi', 'Currency', 'String'),
('FiscalYearStart', '01-01', 'Mali Yıl Başlangıcı', 'Fiscal', 'String'),
('FiscalYearEnd', '31-12', 'Mali Yıl Sonu', 'Fiscal', 'String'),
('AutoBackup', 'true', 'Otomatik Yedekleme', 'Backup', 'Boolean'),
('BackupInterval', '24', 'Yedekleme Aralığı (Saat)', 'Backup', 'Number'),
('MaxBackupFiles', '30', 'Maksimum Yedek Dosya Sayısı', 'Backup', 'Number'),
('InvoicePrefix', 'F', 'Fatura Numarası Öneki', 'Invoice', 'String'),
('VoucherPrefix', 'M', 'Muhasebe Fişi Öneki', 'Voucher', 'String'),
('StockCodePrefix', 'S', 'Stok Kodu Öneki', 'Stock', 'String'),
('CurrentAccountPrefix', 'C', 'Cari Hesap Kodu Öneki', 'Account', 'String'),
('DateFormat', 'dd.MM.yyyy', 'Tarih Formatı', 'Display', 'String'),
('DecimalPlaces', '2', 'Ondalık Basamak Sayısı', 'Display', 'Number'),
('ThousandSeparator', '.', 'Binlik Ayracı', 'Display', 'String'),
('DecimalSeparator', ',', 'Ondalık Ayracı', 'Display', 'String');

-- 7. Döviz Kurları (Örnek)
INSERT INTO ExchangeRates (CurrencyCode, Date, BuyingRate, SellingRate) VALUES
('USD', CAST(GETDATE() AS DATE), 27.50, 27.80),
('EUR', CAST(GETDATE() AS DATE), 30.20, 30.50),
('GBP', CAST(GETDATE() AS DATE), 35.10, 35.40);

-- 8. Bazı Detay Hesaplar
INSERT INTO ChartOfAccounts (AccountCode, AccountName, ParentAccountID, AccountType, AccountGroup, IsDetailAccount) VALUES
('100.01', 'TL Kasası', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '100'), 'Aktif', 'Detay', 1),
('102.01', 'Ziraat Bankası TL', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '102'), 'Aktif', 'Detay', 1),
('102.02', 'İş Bankası TL', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '102'), 'Aktif', 'Detay', 1),
('120.01', 'Müşteri Alacakları', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '120'), 'Aktif', 'Detay', 1),
('153.01', 'Ticari Mallar', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '153'), 'Aktif', 'Detay', 1),
('320.01', 'Tedarikçi Borçları', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '320'), 'Pasif', 'Detay', 1),
('600.01', 'Yurtiçi Satışlar', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '600'), 'Gelir', 'Detay', 1),
('700.01', 'Yurtiçi Alışlar', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '700'), 'Gider', 'Detay', 1),
('760.01', 'Personel Maaşları', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '760'), 'Gider', 'Detay', 1),
('770.01', 'Kira Giderleri', (SELECT AccountID FROM ChartOfAccounts WHERE AccountCode = '770'), 'Gider', 'Detay', 1);

-- Başlangıç için örnek stok kartları
INSERT INTO StockItems (StockCode, StockName, CategoryID, Unit, PurchasePrice, SalePrice, VATRate, CreatedBy) VALUES
('S001', 'Örnek Ürün 1', 1, 'Adet', 100.00, 150.00, 18.00, 1),
('S002', 'Örnek Ürün 2', 1, 'Kg', 50.00, 75.00, 18.00, 1),
('S003', 'Örnek Hizmet', 2, 'Saat', 200.00, 300.00, 18.00, 1);

-- Örnek cari hesaplar
INSERT INTO CurrentAccounts (CurrentAccountCode, CurrentAccountName, CurrentAccountType, TaxNumber, Phone, Email, CreatedBy) VALUES
('C001', 'ABC Ticaret Ltd. Şti.', 'Musteri', '1111111111', '0212-123-45-67', 'abc@ticaret.com', 1),
('C002', 'XYZ Tedarik A.Ş.', 'Tedarikci', '2222222222', '0312-987-65-43', 'xyz@tedarik.com', 1),
('C003', 'Ahmet Yılmaz', 'Personel', '3333333333', '0532-111-22-33', 'ahmet@example.com', 1);

PRINT 'Başlangıç verileri başarıyla eklendi.';
