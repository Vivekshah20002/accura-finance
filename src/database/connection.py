"""
Accura Finance - Veritabanı Bağlantı Yöneticisi
SQL Server bağlantısı ve veritabanı işlemleri
"""

import pyodbc
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
import sys
import os

class DatabaseManager:
    def __init__(self):
        # SQL Server bağlantı bilgileri
        self.server = "PINARIISKO"
        self.database = "AccuraFinanceDB"
        self.trusted_connection = True
        self.trust_server_certificate = True
        self.multiple_active_result_sets = True
        
        # Bağlantı string'i
        self.connection_string = self._build_connection_string()
        self.engine = None
        self.setup_logging()
        
    def setup_logging(self):
        """Logging yapılandırması"""
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(os.path.join(log_dir, 'database.log')),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _build_connection_string(self):
        """SQL Server bağlantı string'ini oluştur"""
        return (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"Trusted_Connection={'yes' if self.trusted_connection else 'no'};"
            f"TrustServerCertificate={'yes' if self.trust_server_certificate else 'no'};"
            f"MultipleActiveResultSets={'true' if self.multiple_active_result_sets else 'false'};"
        )
    
    def create_engine(self):
        """SQLAlchemy engine oluştur"""
        try:
            connection_url = f"mssql+pyodbc:///?odbc_connect={self.connection_string}"
            self.engine = create_engine(
                connection_url,
                pool_size=10,
                max_overflow=20,
                pool_pre_ping=True,
                pool_recycle=3600
            )
            self.logger.info("Veritabanı engine başarıyla oluşturuldu")
            return True
        except Exception as e:
            self.logger.error(f"Engine oluşturma hatası: {e}")
            return False
    
    def test_connection(self):
        """Veritabanı bağlantısını test et"""
        try:
            conn = pyodbc.connect(self.connection_string, timeout=10)
            conn.close()
            self.logger.info("Veritabanı bağlantısı başarılı")
            return True
        except pyodbc.Error as e:
            self.logger.error(f"Veritabanı bağlantı hatası: {e}")
            return False
    
    def create_database_if_not_exists(self):
        """Veritabanını oluştur (yoksa)"""
        try:
            # Master veritabanına bağlan
            master_conn_string = self.connection_string.replace(
                f"DATABASE={self.database};", "DATABASE=master;"
            )
            
            conn = pyodbc.connect(master_conn_string)
            cursor = conn.cursor()
            
            # Veritabanının var olup olmadığını kontrol et
            cursor.execute(
                "SELECT name FROM sys.databases WHERE name = ?", 
                (self.database,)
            )
            
            if not cursor.fetchone():
                # Veritabanını oluştur
                cursor.execute(f"CREATE DATABASE [{self.database}]")
                conn.commit()
                self.logger.info(f"Veritabanı '{self.database}' oluşturuldu")
            else:
                self.logger.info(f"Veritabanı '{self.database}' zaten mevcut")
            
            cursor.close()
            conn.close()
            return True
            
        except pyodbc.Error as e:
            self.logger.error(f"Veritabanı oluşturma hatası: {e}")
            return False
    
    @contextmanager
    def get_connection(self):
        """Context manager ile güvenli bağlantı"""
        conn = None
        try:
            conn = pyodbc.connect(self.connection_string)
            yield conn
        except pyodbc.Error as e:
            self.logger.error(f"Bağlantı hatası: {e}")
            if conn:
                conn.rollback()
            raise
        finally:
            if conn:
                conn.close()
    
    def execute_query(self, query, params=None, fetch=True):
        """SQL sorgu çalıştır"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                if fetch:
                    if query.strip().upper().startswith('SELECT'):
                        columns = [column[0] for column in cursor.description]
                        rows = cursor.fetchall()
                        return [dict(zip(columns, row)) for row in rows]
                    else:
                        return cursor.fetchall()
                else:
                    conn.commit()
                    return cursor.rowcount
                    
        except pyodbc.Error as e:
            self.logger.error(f"Sorgu çalıştırma hatası: {e}")
            raise
    
    def execute_script(self, script_path):
        """SQL script dosyasını çalıştır"""
        try:
            with open(script_path, 'r', encoding='utf-8') as file:
                script = file.read()
            
            # Script'i noktalı virgülle ayır ve çalıştır
            statements = script.split(';')
            
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                for statement in statements:
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)
                
                conn.commit()
                self.logger.info(f"Script başarıyla çalıştırıldı: {script_path}")
                return True
                
        except Exception as e:
            self.logger.error(f"Script çalıştırma hatası: {e}")
            return False
    
    def get_table_info(self, table_name):
        """Tablo bilgilerini getir"""
        query = """
        SELECT 
            COLUMN_NAME,
            DATA_TYPE,
            IS_NULLABLE,
            COLUMN_DEFAULT,
            CHARACTER_MAXIMUM_LENGTH
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = ?
        ORDER BY ORDINAL_POSITION
        """
        return self.execute_query(query, (table_name,))
    
    def backup_database(self, backup_path):
        """Veritabanını yedekle"""
        try:
            query = f"BACKUP DATABASE [{self.database}] TO DISK = ?"
            self.execute_query(query, (backup_path,), fetch=False)
            self.logger.info(f"Veritabanı yedeklendi: {backup_path}")
            return True
        except Exception as e:
            self.logger.error(f"Yedekleme hatası: {e}")
            return False
    
    def restore_database(self, backup_path):
        """Veritabanını geri yükle"""
        try:
            # Önce veritabanını single user moduna al
            query1 = f"ALTER DATABASE [{self.database}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE"
            query2 = f"RESTORE DATABASE [{self.database}] FROM DISK = ?"
            query3 = f"ALTER DATABASE [{self.database}] SET MULTI_USER"
            
            self.execute_query(query1, fetch=False)
            self.execute_query(query2, (backup_path,), fetch=False)
            self.execute_query(query3, fetch=False)
            
            self.logger.info(f"Veritabanı geri yüklendi: {backup_path}")
            return True
        except Exception as e:
            self.logger.error(f"Geri yükleme hatası: {e}")
            return False

# Singleton pattern
_db_manager = None

def get_database_manager():
    """Veritabanı yöneticisi singleton instance"""
    global _db_manager
    if _db_manager is None:
        _db_manager = DatabaseManager()
    return _db_manager
