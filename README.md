$$ File Integrity Checker $$

A lightweight Python tool to detect "unauthorized file modifications" by computing and comparing SHA-256 hash values. Ideal for learning the basics of file integrity, hashing, and monitoring file changes — essential concepts in cybersecurity.

<p align="center">
  <img src="docs/demo.mp4" alt="File Integrity Checker Demo" width="600"/>
</p>

# Features

1)Monitors file integrity using SHA-256 hashing
2)Detects file tampering or unauthorized modifications
3)Simple and fast CLI-based usage


# How It Works

1. You select a target file to monitor.
2. The tool calculates its hash and saves it in a separate `.hash` file.
3. Later, you can verify the file again. If the hash changes, the tool alerts you of tampering.

# Technologies Used

1) Language: Python
2) Libraries: `hashlib`, `json`, `os`, `time`
3) Environment: VS Code, Windows/Linux
4) Version Control: Git + GitHub

# Installation & Usage

bash
git clone https://github.com/yourusername/file_integrity_checker.git
cd file_integrity_checker
python main.py

Follow the menu:

Choose to generate or verify file hash
Enter file path


# Future Enhancements

1)Scheduled/automated file integrity checks
2)Email alerts on hash mismatch
3)GUI with drag & drop


Acknowledgments
Made with ❤️ by Prayag Jariwala
Connect on LinkedIn (https://www.linkedin.com/in/prayag-jariwala-4786b2263/)
Follow on GitHub (https://github.com/PrayagJariwala)
