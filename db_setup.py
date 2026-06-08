import sqlite3

def setup_pro_db():
    conn = sqlite3.connect('Yildiz_V3.db')
    cursor = conn.cursor()

    # 1. KULLANICILAR VE DEPARTMANLAR (İK Modülü)
    cursor.execute('DROP TABLE IF EXISTS Users')
    cursor.execute('''
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            ad_soyad TEXT,
            tc_no TEXT,
            telefon TEXT,
            maas REAL DEFAULT 0,
            birim TEXT DEFAULT 'Genel Operasyon',
            durum TEXT DEFAULT 'Aktif'
        )
    ''')

    # 2. OPERASYON VE LOJİSTİK PLANLAMA (Etkinlik Modülü)
    cursor.execute('DROP TABLE IF EXISTS Organizations')
    cursor.execute('''
        CREATE TABLE Organizations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tip TEXT,
            musteri_ad TEXT,
            tarih TEXT,
            mekan TEXT,
            kisi_sayisi INTEGER,
            butce REAL DEFAULT 0,
            durum TEXT DEFAULT 'Hazırlanıyor'
        )
    ''')

    # 3. FİNANS VE KASA (Bilanço Modülü)
    cursor.execute('DROP TABLE IF EXISTS Finance')
    cursor.execute('''
        CREATE TABLE Finance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            islem_tarihi TEXT,
            aciklama TEXT,
            miktar REAL,
            tur TEXT
        )
    ''')

    # 4. CRM İLETİŞİM (Mesaj Modülü)
    cursor.execute('DROP TABLE IF EXISTS Messages')
    cursor.execute('''
        CREATE TABLE Messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gonderen_ad TEXT,
            email TEXT,
            konu TEXT,
            mesaj TEXT,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 5. YENİ MODÜL: LOJİSTİK VE ENVANTER
    cursor.execute('DROP TABLE IF EXISTS Logistics')
    cursor.execute('''
        CREATE TABLE Logistics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kategori TEXT,
            donanim_adi TEXT,
            stok INTEGER,
            lokasyon TEXT,
            durum TEXT DEFAULT 'Depoda'
        )
    ''')

    # VARSAYILAN YÖNETİM KURULU BŞK. HESABI
    cursor.execute("INSERT INTO Users (username, password, role, ad_soyad) VALUES (?, ?, ?, ?)", 
                   ('enes_mudur', '1234', 'admin', 'Enes Furkan Yıldız'))
    
    # SİSTEMİ TEST ETMEK İÇİN ÖRNEK ENVANTERLER
    cursor.execute("INSERT INTO Logistics (kategori, donanim_adi, stok, lokasyon, durum) VALUES (?, ?, ?, ?, ?)", 
                   ('Ağ & Kablolama', 'CAT6 Kablo Makarası (300m)', 3, 'Ana Depo (Raf A-1)', 'Depoda'))
    cursor.execute("INSERT INTO Logistics (kategori, donanim_adi, stok, lokasyon, durum) VALUES (?, ?, ?, ?, ?)", 
                   ('Lojistik Araç', 'Ford Transit (07 YLDZ 01)', 1, 'Kepez Arena', 'Görevde'))

    conn.commit()
    # db_setup.py içine, diğer tablo oluşturma kodlarının altına ekle:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        org_id INTEGER,
        user_id INTEGER,
        durum TEXT DEFAULT 'Görev Bekliyor',
        FOREIGN KEY(org_id) REFERENCES Organizations(id),
        FOREIGN KEY(user_id) REFERENCES Users(id)
    )
''')
    conn.close()
    print("🚀 YILDIZ ERP: Veritabanı ve Lojistik Modülü Kusursuzca Kuruldu!")

if __name__ == "__main__":
    setup_pro_db()