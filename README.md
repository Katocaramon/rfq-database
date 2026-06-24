# 🧩 RFQ Database – Gestione RFQ e Offerte
*(English version below)*

Applicazione **Flask** per la gestione centralizzata delle **RFQ (Request for Quotation)** e delle **Offerte** — pensata per uso aziendale in rete locale (LAN), con database **PostgreSQL**, server **Waitress** e configurazione tramite variabili d'ambiente.

---

## 🚀 Funzionalità principali

- CRUD completo per RFQ e Offerte
- **6 stati RFQ**: attiva, inattiva, vinta, persa, non_gestita (con motivo), obsoleta
- **Revisioni RFQ**: clona una RFQ in una nuova revisione; la precedente diventa automaticamente obsoleta
- **Anno SOP**: campo per l'anno di avvio produttivo, usato per calcolare la pipeline
- **Dashboard con Pipeline Opportunity**: revenue K€ per Anno SOP (attive e vinte separate), filtro per anno di ricezione
- **Filtro anno** su dashboard e lista RFQ: KPI, contatori di stato e tabelle filtrati per anno di ricezione
- **Timestamp** su RFQ e Offerte (inclusi nell'export Excel)
- Upload documenti allegati a RFQ e Offerte
- Esportazione in **Excel** e **PDF**
- Login / logout con `Flask-Login`; codice autorizzativo per eliminazioni
- Server **Waitress** (Windows-compatible, no dipendenze C) sulla porta 8080

---

## 🧱 Architettura

```
rfq-database/
│
├── app.py              # Route Flask principali
├── auth.py             # Blueprint autenticazione (login/logout)
├── db.py               # Engine SQLAlchemy + SessionLocal (pool PostgreSQL)
├── models.py           # Modelli ORM: RFQ, Offerta, Document, User
├── utils.py            # Export Excel/PDF
├── run.py              # Entry point Waitress (produzione)
├── avvia.bat           # Script avvio Windows (attiva venv + lancia run.py)
│
├── static/             # CSS e asset
├── templates/          # Template Jinja2
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── rfq_list.html / rfq_form.html / rfq_detail.html
│   └── offerta_form.html / offerte_list.html / offerte_pdf.html
│
├── uploads/            # File caricati (fuori da static/, non esposti direttamente)
├── requirements.txt
├── .env.example        # Template variabili d'ambiente
└── mockup.html         # Prototipo statico interattivo (demo offline)
```

### Scelte architetturali

| Aspetto | Scelta | Motivazione |
|---|---|---|
| **Database** | PostgreSQL (default) | Concorrenza multi-utente, integrità transazionale, scalabilità |
| **ORM** | SQLAlchemy 2.0 + mapped_column | Type-safe, pool di connessioni integrato |
| **WSGI server** | Waitress | Produzione Windows-compatible, multi-thread, nessun compiler C |
| **Auth** | Flask-Login + hash bcrypt | Session-based, semplice da gestire in LAN |
| **Config** | python-dotenv (.env) | Nessun segreto hardcoded nel codice |
| **Upload** | Cartella `uploads/` esterna a `static/` | I file non sono accessibili senza autenticazione |

---

## ⚙️ Installazione

### Prerequisiti

- Python 3.11+
- PostgreSQL 14+ (oppure SQLite per sviluppo locale)
- Git

---

### 1. Clona il repository

```bash
git clone https://github.com/Katocaramon/rfq-database.git
cd rfq-database
```

### 2. Crea e attiva il virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installa le dipendenze

```bash
pip install -r requirements.txt
```

### 4. Configura le variabili d'ambiente

```bash
cp .env.example .env
```

Modifica `.env` con i tuoi valori:

```ini
# Chiave segreta Flask (genera con: python -c "import secrets; print(secrets.token_hex(32))")
SECRET_KEY=cambia-con-una-chiave-sicura

# PostgreSQL
DATABASE_URL=postgresql://utente:password@localhost:5432/rfq_db

# Cartella upload (percorso assoluto consigliato)
UPLOAD_FOLDER=C:\rfq-database\uploads

# Codice per autorizzare le eliminazioni
DELETE_AUTH_CODE=il-tuo-codice

# Password admin (se non impostata, viene generata casualmente e stampata in console)
ADMIN_PASSWORD=password-sicura

# Server
PORT=8080
THREADS=8
```

> **Nota SQLite (sviluppo):** per usare SQLite invece di PostgreSQL, imposta:
> ```ini
> DATABASE_URL=sqlite:///rfq.db
> ```

### 5. Crea il database PostgreSQL

```sql
-- Esegui come superuser PostgreSQL
CREATE DATABASE rfq_db;
CREATE USER rfq_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE rfq_db TO rfq_user;
```

Le tabelle vengono create automaticamente al primo avvio.

### 6. Avvia il server

**Windows (script automatico):**
```bat
avvia.bat
```

**Manuale (tutti i sistemi):**
```bash
python run.py
```

Apri il browser su 👉 **http://localhost:8080**

Credenziali default: **admin** / (vedi console al primo avvio)

---

### Accesso LAN (Windows)

Per rendere l'app accessibile solo dalla rete aziendale, aggiungi una regola Windows Firewall:

```bat
netsh advfirewall firewall add rule ^
  name="RFQ Database" ^
  dir=in action=allow protocol=TCP localport=8080 ^
  remoteip=192.168.1.0/24
```

Sostituisci `192.168.1.0/24` con il range IP della tua LAN.

---

## 🧰 Stack tecnologico

| Componente | Versione | Ruolo |
|---|---|---|
| **Python** | 3.11+ | Linguaggio principale |
| **Flask** | 3.0.3 | Web framework |
| **SQLAlchemy** | 2.0.35 | ORM + pool connessioni |
| **psycopg2-binary** | 2.9.9 | Driver PostgreSQL |
| **Waitress** | 3.0.0 | WSGI server produzione |
| **Flask-Login** | 0.6.3 | Autenticazione sessioni |
| **Flask-WTF** | 1.2.1 | Protezione CSRF |
| **OpenPyXL / Pandas** | 3.1.5 / 2.2.2 | Export Excel |
| **xhtml2pdf** | 0.2.16 | Generazione PDF |
| **python-dotenv** | 1.0.1 | Configurazione .env |
| **Chart.js** | CDN | Grafici dashboard (doughnut + bar) |

---

## 🧑‍💻 Autore

**Giuseppe Paciolla**  
YAGEO – Film Capacitor Division  
📧 [giuseppe.paciolla@hotmail.com](mailto:giuseppe.paciolla@hotmail.com)  
GitHub: [@Katocaramon](https://github.com/Katocaramon)

---

---

# 🌐 English Version

**RFQ Database** is a **Flask web application** for centralized management of **Requests for Quotation (RFQs)** and **Offers** — designed for corporate LAN use, with a **PostgreSQL** database, **Waitress** WSGI server, and environment-based configuration.

---

## 🚀 Main Features

- Full CRUD for RFQs and Offers
- **6 RFQ states**: active, inactive, won, lost, unmanaged (with reason), obsolete
- **RFQ Revisions**: clone an RFQ into a new revision; the previous one is automatically set to obsolete
- **SOP Year**: start-of-production year field used to compute the opportunity pipeline
- **Dashboard with Pipeline Opportunity**: revenue K€ by SOP Year (active and won pipelines), filterable by reception year
- **Year filter** on dashboard and RFQ list: KPIs, status counts and tables filtered by reception year
- **Timestamps** on RFQs and Offers (included in Excel export)
- Document attachments on RFQs and Offers
- **Excel** and **PDF** export
- Login / logout with `Flask-Login`; authorization code required for deletions
- **Waitress** server (Windows-compatible, no C compiler needed) on port 8080

---

## 🧱 Architecture

```
rfq-database/
│
├── app.py              # Main Flask routes
├── auth.py             # Auth blueprint (login/logout)
├── db.py               # SQLAlchemy engine + SessionLocal (PostgreSQL pool)
├── models.py           # ORM models: RFQ, Offerta, Document, User
├── utils.py            # Excel/PDF export helpers
├── run.py              # Waitress entry point (production)
├── avvia.bat           # Windows startup script (activates venv + runs run.py)
│
├── static/             # CSS and assets
├── templates/          # Jinja2 templates
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── rfq_list.html / rfq_form.html / rfq_detail.html
│   └── offerta_form.html / offerte_list.html / offerte_pdf.html
│
├── uploads/            # Uploaded files (outside static/, not publicly accessible)
├── requirements.txt
├── .env.example        # Environment variable template
└── mockup.html         # Interactive static prototype (offline demo)
```

### Architectural decisions

| Aspect | Choice | Reason |
|---|---|---|
| **Database** | PostgreSQL (default) | Multi-user concurrency, transactional integrity, scalability |
| **ORM** | SQLAlchemy 2.0 + mapped_column | Type-safe, built-in connection pooling |
| **WSGI server** | Waitress | Production-ready on Windows, multi-threaded, no C compiler |
| **Auth** | Flask-Login + bcrypt hashing | Session-based, simple to manage on LAN |
| **Config** | python-dotenv (.env) | No secrets hardcoded in source |
| **Uploads** | `uploads/` folder outside `static/` | Files not accessible without authentication |

---

## ⚙️ Installation

### Prerequisites

- Python 3.11+
- PostgreSQL 14+ (or SQLite for local development)
- Git

---

### 1. Clone the repository

```bash
git clone https://github.com/Katocaramon/rfq-database.git
cd rfq-database
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```ini
# Flask secret key (generate with: python -c "import secrets; print(secrets.token_hex(32))")
SECRET_KEY=change-to-a-secure-key

# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/rfq_db

# Upload folder (absolute path recommended)
UPLOAD_FOLDER=C:\rfq-database\uploads

# Authorization code required to delete records
DELETE_AUTH_CODE=your-code

# Admin password (if not set, a random one is printed to console on first start)
ADMIN_PASSWORD=secure-password

# Server
PORT=8080
THREADS=8
```

> **SQLite (development):** to use SQLite instead of PostgreSQL, set:
> ```ini
> DATABASE_URL=sqlite:///rfq.db
> ```

### 5. Create the PostgreSQL database

```sql
-- Run as PostgreSQL superuser
CREATE DATABASE rfq_db;
CREATE USER rfq_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE rfq_db TO rfq_user;
```

Tables are created automatically on first startup.

### 6. Start the server

**Windows (automatic script):**
```bat
avvia.bat
```

**Manual (all platforms):**
```bash
python run.py
```

Open your browser at 👉 **http://localhost:8080**

Default credentials: **admin** / (see console output on first startup)

---

### LAN access (Windows)

To restrict access to the corporate network only, add a Windows Firewall rule:

```bat
netsh advfirewall firewall add rule ^
  name="RFQ Database" ^
  dir=in action=allow protocol=TCP localport=8080 ^
  remoteip=192.168.1.0/24
```

Replace `192.168.1.0/24` with your LAN IP range.

---

## 🧰 Tech Stack

| Component | Version | Role |
|---|---|---|
| **Python** | 3.11+ | Core language |
| **Flask** | 3.0.3 | Web framework |
| **SQLAlchemy** | 2.0.35 | ORM + connection pooling |
| **psycopg2-binary** | 2.9.9 | PostgreSQL driver |
| **Waitress** | 3.0.0 | Production WSGI server |
| **Flask-Login** | 0.6.3 | Session authentication |
| **Flask-WTF** | 1.2.1 | CSRF protection |
| **OpenPyXL / Pandas** | 3.1.5 / 2.2.2 | Excel export |
| **xhtml2pdf** | 0.2.16 | PDF generation |
| **python-dotenv** | 1.0.1 | .env configuration |
| **Chart.js** | CDN | Dashboard charts (doughnut + bar) |

---

## 🧑‍💻 Author

**Giuseppe Paciolla**  
YAGEO – Film Capacitor Division  
📧 [giuseppe.paciolla@hotmail.com](mailto:giuseppe.paciolla@hotmail.com)  
GitHub: [@Katocaramon](https://github.com/Katocaramon)
