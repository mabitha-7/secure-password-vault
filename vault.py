import sqlite3
from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    with open("secret.key", "rb") as file:
        return file.read()

# Encrypt the password
def encrypt_password(password, key):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode())

# Decrypt the password
def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password).decode()

# Create the database table
def create_table():
    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add a new credential
def add_credential():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    key = load_key()
    encrypted = encrypt_password(password, key)
    
    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO credentials (website, username, password) VALUES (?, ?, ?)", 
                   (website, username, encrypted))
    conn.commit()
    conn.close()
    print("✅ Credential saved successfully!")

# View all stored credentials
def view_credentials():
    key = load_key()
    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, website, username, password FROM credentials")
    rows = cursor.fetchall()
    conn.close()

    print("\n🔐 Stored Credentials:")
    for row in rows:
        id, website, username, encrypted = row
        decrypted = decrypt_password(encrypted, key)
        print(f"{id}. {website} | {username} | {decrypted}")

# Delete a credential
def delete_credential():
    id_to_delete = input("Enter the ID to delete: ")

    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM credentials WHERE id = ?", (id_to_delete,))
    conn.commit()
    conn.close()
    print(f"🗑️ Credential with ID {id_to_delete} deleted.")

# Menu loop
def main():
    create_table()
    while True:
        print("\n=== Password Vault ===")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Delete Credential")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_credential()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            delete_credential()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
