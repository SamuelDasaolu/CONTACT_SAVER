import csv
from pathlib import Path


def save_participant(file_path: Path, participant_dict: list):
    """Update A CSV file with a Participants Details 
    Creates A New File if it doesn't exist
    Creates Header if It Doesn't Exist""" 
    headers = ["name", "age", "phone", "track"]
    try: 
        with open(file_path, "a", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            if not file_path.exists():
                writer.writeheader()
            for dict_row in participant_dict:
                writer.writerow(dict_row)
            print(f"\n Participant {participant_dict} saved successfully")
    except Exception as e:
        print(f"An error occured {e}")


def load_participants(file_path: Path) -> list:
    """This reads all participants from the CSV and 
    returns them as a list of dictionaries."""
    participants = []
    try: 
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                participants.append(row)
    except Exception as e:
        print(f"An error occured {e}")
    
    return participants


workspace_path = Path("workspace_files")
workspace_path.mkdir(exist_ok=True)
file_path = workspace_path / 'contacts.csv'
diction = [{
    'name': 'sadasd sadads',
    'age': 23,
    'phone': '324324 234',
    'track': 'Ai sadads',
}
]
save_participant(file_path, diction)
for n, row in enumerate(load_participants(file_path)):
    print(f"No {n}: {row}")