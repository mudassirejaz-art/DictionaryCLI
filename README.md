# Dictionary CLI 📝

An advanced Python CLI tool to fetch **word meanings, synonyms, and examples** from the Free Dictionary API.

---

## 🚀 Features

* Fetch word definitions and examples
* Supports synonyms & multiple meanings
* CLI arguments for word lookup
* Export results to JSON
* Clean, color-coded console output (using `rich`)
* Error handling for invalid words

---

## 📂 Project Structure

```
DictionaryCLI/
├── src/
│   ├── main.py             # CLI entry point
│   ├── dictionary_api.py   # API calls
│   └── utils.py            # Helpers (display & export)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/mudassirejaz-art/DictionaryCLI.git
cd DictionaryCLI
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage

Lookup a word:

```bash
python src/main.py --word example
```

Export word details to JSON:

```bash
python src/main.py --word example --export example.json
```

---

## 📦 Requirements

* Python 3.8+
* requests
* rich

Install all with:

```bash
pip install -r requirements.txt
```

---

## 📜 License

This project is licensed under the MIT License.
