def read_notes(path="dane.txt"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_notes(notes, path="dane.txt"):
    with open(path, "w", encoding="utf-8") as file:
        for line in notes:
            file.write(f"{line}\n")

def new_note():
    note = input("Enter note: ")
    notes_list = read_notes()
    notes_list.append(note)
    save_notes(notes_list)
    print("Note saved!")

def show_notes():
    notes_list = read_notes()
    if not notes_list:
        print("File is empty or doesn't exist!")
        return

    print("--- Your notes ---")
    for i, line in enumerate(notes_list, start=1):
        print(f"{i}. {line}")
    print("\n ---")

def search_note():
    notes_list = read_notes()
    phrase = input("Enter phrase: ")
    found = False
    if not notes_list:
        print("File is empty or doesn't exist!")
        return
    for i, line in enumerate(notes_list, start=1):
        if phrase.lower() in line.lower():
            print(f"{i}. {line}")
            found = True
    if not found:
        print("\nNo matching notes found!")

def edit_note():
    notes_list = read_notes()
    try:
        if not notes_list:
            print("File is empty or doesn't exist!")
            return
        show_notes()

        choice = int(input("Choose a note to edit: "))
        if choice <= 0:
            raise IndexError

        new_content = input("Enter new content of the note!:\n")

        notes_list[choice - 1] = new_content

        save_notes(notes_list)

    except ValueError:
        print("Enter correct note number!")

    except IndexError:
        print("Note with this number doesn't exist!")


def delete_note():
    try:
        notes_list = read_notes()

        if not notes_list:
            print("File is empty or doesn't exist!")
            return
        show_notes()
        choice = int(input("Choose a note to delete: "))

        if choice <= 0:
            raise IndexError

        deleted_note = notes_list.pop(choice - 1)

        save_notes(notes_list)

        print(f"Deleted note: {deleted_note}")

    except ValueError:
        print("Enter correct note number!")

    except IndexError:
        print("Note with this number doesn't exist!")

def clear_all():
    cleaned_notepad = []
    save_notes(cleaned_notepad)
    print("All notes cleared!")


# Main app

print("==================")
print(" MINI NOTEPAD 4.1 ")
print("==================\n")

while True:
    print("\n --- Option menu --- \n"
          "1. Add new note\n"
          "2. Show all notes\n"
          "3. Search notes\n"
          "4. Edit note\n"
          "5. Delete note\n"
          "6. Clear all notes\n"
          "0. Exit app\n"
          )

    choice = input("Choose option: ")

    if choice == "1":
        new_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        search_note()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        clear_all()
    elif choice == "0":
        print("Goodbye!")
        break





