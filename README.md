# Vituity EDI Interview Project

Welcome to my Vituity EDI Assessment! This project demonstrates my Python programming and data manipulation capabilities. In this project, I have processed patient data and generated modified CSV files, a report, and more.

## Project Structure

The project directory is organized as follows:

-   `assets`: Contains orginal files to copy.
-   `util`: Contains parser function.
-   `runthis.py`: The main Python script for the project.
-   `mynotes.txt`: The project plan.
-   `README.md`: This documentation.

## Requirements

To run this project, you need:

-   Python (version 3.6.9+)
-   Pandas (install via `pip install pandas`)
-   If `assets` directory is not included, `sampledata.csv`, `ADT_sample.txt`, and `Sample ORU.txt` files must be present on your local machine

## Instructions

Follow these steps to run the project:

1. Clone this GitHub repository to your local machine:

    ```
    git clone https://github.com/janjovellanos/vituity.git
    ```

2. Navigate to the project directory:

    ```
    cd vituity
    ```

3. Run the main script, providing the paths to your sampledata.csv, ADT_sample.txt, and Sample ORU.txt files.

    The files to copy are located in the `assets` directory. You can run the script as follows:

    ```
    python runthis.py --input-csv ./assets/sampledata.csv --input-adt ./assets/ADT_sample.txt --input-oru ./assets/Sample\ ORU.txt
    ```

    This implementation of copying the files allows for flexibility in where the user may store the sample files.
    For instance, if the files are located on your Desktop, you may run the script as:

    ```
    python runthis.py --input-csv ~/Desktop/sampledata.csv --input-adt ~/Desktop/ADT_sample.txt --input-oru ~/Desktop/Sample\ ORU.txt
    ```

New files and directories will be generated in the project's root directory:

-   `Archive/Original`: Contains the copied sample data files.
-   `Archive/Modified`: Contains the modified CSV files and billing report.
-   `adt_patients.db`: An SQLite database containing records of all ADT patients.

## Expected Output

Copying Files: The original data files have been copied to the `Archive/Original` directory.

Creating Modified Files: New CSV files, such as `ADT_(TodaysDate)_Modified_file.csv`, `ORU_(TodaysDate)_Modified_file.csv`, and `ORM_(TodaysDate)_Modified_file.csv`, have been generated in the `Archive/Modified` directory and have been filled with appropriate patient data from `sampledata.csv`.

Data Insertion and Manipulation: Patient data has been extracted from the text files and appended to the correct, modified CSV files. Additional columns, for date of service and patient's full name, have been added as requested.

Report: A report file, `state_total_bill.txt`, lists the total bill amount for each state and the sum of the total bill amount is included as a new row.

## Bonus (Database Support)

An SQLite database for all ADT patients has been created as `adt_patients.db`.

Interact with the database by running:

    sqlite3 adt_patients.db

Below is the schema for the `adt_patients` table:

```sql
CREATE TABLE IF NOT EXISTS "adt_patients" (
    "index" INTEGER,
    "#" INTEGER,
    "id" INTEGER,
    "site_id" TEXT,
    "service_location" REAL,
    "message_type" TEXT,
    "message_time" TEXT,
    "message_id" REAL,
    "account_number" TEXT,
    "discharge_disposition" TEXT,
    "financial_class" TEXT,
    "patient_address_1" TEXT,
    "patient_address_2" TEXT,
    "patient_city" TEXT,
    "patient_state" TEXT,
    "patient_zip" TEXT,
    "patient_zip4" TEXT,
    "patient_date_of_birth" TEXT,
    "patient_deceased_date" REAL,
    "patient_sex" TEXT,
    "patient_ssn" REAL,
    "referring_doctor_id" REAL,
    "attending_doctor_id" REAL,
    "patient_ethnicity" TEXT,
    "patient_race" TEXT,
    "patient_language" TEXT,
    "patient_smoking_status" REAL,
    "patient_email_address" TEXT,
    "patient_cell_phone_area_code" REAL,
    "patient_cell_phone_number" REAL,
    "patient_marital_status" TEXT,
    "bill_amount" INTEGER,
    "patient_drivers_license_number" REAL,
    "guarantor_first_name" TEXT,
    "guarantor_last_name" TEXT,
    "guarantor_middle_name" TEXT,
    "guarantor_address_1" TEXT,
    "guarantor_address_2" TEXT,
    "guarantor_city" TEXT,
    "guarantor_state" TEXT,
    "guarantor_zip" TEXT,
    "date_of_service" TEXT,
    "patient_name" TEXT
);

CREATE INDEX "ix_adt_patients_index" ON "adt_patients" ("index");
```
