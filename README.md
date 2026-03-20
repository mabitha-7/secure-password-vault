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
cryptography


👉 Install using:

pip install -r requirements.txt


---

## 📂 Project Structure


secure_password_vault/
│
├── main.py
├── database.db
├── key.key
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

1. User runs the application
2. Menu options are displayed:
   * Add credential
   * View credentials
   * Delete credential
3. When storing data:
   * Password is encrypted using Fernet
4. Data is saved in SQLite database
5. While viewing:
   * Password is decrypted and displayed

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mabitha-7/secure-password-vault.git
cd secure_password_vault
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Project
python main.py
💡 Example Usage

Add credential → Enter website, username, password

View credentials → Displays decrypted data

Delete → Enter ID to remove data

🔒 Security

Passwords are encrypted using Fernet symmetric encryption

No plain-text password storage

Encryption key stored separately

🔮 Future Enhancements

🖥️ GUI-based interface

🔑 Master password authentication

☁️ Cloud backup support

📱 Mobile application

👩‍💻 Author

Mabitha M
B.Tech (AI & ML) Student

📜 License

This project is for educational purposes only.
