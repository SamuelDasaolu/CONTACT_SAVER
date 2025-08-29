import csv


def beautify_csv(data):
    try:
        with open(data, "r", encoding="utf-8") as f:
            csv_f = csv.reader(f)
        for row in csv_f:
            print('{:<15}  {:<15}  {:<20} {:<25}'.format(*row))
    except FileNotFoundError:
        print(f"Error: The file '{data}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")