"""
file_path = workspace/ contacts.csv
Variables to Collect: name, age(strictly integer), phone number and track
Validate Inputs (Phone by length, non-empty etc)
handling Errors (reprompt if error)

details = {name, age, phone, track}
allow for multiple participants etc

"""
from pathlib import Path
from participant_pkg.file_ops import load_participants, save_participant
from participant_pkg.helper import get_age, get_phone,get_track,get_name


workspace_path = Path("WORKSPACE_FILES")
workspace_path.mkdir(exist_ok=True)
file_path = workspace_path / 'contacts.csv'
participants = []

while True:
    try:
        name = get_name()
        age = get_age()
        phone_number= get_phone()
        track=get_track()
        participant = {
            "name": name, 
            "age": age, 
            "phone": phone_number, 
            "track": track
             }
        participants.append(participant)

        again = input("Add another participant? (y/n): ").lower()
        if again == "y":
            continue
        break
    except Exception as e:
        print(f"An error occured while processing details {e}")
        break

    
save_participant(file_path, participants)
print(f"Saved: {participant}")


# After loop show all participants
participants = load_participants(file_path)
print(f"\nTotal participants saved: {len(participants)}")
for index, participant in enumerate(participants):
    print(f"No {index+1},: {participant}")
  
