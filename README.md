# Vituity EDI Interview Project

Welcome to my Vituity EDI Assessment! This project demonstrates my Python programming and data manipulation capabilities. In this project, I have followed the provided instructions to process patient data and generate modified CSV files, a report, and more.

## Project Structure

The project directory is organized as follows:

-   `Archive/Original`: Contains the original data files.
-   `Archive/Modified`: Stores the modified output files.
-   `utils`: Contains helper functions.
-   `runthis.py`: The main Python script for the project.
-   `mynotes.txt`: The project plan for the assessment.
-   `README.md`: This documentation.

## Requirements

To run this project, you need:

-   `sampledata.csv`, `ADT_sample.txt`, and `Sample ORU.txt` files must be present on your computer
-   Python (version 3.6.9+)
-   Pandas (install via `pip install pandas`)
-   SQLite3 (included with Python)

## Instructions

Follow these steps to run the project:

1. Clone this GitHub repository to your local machine:

    ```
    git clone https://github.com/janjovellanos/vituity.git
    ```

2. Navigate to the project directory:

    ```
    cd vituity-main
    ```

3. Run the main script, providing the paths to your sampledata.csv, ADT_sample.txt, and Sample ORU.txt files.

    For example, if the files are located on your desktop run the script as follows:

    ```
    python runthis.py --input-csv ~/Desktop/sampledata.csv --input-adt ~/Desktop/ADT_sample.txt --input-oru ~/Desktop/Sample\ ORU.txt
    ```

The sample files will be copied into the `Archive/Original` directory and the modified CSV files, report, and other outputs will be generated in the `Archive/Modified` directory.

## Expected Output

Copying Files: The original data files have been copied to the `Archive/Original` directory.

Creating Modified Files: New CSV files, such as `ADT_(TodaysDate)_Modified_file.csv`, `ORU_(TodaysDate)_Modified_file.csv`, and `ORM_(TodaysDate)_Modified_file.csv`, have been generated in the `Archive/Modified` directory and have been filled with appropriate patient data from `sampledata.csv`.

Data Insertion and Manipulation: Patient data has been extracted from text files and appended to the correct datasets. Additional columns, such as date_of_service and patient_name, have been added as requested.

Report: A report file, state_total_bill.txt, lists the total bill amount for each state. The sum of the total bill amount is included as a new row.

## Bonus (Database Support)

A SQLite database for all ADT patients has been created as `adt_patients.db`.

Interact with the database by running:

    sqlite3 adt_patients.db
