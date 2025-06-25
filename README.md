# 🔗 CLI URL Shortener

A simple, command-line based URL shortener written in Python. This project allows you to generate short codes for long URLs and retrieve them later — all stored locally in a JSON file.

## 📁 File Structure

url-shortener/
├── shortener.py # Core logic (shorten/expand)
├── app.py # CLI interface
├── data.json # Stores URL mappings
├── programexec.png # Image displaying an example case
├── README.md # You're reading it!

---

## 🧠 Why I Built This

As a computer engineering student, I wanted to work on a small, practical project that would help me:

- Improve my Python fundamentals
- Understand how basic URL shortening logic works
- Learn about hashing concepts (generating unique identifiers)
- Gain more confidence in building and structuring CLI tools

This was also a quick way to sharpen my skills while keeping the project small enough to complete in a day and upload to GitHub.

---

## 💡 Features

- Shorten any valid URL into a 6-character alphanumeric code
- Automatically detects and avoids duplicate entries
- Retrieve the original URL from any valid short code
- Saves data in a local `data.json` file
- Lightweight and beginner-friendly

---

## 🚀 How to Run

Make sure you have Python 3 installed, then:

```bash
git clone https://github.com/alialghaib/url-shortener.git
cd url-shortener
python app.py
