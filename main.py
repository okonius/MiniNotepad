def file_read(path="dane.txt"):
    with open(path, "r", encoding="utf-8") as file:
        try:
         return file.read().splitlines()
        except FileNotFoundError:
            return []

def save_notes(notes, path="dane.txt"):
    with open(path, "w", encoding="utf-8") as file:
        for line in notatki:
            file.write(f"{notes}\n")

def new_note():
    note = input("Enter note: ")
    notes_list = file_read()
    notes_list.append(note)
    save_notes(notes_list)
    print("Note saved!")

def show_notes():
    notes = file_read()

    print("--- Your notes ---")
    for i, line in enumerate(notes, start=1):
        print(f"{i}. {notes}\n")
    print("\n ---")

def edit_note():
    notes = file_read()
    try:
        if not notes:
            print("File is empty or doesn't exist!")

        show_notes()

        choice = int(input("Choose the note to edit: "))
        if choice <= 0:
            raise IndexError

        new_content = input("Enter new content of the note!:\n")

        notes[choice - 1] = new_content

    except ValueError:
        print("Enter correct option!")

    except IndexError:
        print("Note with this number doesn't exist!")





