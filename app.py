from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = "yildiz_holding_master_key_2026"

# ==========================================
# VERİTABANI BAĞLANTISI
# ==========================================
def get_db():
    conn = sqlite3.connect('Yildiz_V3.db')
    conn.row_factory = sqlite3.Row
    return conn

# ==========================================
# GÜVENLİK DUVARI (SADECE MÜDÜR GİREBİLİR)
# ==========================================
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin': 
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# ==========================================
# 1. MÜŞTERİ VİTRİNİ (FRONT-END) ROTALARI
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kurumsal')
def kurumsal():
    return render_template('kurumsal.html')

@app.route('/hizmetler')
def hizmetler():
    return render_template('hizmetler.html')

@app.route('/galeri')
def galeri():
    return render_template('galeri.html')

@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

# Müşteri Siteden Mesaj Gönderdiğinde Çalışır (CRM)
@app.route('/send_message', methods=['POST'])
def send_message():
    db = get_db()
    db.execute('INSERT INTO Messages (gonderen_ad, email, konu, mesaj) VALUES (?,?,?,?)',
               (request.form.get('ad'), request.form.get('email'), request.form.get('konu'), request.form.get('mesaj')))
    db.commit()
    db.close()
    return redirect(url_for('iletisim'))


# ==========================================
# 2. GİRİŞ VE ÇIKIŞ (AUTH)
# ==========================================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        user = db.execute('SELECT * FROM Users WHERE username=? AND password=?', 
                          (request.form.get('username'), request.form.get('password'))).fetchone()
        db.close()
        if user:
            session['user_id'] = user['id']
            session['role'] = user['role']
            session['ad_soyad'] = user['ad_soyad']
            
            # Eğer giren kişi adminse Müdür Paneline, değilse Ana Sayfaya yönlendir
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('index'))
                
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# ==========================================
# 3. YÖNETİCİ PANELİ (ADMIN BACK-OFFICE) ROTALARI
# ==========================================
@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    db = get_db()
    
    # KPI (Özet) Verileri
    kpi = {
        'aktif': db.execute('SELECT COUNT(*) FROM Organizations WHERE durum != "Tamamlandı"').fetchone()[0],
        'ekip': db.execute('SELECT COUNT(*) FROM Users WHERE role="staff"').fetchone()[0],
        'mesaj': db.execute('SELECT COUNT(*) FROM Messages').fetchone()[0]
    }
    
    # Kasa Bilanço Hesaplaması
    income = db.execute('SELECT SUM(miktar) FROM Finance WHERE tur="Gelir"').fetchone()[0] or 0
    expense = db.execute('SELECT SUM(miktar) FROM Finance WHERE tur="Gider"').fetchone()[0] or 0
    
    # Tablo Listeleri
    orgs = db.execute('SELECT * FROM Organizations ORDER BY tarih DESC').fetchall()
    staffs = db.execute('SELECT * FROM Users WHERE role="staff" ORDER BY id DESC').fetchall()
    mesajlar = db.execute('SELECT * FROM Messages ORDER BY tarih DESC').fetchall()
    db.close()
    
    return render_template('admin_panel.html', kpi=kpi, orgs=orgs, staffs=staffs, mesajlar=mesajlar, income_sum=income, expense_sum=expense, kasa_toplam=(income-expense))


@app.route('/admin/add_org', methods=['POST'])
@admin_required
def add_org():
    db = get_db()
    cur = db.execute('INSERT INTO Organizations (tip, musteri_ad, tarih, mekan, kisi_sayisi, butce) VALUES (?,?,?,?,?,?)', 
                     (request.form.get('tip'), request.form.get('musteri_ad'), request.form.get('tarih'), request.form.get('mekan'), request.form.get('kisi_sayisi'), request.form.get('butce')))
    org_id = cur.lastrowid
    
    # Seçilen personelleri bu organizasyona atama döngüsü
    staff_ids = request.form.getlist('staff_ids')
    if staff_ids:
        for sid in staff_ids:
            db.execute('INSERT INTO Assignments (org_id, user_id) VALUES (?,?)', (org_id, sid))
        
    db.commit()
    db.close()
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/add_staff', methods=['POST'])
@admin_required
def add_staff():
    db = get_db()
    db.execute('INSERT INTO Users (username, password, role, ad_soyad, tc_no, telefon, maas, birim) VALUES (?, ?, "staff", ?, ?, ?, ?, ?)',
               (request.form.get('username'), request.form.get('password'), request.form.get('ad_soyad'), request.form.get('tc_no'), request.form.get('telefon'), request.form.get('maas'), request.form.get('birim')))
    db.commit()
    db.close()
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/add_finance', methods=['POST'])
@admin_required
def add_finance():
    db = get_db()
    db.execute('INSERT INTO Finance (tur, aciklama, miktar, islem_tarihi) VALUES (?, ?, ?, DATE("now"))', 
               (request.form.get('tur'), request.form.get('aciklama'), request.form.get('miktar')))
    db.commit()
    db.close()
    return redirect(url_for('admin_dashboard'))


# --- SİLME (DELETE) İŞLEMLERİ ---
@app.route('/admin/delete_message/<int:id>')
@admin_required
def delete_message(id):
    db = get_db()
    db.execute('DELETE FROM Messages WHERE id = ?', (id,))
    db.commit()
    db.close()
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/delete_org/<int:id>')
@admin_required
def delete_org(id):
    db = get_db()
    db.execute('DELETE FROM Organizations WHERE id = ?', (id,))
    db.commit()
    db.close()
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/delete_staff/<int:id>')
@admin_required
def delete_staff(id):
    db = get_db()
    db.execute('DELETE FROM Users WHERE id = ? AND role = "staff"', (id,))
    db.commit()
    db.close()
    return redirect(url_for('admin_dashboard'))


if __name__ == '__main__': 
    # Sistemin ağ üzerinde her cihazdan erişilebilir olması için host ayarı yapıldı
    app.run(debug=True, host='0.0.0.0')