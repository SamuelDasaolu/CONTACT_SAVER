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

workspace_path = Path("WORKSPACE_FILES")
workspace_path.mkdir(exist_ok=True)
file_path = workspace_path / 'contacts.csv'

'''sadjhgsad'''
