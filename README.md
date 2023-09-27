# Vituity EDI Interview Project

Welcome to the Vituity EDI Interview Project! This project demonstrates my Python programming skills and data manipulation capabilities. In this project, I have followed the provided instructions to process patient data and generate modified CSV files, a report, and more.

## Project Structure

The project directory is organized as follows:

-   `Archive/Original`: Contains the original data files.
-   `Archive/Modified`: Stores the modified output files.
-   `utils`: Contains helper functions.
-   `main.py`: The main Python script for the project.
-   `README.md`: This documentation.

## Requirements

To run this project, you need:

-   Python (version 3.6.9+)
-   Pandas (install via `pip install pandas`)

## Instructions

Follow these steps to run the project:

1. Clone this GitHub repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd vituity-edi-interview
    ```

3. Run the main script:

    ```bash
    python runthis.py
    ```

### The modified CSV files, report, and other outputs will be generated in the Archive/Modified directory.

## Project Details

Copying Files: The original data files have been copied to the Archive/Original directory.

Creating Modified Files: New CSV files, such as ADT*(TodaysDate)\_Modified_file.csv and ORU*(TodaysDate)\_Modified_file.csv, have been generated in the Archive/Modified directory.

Data Manipulation: Patient data has been extracted from text files and appended to the appropriate dataframes. Additional columns, such as date_of_service and patient_name, have been added as requested.

Report: A report file, state_total_bill.txt, lists the total bill amount for each state. The sum of the total bill amount is included as a new row.

## Bonus (Database Support)

If you choose to implement the bonus objectives related to database support, please follow the instructions provided in the code.
