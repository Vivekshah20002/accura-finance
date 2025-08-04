"""
Accura Finance - Yapılandırma Yöneticisi
Sistem ayarları ve yapılandırma yönetimi
"""

import configparser
import os
import json
from datetime import datetime

class ConfigManager:
    def __init__(self):
        self.config_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
            'data', 
            'config.ini'
        )
        self.user_config_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
            'data', 
            'user_config.json'
        )
        
        # Dizini oluştur (yoksa)
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        
        self.config = configparser.ConfigParser()
        self.user_config = {}
        
        self.load_config()
        self.load_user_config()
    
    def load_config(self):
        """Sistem yapılandırmasını yükle"""
        if os.path.exists(self.config_file):
            self.config.read(self.config_file, encoding='utf-8')
        else:
            self.create_default_config()
    
    def create_default_config(self):
        """Varsayılan yapılandırmayı oluştur"""
        # Database Section
        self.config['DATABASE'] = {
            'server': 'PINARIISKO',
            'database': 'AccuraFinanceDB',
            'trusted_connection': 'True',
            'trust_server_certificate': 'True',
            'multiple_active_result_sets': 'True',
            'connection_timeout': '30',
            'command_timeout': '60'
        }
        
        # Application Section
        self.config['APPLICATION'] = {
            'name': 'Accura Finance',
            'version': '1.0.0',
            'theme': 'light',
            'language': 'tr',
            'auto_backup': 'True',
            'backup_interval': '24',
            'max_backup_files': '30'
        }
        
        # Company Section
        self.config['COMPANY'] = {
            'name': 'Örnek Şirket A.Ş.',
            'tax_number': '',
            'tax_office': '',
            'address': '',
            'phone': '',
            'email': '',
            'website': '',
            'logo_path': ''
        }
        
        # Financial Section
        self.config['FINANCIAL'] = {
            'default_currency': 'TRY',
            'decimal_places': '2',
            'thousand_separator': '.',
            'decimal_separator': ',',
            'default_vat_rate': '18.00',
            'fiscal_year_start': '01-01',
            'fiscal_year_end': '31-12'
        }
        
        # Security Section
        self.config['SECURITY'] = {
            'session_timeout': '60',
            'password_min_length': '6',
            'password_complexity': 'False',
            'max_login_attempts': '3',
            'lockout_duration': '15'
        }
        
        # Logging Section
        self.config['LOGGING'] = {
            'level': 'INFO',
            'max_file_size': '10',
            'max_files': '5',
            'log_to_file': 'True',
            'log_to_console': 'True'
        }
        
        # Reports Section
        self.config['REPORTS'] = {
            'default_format': 'PDF',
            'auto_open': 'True',
            'save_path': 'reports',
            'date_format': 'dd.MM.yyyy',
            'include_logo': 'True'
        }
        
        self.save_config()
    
    def load_user_config(self):
        """Kullanıcı ayarlarını yükle"""
        if os.path.exists(self.user_config_file):
            try:
                with open(self.user_config_file, 'r', encoding='utf-8') as f:
                    self.user_config = json.load(f)
            except:
                self.user_config = {}
        else:
            self.create_default_user_config()
    
    def create_default_user_config(self):
        """Varsayılan kullanıcı ayarlarını oluştur"""
        self.user_config = {
            'window_geometry': '1400x900',
            'window_state': 'normal',
            'last_module': 'dashboard',
            'grid_settings': {},
            'recent_files': [],
            'shortcuts': {},
            'preferences': {
                'auto_save': True,
                'confirm_delete': True,
                'show_tooltips': True,
                'remember_filters': True
            }
        }
        self.save_user_config()
    
    def save_config(self):
        """Sistem yapılandırmasını kaydet"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                self.config.write(f)
        except Exception as e:
            print(f"Yapılandırma kaydetme hatası: {e}")
    
    def save_user_config(self):
        """Kullanıcı ayarlarını kaydet"""
        try:
            with open(self.user_config_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Kullanıcı ayarları kaydetme hatası: {e}")
    
    def get(self, section, key, fallback=None):
        """Yapılandırma değeri al"""
        try:
            return self.config.get(section, key, fallback=fallback)
        except:
            return fallback
    
    def getint(self, section, key, fallback=0):
        """Integer yapılandırma değeri al"""
        try:
            return self.config.getint(section, key, fallback=fallback)
        except:
            return fallback
    
    def getfloat(self, section, key, fallback=0.0):
        """Float yapılandırma değeri al"""
        try:
            return self.config.getfloat(section, key, fallback=fallback)
        except:
            return fallback
    
    def getboolean(self, section, key, fallback=False):
        """Boolean yapılandırma değeri al"""
        try:
            return self.config.getboolean(section, key, fallback=fallback)
        except:
            return fallback
    
    def set(self, section, key, value):
        """Yapılandırma değeri ayarla"""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))
        self.save_config()
    
    def get_user_setting(self, key, default=None):
        """Kullanıcı ayarı al"""
        return self.user_config.get(key, default)
    
    def set_user_setting(self, key, value):
        """Kullanıcı ayarı belirle"""
        self.user_config[key] = value
        self.save_user_config()
    
    def get_database_config(self):
        """Veritabanı yapılandırmasını al"""
        return {
            'server': self.get('DATABASE', 'server', 'PINARIISKO'),
            'database': self.get('DATABASE', 'database', 'AccuraFinanceDB'),
            'trusted_connection': self.getboolean('DATABASE', 'trusted_connection', True),
            'trust_server_certificate': self.getboolean('DATABASE', 'trust_server_certificate', True),
            'multiple_active_result_sets': self.getboolean('DATABASE', 'multiple_active_result_sets', True),
            'connection_timeout': self.getint('DATABASE', 'connection_timeout', 30),
            'command_timeout': self.getint('DATABASE', 'command_timeout', 60)
        }
    
    def get_company_config(self):
        """Şirket yapılandırmasını al"""
        return {
            'name': self.get('COMPANY', 'name', ''),
            'tax_number': self.get('COMPANY', 'tax_number', ''),
            'tax_office': self.get('COMPANY', 'tax_office', ''),
            'address': self.get('COMPANY', 'address', ''),
            'phone': self.get('COMPANY', 'phone', ''),
            'email': self.get('COMPANY', 'email', ''),
            'website': self.get('COMPANY', 'website', ''),
            'logo_path': self.get('COMPANY', 'logo_path', '')
        }
    
    def get_financial_config(self):
        """Mali yapılandırmayı al"""
        return {
            'default_currency': self.get('FINANCIAL', 'default_currency', 'TRY'),
            'decimal_places': self.getint('FINANCIAL', 'decimal_places', 2),
            'thousand_separator': self.get('FINANCIAL', 'thousand_separator', '.'),
            'decimal_separator': self.get('FINANCIAL', 'decimal_separator', ','),
            'default_vat_rate': self.getfloat('FINANCIAL', 'default_vat_rate', 18.00),
            'fiscal_year_start': self.get('FINANCIAL', 'fiscal_year_start', '01-01'),
            'fiscal_year_end': self.get('FINANCIAL', 'fiscal_year_end', '31-12')
        }
    
    def add_recent_file(self, file_path):
        """Son kullanılan dosyaya ekle"""
        recent = self.user_config.get('recent_files', [])
        if file_path in recent:
            recent.remove(file_path)
        recent.insert(0, file_path)
        # Son 10 dosyayı sakla
        self.user_config['recent_files'] = recent[:10]
        self.save_user_config()
    
    def get_recent_files(self):
        """Son kullanılan dosyaları al"""
        return self.user_config.get('recent_files', [])
    
    def clear_recent_files(self):
        """Son kullanılan dosyaları temizle"""
        self.user_config['recent_files'] = []
        self.save_user_config()
    
    def export_config(self, file_path):
        """Yapılandırmayı dışa aktar"""
        try:
            export_data = {
                'system_config': dict(self.config),
                'user_config': self.user_config,
                'export_date': datetime.now().isoformat()
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Yapılandırma dışa aktarma hatası: {e}")
            return False
    
    def import_config(self, file_path):
        """Yapılandırmayı içe aktar"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                import_data = json.load(f)
            
            # Sistem yapılandırmasını güncelle
            if 'system_config' in import_data:
                for section_name, section_data in import_data['system_config'].items():
                    if not self.config.has_section(section_name):
                        self.config.add_section(section_name)
                    for key, value in section_data.items():
                        self.config.set(section_name, key, value)
            
            # Kullanıcı yapılandırmasını güncelle
            if 'user_config' in import_data:
                self.user_config.update(import_data['user_config'])
            
            self.save_config()
            self.save_user_config()
            return True
            
        except Exception as e:
            print(f"Yapılandırma içe aktarma hatası: {e}")
            return False
