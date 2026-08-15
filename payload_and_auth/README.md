# 🔑 Targeted Security Wordlist Generator (`wordlist_builder.py`)

A modular Python utility designed for penetration testing and credential fuzzing. This tool automates the compilation of targeted custom wordlists by pairing base seed keywords with randomized numeric padding and security suffixes.

---

## 🚀 Key Features

* **Seed Expansion:** Takes root target identifiers (such as brand names or usernames) and applies dynamic pattern variations.
* **Randomized Padding:** Generates 2-digit numerical sequences per payload.
* **Security Suffixes:** Appends common credential symbols and year markers (`!`, `@2026`, `#SEC`, `$123`, `!pass`).
* **Automated Disk Export:** Writes generated payloads line-by-line into an external text file.
* **Command-Line Interface:** Validates arguments and paths using Python's `sys` module.

---

## 💻 Requirements

* Python 3.8+
* Standard libraries: `sys`, `random`

---

## 🛠️ Usage

Run the script from your terminal and provide the target output file name as a command-line argument:

```bash
python3 payload_and_auth/wordlist_builder.py custom_passwords.txt
```

### Safety Guard Rail
If executed without specifying a destination file, the tool halts execution and prints proper CLI usage:

```text
Usage: python3 wordlist_builder.py <output_file.txt>
```

---

## 📊 Sample Execution & Output

### Terminal Output
```text
$ python3 payload_and_auth/wordlist_builder.py custom_passwords.txt
✅ Target wordlist successfully compiled: custom_passwords.txt
```

### Generated Output File (`custom_passwords.txt`)
```text
admin82#SEC
admin49!pass
admin74$123
cypher54$123
cypher49@2026
cypher11!pass
root65@2026
root71$123
root41@2026
vault82@2026
vault35!
vault44#SEC
target_cop29$123
target_cop40@2026
target_cop36!
```

---

## ⚙️ How It Works (Internal Logic)

1. **`create_payload(word)`:** Receives an individual keyword string, fetches a random integer between 10–99, selects a suffix from the list, and returns the formatted payload.
2. **`export_word_list(output_filename, word_list, count_per_word)`:** Opens the destination file in write mode (`"w"`), iterates through each word in `word_list`, invokes `create_payload()` for the specified count, and streams each line directly to disk.
