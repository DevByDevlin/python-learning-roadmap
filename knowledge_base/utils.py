import json
from datetime import datetime

FILE_NAME = "notes.json"

def load_notes():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(notes, content):
    note = {
        "id": len(notes) + 1,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    notes.append(note)

def list_notes(notes):
    for note in notes:
        print(f"{note['id']}: {note['content']} ({note['timestamp']})")

def search_notes(notes, keyword):
    return [note for note in notes if keyword.lower() in note["content"].lower()]
