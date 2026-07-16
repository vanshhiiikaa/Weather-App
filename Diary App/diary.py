import json
while True:
    print("PERSONAL DIARY\n1.Add Entry\n2.View Entries\n3.Search Entry\n4.Delete Entry\n5.Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1 :
        date = input("Enter date(YYYY-MM-DD): ")
        title = input("Enter title: ")
        entry = input("Enter your diary entry: ")
        
        new_entry = {
           "date": date,
           "title": title,
           "entry": entry
        }
        file_path = "Diary App/diary.json"

        try:
            with open(file_path, "r") as file:
               diary_entries = json.load(file)

        except FileNotFoundError:
            diary_entries = []

        diary_entries.append(new_entry)

        with open(file_path, "w") as file:
            json.dump(diary_entries, file, indent=4)

        print("Diary Entry Saved!")

    elif choice == 2 :
        file_path = "Diary App/diary.json"

        try:
            with open(file_path, "r") as file:
               diary_entries = json.load(file)

            for index, info in enumerate(diary_entries, start=1):
                print("\nEntry", index)
                print("Date:", info["date"])
                print("Title:", info["title"])
                print("Diary:", info["entry"])
                print("----------------")

        except FileNotFoundError:
            print("No diary entries available.")
        
    elif choice == 3 :
        file_path = "Diary App/diary.json"

        search = input("Enter tilte to search: ")
        try: 
            with open(file_path,"r") as file:
                diary_entries = json.load(file)

            found = False
            for index, entry in enumerate(diary_entries, start=1):
                if search.lower() in entry["title"].lower():
                    print("\nEntry", index)
                    print("Date:", entry["date"])
                    print("Title:", entry["title"])
                    print("Diary:", entry["entry"])
                    print("----------------")
                    found = True

            if found == False:
                print("No matching entry found.")

        except FileNotFoundError:
            print("No diary entries available.")
    
    elif choice == 4:
        file_path = "Diary App/diary.json"

        try:
            with open(file_path, "r") as file:
                diary_entries = json.load(file)

            if len(diary_entries) == 0:
                print("No entries available.")

            else:
                for index, entry in enumerate(diary_entries, start=1):
                   print("\nEntry", index)
                   print("Date:", entry["date"])
                   print("Title:", entry["title"])

                delete_choice = int(input("\nEnter entry number to delete: "))

                if delete_choice >= 1 and delete_choice <= len(diary_entries):
                   removed_entry = diary_entries.pop(delete_choice - 1)

                   with open(file_path, "w") as file:
                     json.dump(diary_entries, file, indent=4)

                   print("Deleted:", removed_entry["title"])

                else:
                   print("Invalid entry number.")

        except FileNotFoundError:
            print("No diary entries available.")
        

        
    elif choice == 5 :
        print("Goodbye!")
        break
    else:
        print("Invalid choice")