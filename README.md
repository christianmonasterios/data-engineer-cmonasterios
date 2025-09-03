# Educations:

## 🧩 Overview

This solution focuses on two key aspects that should be addressed **before development begins**:

- ✅ **Scalability**
- 🛠️ **Maintainability**

Each data source requires its own mapping function to format the input data according to the expected schema of the destination table.

---

## 📊 Data Profiling

Proper fields mapping is **critical**. It is strongly recommended to coordinate with **analysts and vendors** to:

- Define what is expected for each field.
- Perform **data profiling**.
- Standardize **date formats**.
- Remove special characters and unnecessary whitespace.

Since each source may come from a different vendor, it is important to clearly understand which fields will be received and their formats **before files are delivered**.

> ⏱️ Time invested at this stage is crucial for long-term success.

---

## 📈 Scalability

The solution can easily scale to support 100+ data sources with **no changes to the core code**.  
To add a new source:

1. Add an entry to `config/datasources.json`.
2. Create a new mapping script: `map_datasource_X.py`.

---

## 📂 Source Files

Files are stored in a repository and may arrive at any time.  
The solution is designed for **batch processing**, ideally run nightly via **Airflow**, to process files received the **previous day**.

### 📌 Implementation Notes

- File names may include dates or be placed in date-specific folders separated by DATE (e.g. in AWS S3).
- The process will scan the previous day’s folder and iterate over any files found there.
- ⚠️ **Note:** This can not be event-driven *(to be discussed)*.

---

## 🎯 Target

For demonstration purposes, the destination is a single table in **SQLite**.

---

## 🚫 Duplicate Handling

The process includes logic to avoid inserting duplicates, using the combination of `PHONE` and `ADDRESS` fields as a deduplication key.

---

## ⚙️ Performance

The expected data volume is low and no specific performance constraints were provided.  
Thus, using **Python + pandas** is appropriate.

For larger files, data can be processed in **chunks**. In cloud environments like AWS, this logic could be implemented on:

- AWS Lambda
- AWS Batch

> At this stage, the use of PySpark (e.g., Glue or Databricks) is not necessary.

---

## ✅ TODO / Improvements

Future iterations should improve the following areas:

1. **Validation with Analysts**: Confirm mappings and transformations with business stakeholders.
2. **Key Field Normalization**: For example, strip parentheses from `PHONE` to avoid **join** issues.
3. **Date Format Standardization**: Dates must follow a consistent format (not yet implemented).
4. **Global Whitespace Cleanup**: Many fields need trimming due to messy source files.
5. **Robust Error Handling**: Add retry logic and failure handling.(Nothing implemented in this iteration)

---

## 📦 Summary

This pipeline is designed to be simple, flexible, and ready for scale.  
It emphasizes correctness, clarity, and maintainability from the start — especially for teams that must integrate data from multiple vendors with inconsistent formats.

