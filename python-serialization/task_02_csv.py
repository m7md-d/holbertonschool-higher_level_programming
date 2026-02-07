#!/usr/bin/python3
"""
2. Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Function that takes the csv_filename as its parameter
    and writes the JSON data to data.json.
    """
    try:
        data = []

        with open(csv_filename, "r") as f:
            readed = csv.DictReader(f)

            for i in readed:
                data.append(i)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

        return True

    except FileNotFoundError:
        return False
