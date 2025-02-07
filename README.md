# DailyWingman

Scripts that makes my life easier 

## Format Vocabulary Bank

### 📚 **Overview**

**Format Vocabulary Bank** is a Python script designed to format vocabulary entries efficiently. It accepts multi-line user input from the command line and applies consistent formatting to text, specifically:

- Adding missing spaces after `=` signs.

- Highlighting key terms before `=` using `**bold**` markdown styling.

- Supporting seamless multi-line input termination with `Ctrl+Z + Enter` on Windows.

---

### ⚙️ **Features**

- **Automatic Formatting:** Adds missing spaces after `=` and applies bold formatting.

- **EOF Handling:** Correctly processes input using `Ctrl+Z + Enter` without the need for double confirmation.

- **Real-Time Input Capture:** Uses the Windows-specific `msvcrt` module for efficient, low-level input handling.

- **Output Saving:** Automatically saves formatted output to `formatted_output.txt`.

---

### 💡 **Usage Instructions**

#### 1️⃣ **Run the Script**

```bash
python Format_Vocabulary_Bank.py
```

#### 2️⃣ **Input Your Vocabulary Data**

Paste or type your vocabulary entries:

```markdown
A tad = a little bit
Natter = a casual & informal & leisurely convo
Chinwag = chat / have a chat
```

#### 3️⃣ **End Input**

- **For Windows:** Press `Ctrl+Z` then `Enter` to finish the input.

- **For Linux/macOS:** Press `Ctrl+D` to finish the input.

#### 4️⃣ **View the Formatted Output**

The script will:

- Display the formatted output in the terminal.

- Save the output to `formatted_output.txt` for easy access.

#### ✅ **Example Output:**

```markdown
**A tad** = a little bit
**Natter** = a casual & informal & leisurely convo
**Chinwag** = chat / have a chat
```

---

### 🛠️ **Customization**

- **Change Output File Name:** Modify the file-saving section in the script to rename `formatted_output.txt`.

- **Adjust Formatting Style:** Change the bold formatting (`**{text}**`) to other markdown styles if needed.

---

### 📊 **Sample Input & Output**

#### **Input:**

```
Banter = playful conversationTrait=unique characteristic
```

#### **Output:**

```
**Banter** = playful conversation**Trait** = unique characteristic
```

---

### 🚫 **Known Issues & Limitations**

- Currently optimized for **Windows** only due to `msvcrt` dependency.

- May require slight adjustments for Linux/macOS compatibility.

---

## 👍 **Contributing**

If you'd like to contribute:

1. Fork this repository.

2. Make your changes.

3. Submit a pull request with a detailed description of your changes.

---

## 🌟 **License**

This project is licensed under the MIT License.
