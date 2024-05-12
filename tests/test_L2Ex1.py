import pytest

from L2Ex1 import Menu, Note, Notebook


def test_note_init():
    note1 = Note("It's time to learn", "time")
    assert note1.text == "It's time to learn"
    assert note1.tag == "time"
    assert note1.date is not None


def test_note_match():
    note1 = Note("It's time to learn", "time")
    assert note1.match("fun") == False
    assert note1.match("to") == True


def test_notebook_init():
    nbook1 = Notebook()
    assert nbook1.notes == []


def test_nbook_new_note():
    nbook1 = Notebook()
    note1 = Note("It's time to learn", "time")
    nbook1.new_note(note1)
    assert nbook1.notes[0] == note1


def test_nbook_modify_text():
    nbook1 = Notebook()
    note1 = Note("It's time to learn", "time")
    nbook1.new_note(note1)
    nbook1.modify_text(nbook1.notes[0].note_id, "It's time to rest")
    n1 = nbook1.notes[0]
    assert n1.text == "It's time to rest"


def test_nbook_modify_tag():
    nbook1 = Notebook()
    note1 = Note("It's time to learn", "time")
    nbook1.new_note(note1)
    nbook1.modify_tag(nbook1.notes[0].note_id, "relax")
    n1 = nbook1.notes[0]
    assert n1.tag == "relax"


def test_nbook_search():
    nbook1 = Notebook()
    note1 = Note("It's time to learn", "relax")
    note2 = Note("It's relax to learn", "time")
    nbook1.new_note(note1)
    nbook1.new_note(note2)
    assert len(nbook1.search("time")) == 2


def test_menu_init():
    m1 = Menu()
    assert isinstance(m1.notebook, Notebook)
    assert isinstance(m1.options, dict)


def test_show_menu(capsys):
    m1 = Menu()
    m1.show_menu()
    out, err = capsys.readouterr()
    assert out.strip() == ('"1": self.show_notes, "2": self.search_notes, '
                           '"3": self.add_note, "4": self.modify_note, "5": self.quit')


@pytest.mark.skip("Don't know how to test it, needed methods not implemented")
def test_menu_run():
    pass


def test_quit(capsys):
    m1 = Menu()
    m1.quit()
    out, err = capsys.readouterr()
    assert out.strip() == "Goodbye!"


def test_menu_add_note():
    m1 = Menu()
    m1.add_note("Dogs", "You shall love dogs")
    assert m1.notebook.notes[0].text == "You shall love dogs"
    assert m1.notebook_len == 1


def test_search_notes(capsys):
    m1 = Menu()
    m1.add_note("Dogs", "You shall love dogs")
    m1.add_note("Cats", "You shall love cats")
    m1.add_note("Gnomes", "You shall hate something")
    m1.search_notes("love")
    out, err = capsys.readouterr()
    assert out.strip() == (
        f"Note {m1.notebook.notes[0].note_id} Dogs: You shall love dogs\n" f"Note {m1.notebook.notes[1].note_id} Cats: You shall love cats"
    )


def test_show_notes(capsys):
    m1 = Menu()
    m1.add_note("Dogs", "You shall love dogs")
    m1.add_note("Cats", "You shall love cats")
    m1.add_note("Gnomes", "You shall hate something")
    m1.show_notes()
    out, err = capsys.readouterr()
    assert out.strip() == (
        f"Note {m1.notebook.notes[0].note_id} Dogs: You shall love dogs\n"
        f"Note {m1.notebook.notes[1].note_id} Cats: You shall love cats\n"
        f"Note {m1.notebook.notes[2].note_id} Gnomes: You shall hate something"
    )