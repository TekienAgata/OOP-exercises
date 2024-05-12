import datetime
from uuid import uuid4


class Note:
    def __init__(self, txt: str, tag: str):
        self.text = txt
        self.tag = tag
        self.date = datetime.datetime.now()
        self.note_id = uuid4()

    def match(self, txt: str) -> bool:
        if txt in self.text or txt in self.tag:
            return True
        return False

    def __str__(self) -> str:
        return f"Note {self.note_id} {self.tag}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, n: Note):
        self.notes.append(n)

    def modify_text(self, note_id: uuid4, txt: str):
        the_note = self.match_id(note_id)
        the_note.text = txt

    def modify_tag(self, note_id: uuid4, tag: str):
        the_note = self.match_id(note_id)
        the_note.tag = tag

    def search(self, txt: str) -> list:
        note_list = []
        for note in self.notes:
            if note.match(txt):
                note_list.append(note)
        return note_list

    def match_id(self, note_id: uuid4) -> Note:
        for note in self.notes:
            if note.note_id == note_id:
                return note
            
class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }
        self.notebook_len = 0

    def show_notes(self, note_list: list = None):
        if note_list is None:
            for note in self.notebook.notes:
                print(note)
        else:
            for note in note_list:
                print(note)

    def search_notes(self, key_word: str):
        self.show_notes(self.notebook.search(key_word))

    def add_note(self, tag: str, txt: str):
        self.notebook.new_note(Note(txt, tag))
        self.notebook_len += 1

    def modify_note(self):
        note_id = int(input("Which note do you wish to modify?"))
        print(self.notebook.notes[note_id - 1])
        tag = input("What would you like the tag to be?")
        text = input("What would you like the text to be")
        self.notebook.modify_tag(note_id, tag)
        self.notebook.modify_text(note_id, text)

    def quit(self):
        print("Goodbye!")

    def show_menu(self):
        print(
            '"1": self.show_notes, "2": self.search_notes, '
            '"3": self.add_note, "4": self.modify_note, "5": self.quit'
        )
    def run(self):
        while True:
            self.show_menu()
            key = input("What would you like to do?")
            if key == "5":
                self.quit()
                break
            if key in self.options:
                self.options[key]()
            else:
                print("Invalid option, please try again.")
