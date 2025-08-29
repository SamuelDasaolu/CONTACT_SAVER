import json
import csv
import io


def beautify_json_string(data, data_type ="string"):
    #JSON
    if data_type == "json":
        # if data is string
        if data.strip().startswith("{") or data.strip().startswith("["):
            obj = json.loads(data)
        # if data is file
        else:
            with open(data, "r") as f:
                obj = json.load(f)
        return json.dumps(obj, indent=4)
    
    # RAW STRING
    else:
        return "\n" + data.strip() + "\n"
    

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