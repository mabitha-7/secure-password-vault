# 🔐 Secure Password Vault (Console-Based)

## 📌 Project Overview

The **Secure Password Vault** is a Python-based console application designed to help users securely store and manage their login credentials.

It uses **encryption techniques** to protect sensitive data and ensures that passwords are not stored in plain text.

---

## 🎯 Objectives

* To securely store user credentials
* To prevent unauthorized access to passwords
* To provide simple password management
* To implement encryption for data protection

---

## 🧠 Features

* 🔐 Add new credentials (website, username, password)
* 👀 View stored credentials (decrypted format)
* ❌ Delete credentials by ID
* 🛡️ Secure encryption using Fernet
* 💾 Data stored using SQLite database
* ⚡ Fast and simple console interface

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Database:** SQLite (sqlite3)
* **Libraries:**

  * Cryptography (Fernet)

---

## 📦 Requirements

Install the following dependencies:

```
cryptography
```

👉 Install using:

```
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
SECURE_PASSWORD_VAULT/
│
├── key_generator.py     # Generates encryption key
├── secret.key           # Stores encryption key
├── vault.db             # SQLite database file
├── vault.py             # Main application file
└── .gitignore           # Ignored files
```

---

## ⚙️ How It Works

1. Run the application using Python
2. The system provides options to:

   * Add credentials
   * View credentials
   * Delete credentials
3. When adding data:

   * Password is encrypted using Fernet
4. Data is stored in SQLite database
5. When viewing data:

   * Password is decrypted and displayed

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mabitha-7/secure-password-vault.git
cd SECURE_PASSWORD_VAULT
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Project

```bash
python vault.py
```

---

## 💡 Example Usage

* Add credential → Enter website, username, password
* View credentials → Displays decrypted data
* Delete → Enter ID to remove data

---

## 🔒 Security

* Passwords are encrypted using **Fernet symmetric encryption**
* No plain-text password storage
* Encryption key stored separately

---

## 🔮 Future Enhancements

* 🖥️ GUI-based interface
* 🔑 Master password authentication
* ☁️ Cloud backup support
* 📱 Mobile application

---

## 👩‍💻 Author

**Mabitha M**
B.Tech (AI & ML) Student

---

## 📜 License

This project is for educational purposes only.
