# 🌐 TOPSIS Web Service  
### Part-III: Web Service Implementation of TOPSIS

**Name:** Krit Goyal  
**Roll Number:** 102303032  

This project implements a **web-based service for the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method.  
Users can upload a CSV file, provide weights and impacts, enter their email ID, and receive the **TOPSIS result file via email**.

---

## 📌 Project Objective

To develop a **web service** that:
- Accepts user input through a web interface
- Applies the TOPSIS algorithm on uploaded data
- Sends the result file to the user via **email**

---

## 🛠 Technologies Used

- **Python**
- **Flask** (Web Framework)
- **NumPy & Pandas** (Data Processing)
- **HTML / CSS** (Frontend)
- **SMTP (Gmail)** for sending result via email

---

## 🧮 What is TOPSIS?

TOPSIS is a **Multi-Criteria Decision Making (MCDM)** technique that ranks alternatives based on their distance from:
- **Ideal Best Solution**
- **Ideal Worst Solution**

The alternative closest to the ideal best and farthest from the ideal worst gets the highest rank.

---

## 🌐 Web Application Features

✔ File upload (CSV format)  
✔ User-defined weights and impacts  
✔ Email validation  
✔ Automatic TOPSIS calculation  
✔ Result file sent via email  

---

## 📥 User Inputs

The user must provide:

1. **Input CSV File**
2. **Weights** (comma-separated, e.g. `1,1,1,1`)
3. **Impacts** (`+` for benefit, `-` for cost; comma-separated)
4. **Valid Email ID**

---

## ✅ Validation Rules

- Number of **weights must equal number of impacts**
- Impacts must be **only `+` or `-`**
- Weights and impacts must be **comma-separated**
- Email ID format must be valid
- CSV file must contain numerical criteria

---

## 📤 Output

- A CSV file containing:
  - **TOPSIS Score**
  - **Rank**
- The result file is **sent to the user’s email**

---

## 🖥 How the Website Works (Screenshots)

### 🔹 Home Page – Input Form
Users upload the file and enter required details.

![Home Page](screenshots/details_filled.jpeg)

---

### 🔹 Successful Submission
Confirmation that the file has been processed and email sent.

![Success Message](screenshots/email_sent.png)

---

### 🔹 Result Received via Email
The TOPSIS result file received in the user's inbox.

![Email Result](screenshots/email.png)

📌 *Note:* Place your screenshots inside a folder named `screenshots/` in the GitHub repository.

