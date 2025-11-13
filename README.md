# 🧹 Data Cleaning and Preprocessing – Data Analyst Internship Task 1

## 📄 Project Overview
This project focuses on cleaning and preprocessing raw data as part of a Data Analyst Internship assignment.  
The objective is to transform messy data (with missing values, duplicates, and inconsistent formats) into a clean, structured dataset ready for analysis.

---

## 🎯 Objectives
- Identify and handle **missing values**
- Remove **duplicate records**
- Standardize **text and date formats**
- Correct **data types**
- Rename and organize **column headers**

---

## 🧰 Tools & Technologies
- **Microsoft Excel**
- **Python (Pandas, NumPy)**
- **Jupyter Notebook / VS Code**

---

## ⚙️ Steps Performed

### 1. Data Inspection
- Checked dataset shape, columns, and basic info using `df.info()` and `df.describe()`
- Identified missing and duplicate values

### 2. Data Cleaning
- Removed duplicates using `drop_duplicates()`
- Handled missing values with `fillna()` or `dropna()` depending on context
- Standardized text entries (e.g., gender, country names)
- Converted date columns to a uniform `dd-mm-yyyy` format
- Renamed columns for consistency (lowercase, no spaces)

### 3. Data Type Correction
- Converted numerical and date columns to appropriate data types
- Verified that categorical data is correctly encoded

### 4. Final Output
- Produced a **cleaned dataset** ready for analysis or visualization
- Saved the cleaned file as `cleaned_data.xlsx`

---

## 📊 Deliverables
- ✅ `raw_data.xlsx` (original dataset)
- ✅ `cleaned_data.xlsx` (cleaned version)
- ✅ `clean_data.py`
- ✅ `README.md` (this file)

---

## 📚 Learning Outcomes
By completing this task, I learned to:
- Identify and resolve common data quality issues
- Use Excel and Python for preprocessing
- Prepare datasets for further analysis or modeling

---

## 🧠 Interview Concepts Practiced
- Handling missing values
- Removing duplicates
- Difference between `dropna()` and `fillna()`
- Outlier treatment and importance
- Data standardization
- Handling inconsistent formats
- Data quality checks

---

## 👩‍💻 Author
**Name:** sri lakshaya  
**Internship Role:** Data Analyst Intern  
**Date:** 13 November 2025  
