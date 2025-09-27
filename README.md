# 📁 Project Structure Checker

Script CLI sederhana berbasis Python untuk menampilkan struktur direktori sebuah project dalam format tree, cocok digunakan di VPS atau environment terminal lainnya.

---

## 🚀 Fitur

- Menampilkan struktur folder dan file dalam format yang rapi
- Melewati file tersembunyi (dotfiles) secara default
- Bisa dijalankan dari direktori mana pun
- Mendukung path kustom sebagai argumen

---

## 📦 Requirements

- Python 3.x

Tidak membutuhkan dependency eksternal tambahan.

---

## 🔧 Instalasi

Clone repositori ini ke server atau lokal kamu:

```bash
git clone https://github.com/Muzakie-ID/Structure-Checker
cd Structure-Checker
python3 check_structure.py [path]
```
## Contoh
```bash
python3 check_structure.py /home/ubuntu/project
```

### Output
```bash
Struktur project di: /home/ubuntu/project

├── LICENSE
├── src
│   ├── README.md
│   ├── main.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_helper.py
│   │   └── test_main.py
│   └── utils
│       ├── __init__.py
│       ├── helper.py
│       └── helper2.py
└── .gitignore
```
