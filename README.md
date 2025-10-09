# 🧩 RFQ Database – Gestione RFQ e Offerte  
*(English version below)*

Applicazione **Flask** per la gestione centralizzata delle **RFQ (Request for Quotation)** e delle **Offerte**.  
Consente la creazione, visualizzazione, modifica ed esportazione delle offerte in formato **Excel** e **PDF**, con gestione utenti e autenticazione sicura.  

---

## 🚀 Funzionalità principali

- CRUD completo (creazione, lettura, modifica, cancellazione) per RFQ e Offerte  
- Login / logout utenti con `flask-login`  
- Esportazione offerte in formato **Excel** e **PDF**  
- Template HTML responsive basati su **Bootstrap 5**  
- Ricerca e filtri per cliente, progetto e data  
- Struttura modulare e facilmente estendibile

---

## 🧱 Struttura del progetto

```
rfq_offerte_app/
│
├── app.py                 # Entry point Flask principale
├── auth.py                # Gestione autenticazione
├── db.py                  # Connessione SQLAlchemy
├── models.py              # Modelli RFQ, Offerta, User, Document
├── utils.py               # Funzioni di supporto (Excel, PDF, date parsing)
│
├── static/                # CSS, JS e template Excel
│   ├── css/app.css
│   ├── js/xlsx.full.min.js
│   └── templates/offerta_template_bosch.xlsx
│
├── templates/             # Template HTML Jinja2
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── rfq_list.html / rfq_form.html / rfq_detail.html
│   ├── offerte_list.html / offerta_form.html / offerte_pdf.html
│   └── view_excel*.html
│
├── requirements.txt       # Dipendenze Python
└── rfq.db                 # Database SQLite locale
```

---

## ⚙️ Installazione locale

### 1️⃣ Clona il repository
```bash
git clone https://github.com/Katocaramon/rfq-database.git
cd rfq-database
```

### 2️⃣ Crea e attiva un ambiente virtuale
```bash
python3 -m venv .venv
source .venv/bin/activate   # su Mac/Linux
# oppure .venv\Scripts\activate su Windows
```

### 3️⃣ Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4️⃣ Avvia l’app Flask
```bash
flask run
```

Apri il browser su 👉 **http://127.0.0.1:5000**

---

## 🧰 Stack Tecnologico

| Componente | Descrizione |
|-------------|-------------|
| **Python 3.12+** | Linguaggio principale |
| **Flask** | Web framework |
| **SQLAlchemy** | ORM per il database |
| **Flask-Login** | Gestione autenticazione utenti |
| **OpenPyXL / Pandas** | Esportazione in Excel |
| **WeasyPrint / ReportLab** | Generazione PDF |
| **Bootstrap 5** | UI responsive |

---

## 🗂️ Versionamento

Repository GitHub:  
👉 [https://github.com/Katocaramon/rfq-database](https://github.com/Katocaramon/rfq-database)

Branch principale: `main`  
Usare branch dedicati (es. `feature/export-pdf`) per nuove funzioni.

---

## 🧑‍💻 Autore

**Giuseppe Paciolla**  
YAGEO – Film Capacitor Division  
📧 [giuseppe.paciolla@hotmail.com](mailto:giuseppe.paciolla@hotmail.com)  
GitHub: [@Katocaramon](https://github.com/Katocaramon)

---

# 🌐 English Version

**RFQ Database** is a **Flask web application** designed to manage **Requests for Quotation (RFQs)** and **Offers** in an organized and efficient way.  
It provides a full CRUD system with user authentication, data filtering, and export capabilities in **Excel** and **PDF** formats.

---

## 🚀 Main Features

- Full CRUD for RFQs and Offers  
- User login/logout with `flask-login`  
- Export offers to **Excel** and **PDF**  
- Responsive HTML templates (Bootstrap 5)  
- Search and filtering by customer, project, or date  
- Modular and easily extensible architecture

---

## 🧱 Project Structure

```
rfq_offerte_app/
│
├── app.py                 # Flask main entry point
├── auth.py                # Authentication logic
├── db.py                  # SQLAlchemy connection and session
├── models.py              # Data models: RFQ, Offer, User, Document
├── utils.py               # Utility functions (Excel, PDF, date parsing)
│
├── static/                # CSS, JS, Excel templates
│   ├── css/app.css
│   ├── js/xlsx.full.min.js
│   └── templates/offerta_template_bosch.xlsx
│
├── templates/             # HTML Jinja2 templates
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── rfq_list.html / rfq_form.html / rfq_detail.html
│   ├── offerte_list.html / offerta_form.html / offerte_pdf.html
│   └── view_excel*.html
│
├── requirements.txt       # Python dependencies
└── rfq.db                 # Local SQLite database
```

---

## ⚙️ Local Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Katocaramon/rfq-database.git
cd rfq-database
```

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # on macOS/Linux
# or .venv\Scripts\activate on Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app
```bash
flask run
```

Then open your browser at 👉 **http://127.0.0.1:5000**

---

## 🧰 Tech Stack

| Component | Description |
|------------|-------------|
| **Python 3.12+** | Core language |
| **Flask** | Web framework |
| **SQLAlchemy** | Database ORM |
| **Flask-Login** | Authentication management |
| **OpenPyXL / Pandas** | Excel export |
| **WeasyPrint / ReportLab** | PDF generation |
| **Bootstrap 5** | Responsive UI |

---

## 🗂️ Versioning

GitHub Repository:  
👉 [https://github.com/Katocaramon/rfq-database](https://github.com/Katocaramon/rfq-database)

Main branch: `main`  
Use feature branches for development (e.g., `feature/export-pdf`).

---

## 🧑‍💻 Author

**Giuseppe Paciolla**  
YAGEO – Film Capacitor Division  
📧 [giuseppe.paciolla@hotmail.com](mailto:giuseppe.paciolla@hotmail.com)  
GitHub: [@Katocaramon](https://github.com/Katocaramon)
