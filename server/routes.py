from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.model import NoteSchema

router = APIRouter()

notes = {
    "1": {
        "title": "My first note",
        "content": "This is the first note in my notes application"
    },
    "2": {
        "title": "Uniform circular motion.",
        "content": "Consider a body moving round a circle of radius r, wit uniform speed v as shown below. The speed everywhere is the same as v but direction changes as it moves round the circle."
    }
}


@router.get("/")
def get_notes() -> dict:
    return {
        "data": notes
    }

@router.get("/{id}")
async def get_note(id: str) -> dict:
    if int(id) > len(notes):
        return {
            "error": "Invalid note ID"
        }

    for note in notes.keys():
        if note == id:
            return {
                "data": notes[note]
            }

    return {
        "Error": "Invalid ID"
    }

@router.post("/")
def add_note(note: NoteSchema = Body(...)) -> dict:
    notes[str(len(notes)+1)] = note.dict()

    return {
        "message": "Note added successfully"
    }
#
@router.put("/{id}")
def update_note(id: str, note: NoteSchema):
    stored_note = notes[id]
    stored_note_model = NoteSchema(**stored_note)
    update_data = note.dict(exclude_unset=True)
    updated_note = stored_note_model.copy(update=update_data)
    notes[id] = jsonable_encoder(updated_note)
    return {
        "message": "Note updated successfully"
    }


@router.delete("/{id}")
def delete_note(id: str) -> dict:
    if int(id) > len(notes):
        return {
            "error": "Invalid note ID"
        }

    for note in notes.keys():
        if note == id:
            del notes[note]
            return {
                "message": "Note deleted"
            }

    return {
        "error": "Note with {} doesn't exist".format(id)
    }

