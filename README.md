# CV-Booster AI (Pembuat Poin Deskripsi CV Otomatis)

Aplikasi berbasis Python yang memanfaatkan **Google Gemini API** untuk mengubah kalimat biasa atau informal pada pengalaman kerja CV menjadi kalimat deskripsi yang profesional, dan berbobot.

---

## Tampilan Aplikasi
Program ini berjalan langsung melalui layar terminal / Command Prompt dengan proses yang cepat dan sederhana.

---

## Fitur Utama
- **Generasi Teks Otomatis:** Mengubah kalimat sederhana menjadi poin deskripsi CV yang menggunakan *action verbs* (kata kerja aksi).
- **Proses Cepat:** Menggunakan model AI terbaru dari Google (`gemini-3.8-flash`).
- **Antarmuka Sederhana:** Mudah dijalankan di laptop tanpa perlu tampilan web yang rumit.

---

## Tools & Teknologi
- **Bahasa Pemrograman:** Python 3.x
- **SDK AI:** `google-generativeai`
- **Model AI:** Google Gemini API (`models/gemini-3.8-flash`)
- **Version Control:** Git & GitHub

---

## Cara Menjalankan Aplikasi di Laptop

Ikuti langkah-langkah mudah berikut untuk menjalankan aplikasi ini di komputer/laptop :

### 1. Unduh / Clone Repository Ini
Buka terminal / Command Prompt, lalu jalankan perintah:
```bash
git clone [https://github.com/ardiladhea/cv-booster-ai.git](https://github.com/ardiladhea/cv-booster-ai.git)
cd cv-booster-ai
```

### 2. Install Library yang Dibutuhkan
Install SDK resmi dari Google Generative AI dengan perintah:
```bash
pip install google-generativeai
```

### 3. Masukkan Google Gemini API Key
- Buka file app.py menggunakan teks editor (seperti VS Code).
- Cari baris API_KEY dan masukkan kode API Key milik Anda sendiri:
```python
API_KEY = "MASUKKAN_API_KEY_KAMU_DI_SINI"
```

### 4. Jalankan Project
Ketik perintah berikut di terminal untuk memulai project:
```bash
python app.py
```
---
Dibuat oleh Dhea Ardila sebagai portofolio pengembangan aplikasi berbasis AI.




