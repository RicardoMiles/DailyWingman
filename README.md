# DailyWingman

Scripts that makes my life easier 

## TOC
1. [Format Vocabulary Bank](#script1)
2. [Word Sheet Helper](#script2)




## 1.1 Format Vocabulary Bank
<a id="script1"></a>
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

## 1.2 Word Sheet Helper
<a id="script2"></a>
### 📚 Overview

Word Sheet Helper is a Python script designed to assist with formatting tables in Microsoft Word documents. Especially tailored for solicitors' document workflows by automatically adjusting table layouts and styles. This tool tackles the problem of incomplete or poorly formatted tables that frequently occur when PDF documents are converted to Word and then processed using machine translation. 

---

### ⚙️ Features

- **Dynamic Row Height Adjustment:** Automatically resizes rows based on text content.

- **Preserves Column Width:** Ensures table structure remains intact while adjusting heights.

- **Batch Processing:** Works on multiple tables within a document.

- **User-Friendly GUI:** Provides a graphical interface for file selection and processing.

---

### 💡 Usage Instructions

Make sure you have installed `python-docx` lib before run this script.

```bash
pip install python-docx
```

Or use the [released version](https://github.com/RicardoMiles/DailyWingman/releases/download/Pre-release/Word_Sheet_Helper_CN.exe).


1️⃣ **Run the Script**

```bash
python Word_Sheet_Helper_CN.py # 中文版
python Word_Sheet_Helper_EN.py # English Version
```

2️⃣ **Select a Word Document**

- Click the "Select File" button.

- Choose a `.docx` file containing tables that need formatting.

3️⃣ **Processing Begins**

- The script will adjust row heights dynamically.

- A loading animation indicates progress.

4️⃣ **Completion Notification**

- Once processing is complete, a message box will confirm success.

- The formatted document is saved as `original_filename_revised.docx`.

✅ **Example Output:**

- **Before:** Text may be cut off due to inadequate row height.

- **After:** All text is fully visible within each row.

---

### 🚫 Known Issues & Limitations

- Works only with `.docx` format.

- Optimized for Windows; may require testing on macOS/Linux.

---

## 👍 **Contributing**

If you'd like to contribute:

1. Fork this repository.

2. Make your changes.

3. Submit a pull request with a detailed description of your changes.

---

## 🌟 **License**

This project is licensed under the MIT License.
