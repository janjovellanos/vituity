# Vituity EDI Interview Project

Welcome to my Vituity EDI Assessment! This project demonstrates my Python programming and data manipulation capabilities. In this project, I have processed patient data and generated modified CSV files, a report, and more.

## Project Structure

The project directory is organized as follows:

-   `utils`: Contains helper functions.
-   `runthis.py`: The main Python script for the project.
-   `mynotes.txt`: The project plan.
-   `README.md`: This documentation.

## Requirements

To run this project, you need:

-   Python (version 3.6.9+)
-   Pandas (install via `pip install pandas`)
-   `sampledata.csv`, `ADT_sample.txt`, and `Sample ORU.txt` files to be present on your computer

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

    For example, if the files are located on your desktop, run the script as follows:

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

Data Insertion and Manipulation: Patient data has been extracted from the text files and appended to the correct modified CSV files. Additional columns, for date of service and patient's full name, have been added as requested.

Report: A report file, `state_total_bill.txt`, lists the total bill amount for each state and the sum of the total bill amount is included as a new row.

## Bonus (Database Support)

An SQLite database for all ADT patients has been created as `adt_patients.db`.

Interact with the database by running:

    sqlite3 adt_patients.db
