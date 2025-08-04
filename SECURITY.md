# 🔒 Security Policy

## 🛡️ Desteklenen Sürümler

Aşağıdaki sürümler güvenlik güncellemeleri almaktadır:

| Sürüm | Destekleniyor |
| ------- | ------------------ |
| 1.0.x   | ✅ |
| < 1.0   | ❌ |

## 🚨 Güvenlik Açığı Bildirimi

Accura Finance'da bir güvenlik açığı keşfederseniz, lütfen bu bilgileri sorumlu bir şekilde bildirin.

### 📧 İletişim

**Güvenlik açıklarını bildirmek için:**
- Email: piinartp@gmail.com
- Konu: [SECURITY] Accura Finance Güvenlik Açığı

### 📋 Bildiri Süreci

1. **Özel Bildirim**: Güvenlik açıklarını public issue olarak açmayın
2. **Detaylı Açıklama**: Açığın nasıl yeniden oluşturulacağını açıklayın
3. **Etki Analizi**: Açığın potansiyel etkisini belirtin
4. **Öneriler**: Varsa çözüm önerilerinizi paylaşın

### 🔍 Bildirmeniz Gereken Bilgiler

- Açığın türü (SQL injection, XSS, authentication bypass, vb.)
- Etkilenen bileşenler
- Yeniden oluşturma adımları
- Potansiyel etki
- Önerilen çözüm (varsa)

### ⏱️ Yanıt Süresi

- **İlk Yanıt**: 48 saat içinde
- **Durum Güncellemesi**: 7 gün içinde
- **Çözüm Süresi**: Açığın ciddiyetine bağlı olarak

### 🏆 Güvenlik Araştırmacıları

Güvenlik açığı bildiren araştırmacılar:
- CHANGELOG.md'de teşekkür edilecek
- GitHub contributors listesine eklenecek
- LinkedIn endorsement alabilecek

### 🔐 Güvenlik İyi Uygulamaları

**Kullanıcılar için:**
- Güçlü şifreler kullanın
- Düzenli olarak güncellemeleri takip edin
- Veritabanı bağlantılarını güvenli tutun
- Hassas verileri yedekleyin

**Geliştiriciler için:**
- SQL injection'a karşı parameterized queries kullanın
- Input validation uygulayın
- Authentication/authorization kontrolleri yapın
- Sensitive data'yı loglamayın

### 📊 Güvenlik Kontrolü

Proje düzenli olarak aşağıdaki araçlarla taranmaktadır:
- Bandit (Python security linting)
- Safety (dependency vulnerability checking)
- CodeQL (semantic code analysis)

### 🔄 Güncelleme Politikası

- **Kritik Güvenlik Açıkları**: 24-48 saat içinde patch
- **Yüksek Öncelikli**: 1 hafta içinde
- **Orta Öncelikli**: 1 ay içinde
- **Düşük Öncelikli**: Bir sonraki minor release'te

## 📞 İletişim

Güvenlik ile ilgili sorularınız için:
- Email: piinartp@gmail.com
- GitHub: @ThecoderPinar

---

**Teşekkürler!** Accura Finance'ı güvenli tutmaya yardımcı olduğunuz için teşekkür ederiz. 🙏
