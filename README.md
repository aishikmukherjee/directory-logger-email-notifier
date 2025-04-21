# 📂 Directory Traversal Logger & Email Notifier

This Python script automates the scanning of a directory and generates a detailed log of all files and folders. It then emails the log file to a user-specified address and moves the log to the system's trash to keep your workspace clean.

## 🚀 Features

- Recursively scans folders and subfolders
- Generates a structured log file with system metadata
- Sends the log as an email attachment using Gmail (via yagmail)
- Moves the log file to system trash after sending (using send2trash)
- Auto-installs required modules if not found

## 🛠 Technologies Used

- `Python`
- `yagmail` – for sending emails
- `send2trash` – for safe file deletion
- `os`, `getpass`, `socket`, `datetime` – for system interaction

## 📦 Setup & Usage

1. **Clone the repo**
    ```bash
    git clone https://github.com/your-username/repo-name.git
    cd repo-name
    ```

2. **Run the script**
    ```bash
    python main.py
    ```

3. **Follow the prompts** to:
   - Enter the directory path you want to scan
   - Provide the recipient's email

4. The log will be emailed and then moved to trash.

## ⚠️ Requirements

- Python 3.6+
- Gmail with "App Passwords" enabled if using 2FA
- Internet connection (to send the email)

## 🧠 Author

**Aishik Mukherjee**  
[LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)

---

*Feel free to fork, star, or contribute!*

