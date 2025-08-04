"""
Şifre sorununu düzeltmek için admin kullanıcısının şifresini güncelle
"""
import pyodbc
import hashlib

# Veritabanı bağlantısı
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PINARIISKO;"
    "DATABASE=AccuraFinanceDB;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes"
)

def hash_password(password):
    """Şifreyi SHA256 ile hash'le"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

try:
    print("Veritabanına bağlanıyor...")
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    # Önce mevcut kullanıcıları kontrol et
    print("\nMevcut kullanıcılar:")
    cursor.execute("SELECT UserID, Username, PasswordHash, FullName, Role FROM Users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Kullanıcı: {user[1]}, Hash: {user[2][:20]}..., Ad: {user[3]}, Rol: {user[4]}")
    
    # Admin kullanıcısının şifresini düzelt
    new_password = "admin123"
    hashed_password = hash_password(new_password)
    
    print(f"\nYeni şifre hash'i: {hashed_password}")
    
    # Admin kullanıcısını güncelle veya oluştur
    cursor.execute("SELECT COUNT(*) FROM Users WHERE Username = 'admin'")
    admin_exists = cursor.fetchone()[0]
    
    if admin_exists:
        print("Admin kullanıcısını güncelliyorum...")
        update_query = """
        UPDATE Users 
        SET PasswordHash = ?, FullName = 'Sistem Yöneticisi', Email = 'admin@accura.com', Role = 'Admin'
        WHERE Username = 'admin'
        """
        cursor.execute(update_query, hashed_password)
    else:
        print("Admin kullanıcısını oluşturuyorum...")
        insert_query = """
        INSERT INTO Users (Username, PasswordHash, FullName, Email, Role) 
        VALUES ('admin', ?, 'Sistem Yöneticisi', 'admin@accura.com', 'Admin')
        """
        cursor.execute(insert_query, hashed_password)
    
    conn.commit()
    
    # Güncellenmiş kullanıcıları kontrol et
    print("\nGüncellenmiş kullanıcılar:")
    cursor.execute("SELECT UserID, Username, PasswordHash, FullName, Role FROM Users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Kullanıcı: {user[1]}, Hash: {user[2][:20]}..., Ad: {user[3]}, Rol: {user[4]}")
    
    cursor.close()
    conn.close()
    
    print("\n✅ Şifre başarıyla güncellendi!")
    print("Giriş bilgileri:")
    print("Kullanıcı adı: admin")
    print("Şifre: admin123")
    
except Exception as e:
    print(f"❌ Hata: {e}")

input("\nDevam etmek için Enter tuşuna basın...")
