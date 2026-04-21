# Functional_treat_project4
# 📊 Data Analyzer and Transformer Program

## 📌 Overview

This is a **menu-driven Python program** that allows users to:

* Input and manage a 2D dataset
* Perform data analysis and transformations
* Compute statistics such as minimum, maximum, sum, and average
* Apply filtering and sorting operations
* Calculate factorial using recursion

---

## 🚀 Features

### 1. Input Data

* Accepts user input to create a **2D list (matrix)**

### 2. Display Data Summary

* Displays:

  * Total number of elements
  * Average of dataset
* Uses a **global variable (`dataset_summary`)**

### 3. Calculate Factorial

* Computes factorial using **recursion**

### 4. Filter Data by Threshold

* Filters values greater than a given threshold
* Uses:

  * `lambda`
  * `filter()`

### 5. Sort Data

* Sorts all values in:

  * Ascending order
  * Descending order
* Uses `sorted()` function

### 6. Display Dataset Statistics

* Returns and displays:

  * Minimum value
  * Maximum value
  * Total sum
* Demonstrates:

  * Multiple return values
  * `*args` usage
  * `**kwargs` usage

---

## 🧠 Concepts Used

* Functions and modular programming
* Recursion
* Global variables
* Lambda functions
* `filter()` and `sorted()`
* `*args` and `**kwargs`
* Docstrings (`__doc__`)
* List comprehensions

---

## 📂 Program Structure

* `factorial()` → recursive factorial function
* `data_summary()` → returns min, max, total
* `compute_summary()` → stores dataset summary globally
* `display_args()` → prints values using `*args`
* `display_kwargs()` → prints summary using `**kwargs`
* `filter_data()` → filters dataset using lambda
* `sort_data()` → sorts dataset

---

## 📋 Sample Menu

```
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
```
---

## 👩‍💻 Author

Bhumi Shah

---

## 📄 License

This project is for educational purposes.

