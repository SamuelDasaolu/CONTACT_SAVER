


from pathlib import Path
# from participant_pkg.file_ops import save_participant, load_participants
# from participant_pkg import helper
# csv_path = Path("contacts.csv")



while True:
    try:
        name = input("Enter participant name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")

        age = int(input("Enter age: "))
        if age <=0:
            raise ValueError("Age must be greater than 0")
        phone = input("Enter phone number: ").strip()
        if len(phone) != 11:
            raise ValueError("Phone number too short")

        track = input("Enter track: ").strip()
        if not track:
            raise ValueError("Track cannot be empty")

        participant = {"Name": name, "Age": age, "Phone": phone, "Track": track}
        save_participant(csv_path, participant)
        print(f"Saved: {participant}")

    except ValueError as e:
        print(f"Invalid input: {e}")
        continue

    again = input("Add another participant? (y/n): ").lower()
    if again != "y":
        break

# After loop → show all participants
participants = load_participants(csv_path)
print(f"\nTotal participants saved: {len(participants)}")
for p in participants:
    print(p)