from utils import load_notes, save_notes, add_note, list_notes, search_notes

def main():
    notes = load_notes()

    while True:
        command = input("\nCommand (add/list/search/exit): ").strip().lower()

        if command == "add":
            content = input("Note: ")
            add_note(notes, content)
            save_notes(notes)

        elif command == "list":
            list_notes(notes)

        elif command == "search":
            keyword = input("Search keyword: ")
            results = search_notes(notes, keyword)
            list_notes(results)

        elif command == "exit":
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
