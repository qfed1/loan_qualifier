# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(user_path, qualifying_loans):
    """Saves data as .csv file to a user defined file path
    Args:
        user_path (string): user defined file path where the .csv file is saved
        qualifying_loans (list of lists): The qualifying bank loans.
    """

    with open(user_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        #define header based on primary bank data file and then write header row to csv first
        header = ["Lender", "Max Loan Amount" ,"Max LTV" ,"Max DTI", "Min Credit Score", "Interest Rate"]
        csvwriter.writerow(header)

        # Then we can write the data rows
        for loan in qualifying_loans:
            csvwriter.writerow(loan)