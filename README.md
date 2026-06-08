<div align="center">

# ⭐ YILDIZ ORGANİZASYON  ⭐
### Premium Etkinlik ve Operasyon Yönetim Sistemi

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

**Operasyonel Süreçlerin Dijitalleştiği, Güvenli ve Ölçeklenebilir Bilişim Altyapısı**

</div>

---

## 📌 Yönetici Özeti (Executive Summary)
Yıldız Organizasyon V2; karmaşık etkinlik operasyonlarını, personel yönetimini ve müşteri verilerini tek bir merkezden kontrol etmek amacıyla geliştirilmiş **dinamik bir bilişim sistemi projesidir.** 

Bu proje sadece bir web arayüzü değil; arka planda güçlü bir veritabanı mimarisi barındıran, veri bütünlüğünü sağlayan ve yöneticilere kusursuz bir operasyon paneli sunan tam teşekküllü bir **Yönetim Bilişim Sistemi (MIS)** çözümüdür. Sıradanlığı reddeden vizyonumuzla, hem kod kalitesini hem de kullanıcı deneyimini en üst düzeyde tutuyoruz.

---

## 🚀 Ne Yaptık? (Sistem Mimarisi ve Özellikler)

Sistemin temelini sağlam bir altyapı üzerine inşa ettik:

*   🛡️ **Rol Tabanlı Güvenlik (Role-Based Access):** Yetkisiz erişimleri engelleyen, sadece sistem yöneticilerinin (Admin) girebildiği şifreli yönetim paneli.
*   ⚙️ **Dinamik Veri Yönetimi (CRUD Operasyonları):** Etkinliklerin ve personel kadrosunun veritabanı üzerinden anlık olarak eklenmesi, listelenmesi ve güvenli bir şekilde (deletion validation) sistemden kaldırılması.
*   🗄️ **İlişkisel Veritabanı Mimarisi:** SQLite entegrasyonu ile veri kaybını önleyen, optimize edilmiş tablo yapıları.
*   🎨 **Premium Kullanıcı Deneyimi (UX):** Bootstrap 5 ve özel CSS animasyonlarıyla donatılmış, "Splash Screen" (Açılış Şovu) içeren, tüm cihazlarla tam uyumlu (Responsive) vitrin tasarımı.

---

## 🔮 Ne Yapacağız? (Sistem Yol Haritası)

Projenin bir sonraki fazında, sistem yönetimini ve donanım/sunucu takibini daha da profesyonelleştirecek adımlar planlanmaktadır:

- [ ] **Sistem Loglama (Logging):** Yöneticilerin sistemdeki tüm hareketlerini (kim, ne zaman, hangi veriyi sildi/ekledi) takip eden güvenlik kayıt modülü.
- [ ] **Sunucu İzleme Paneli (Server Monitoring):** Sistemin çalıştığı sunucunun anlık durumunu, kaynak tüketimini panel üzerinden görüntüleme.
- [ ] **Otomatik Veritabanı Yedekleme:** Olası bir veri kaybına karşı SQLite veritabanının belirli periyotlarla otomatik yedeklenmesi (Automated Backup).
- [ ] **Donanım Entegrasyonu Altyapısı:** İlerleyen süreçte sahada kullanılacak operasyon cihazlarının (barkod okuyucular, giriş terminalleri) sisteme entegre edilebilmesi için API altyapısı hazırlığı.

---

## 🛠️ Teknik Altyapı ve Dizilim (Tech Stack)

<table>
  <tr>
    <th>Kategori</th>
    <th>Teknolojiler</th>
  </tr>
  <tr>
    <td><b>Backend (Sunucu Mimarisi)</b></td>
    <td>Python, Flask Microframework</td>
  </tr>
  <tr>
    <td><b>Database (Veri Yönetimi)</b></td>
    <td>SQLite 3, SQL Query Language</td>
  </tr>
  <tr>
    <td><b>Frontend (Kullanıcı Arayüzü)</b></td>
    <td>HTML5, CSS3, Bootstrap 5, Jinja2 Template Engine</td>
  </tr>
</table>

---

## ⚙️ Kurulum ve Çalıştırma (Sistem Yöneticileri İçin)

Projeyi yerel sunucunuzda (localhost) test etmek için terminal/CMD üzerinden aşağıdaki adımları izleyin:

```bash
# 1. Sistemi Bilgisayarınıza Klonlayın
git clone https://github.com/enesfurkanyildiz/Yildiz_Organizasyon_V2.git

# 2. Proje Dizinine Geçiş Yapın
cd Yildiz_Organizasyon_V2

# 3. Gerekli Python Modüllerini Yükleyin
pip install flask

# 4. Veritabanı Şemalarını Ayağa Kaldırın
python db_setup.py

# 5. Sunucuyu Başlatın
python app.py
