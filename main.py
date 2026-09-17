"""
Add a study session.
Record the subject.
Record the study duration.
Record the date.
Add optional notes.
Save sessions to a JSON file.
Display all recorded sessions.
Calculate total study time.
Show progress by subject.
-----------------------------
Create the project folder and basic program.
Add a single study session in memory.
Create a menu-driven command-line interface.
Add input validation.
Save and load sessions using JSON.
Display total study time.
Display progress by subject.
Separate the code into functions and modules.
Add automated tests.
Document the project and prepare it for GitHub.
"""
import datetime
import os
import json
def add_session():
    subject = (input("Enter the subject name: ")).capitalize()
    while True:
        try:
            duration = int(input("Enter the study duration (in minutes): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    notes = (input("Any notes?: ")).title()
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session = {
        "subject": subject,
        "duration": duration,
        "notes": notes,
        "time": time
    }
    return session
def save_session(session):
    filepath = "data.json"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            sessions = json.load(file)
    else:
        sessions = []
    sessions.append(session)
    with open(filepath, "w") as file:
        json.dump(sessions, file, indent=4)
    return "Session saved successfully."
def display_sessions():
    print("1. Today's study sessions.")
    print("2. This Month's study sessions.")
    print("3. All sessions.")
    print()
    choice = input("Enter a number to proceed: ")
    filepath = "data.json"
    if os.path.exists(filepath):
        if choice == "3":
            with open(filepath, "r") as file:
                content = json.load(file)
            for index, i in enumerate(content, start=1):
                print(f"{index}.")
                for key, value in i.items():
                    print(f"{key}: {value}")
                print()
            return None
        elif choice == "1":
            with open(filepath, "r") as file:
                content = json.load(file)
            for index, i in enumerate(content, start=1):
                if i["time"][:10] == (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[:10]:
                    print(f"{index}.")
                    for key, value in i.items():
                        print(f"{key}: {value}")
                    print()
            return None
        elif choice == "2":
            with open(filepath, "r") as file:
                content = json.load(file)
            for index, i in enumerate(content, start=1):
                if i["time"][:7] == (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[:7]:
                    print(f"{index}.")
                    for key, value in i.items():
                        print(f"{key}: {value}")
                    print()
            return None
        else:
            print()
            return None
    else:
        return "No records found. Kindly save a session first."
def calculate_study_time():
    time_daily = 0
    filepath = "data.json"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
           content = json.load(file)
        for i in content:
            if i["time"][:10] == (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[:10]:
                time_daily += i["duration"]
        return f"You studied for {time_daily} minutes today!."
    else:
        return "No records found. Kindly save a session first."
def display_progress():
    total_time = 0
    subject = (input("Enter the subject name: ")).capitalize()
    filepath = "data.json"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            content = json.load(file)
        for i in content:
            if i["subject"] == subject:
                total_time += i["duration"]
        return f"You have studied for a total of {total_time} minutes in the subject {(subject.upper())}. Well done and keep it up!."
    else:
        return "No records found. Kindly save a session first."
def main():
    is_running = True
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~WELCOME TO YOUR STUDY TRACKER~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    while is_running:
        print("1. Add a study session.")
        print("2. Display study sessions. ")
        print("3. What is my study time today? ")
        print("4. Show progress by subject. ")
        print("5. Quit the program. ")
        print()
        while True:
            try:
                choice = int(input("Enter a number to proceed: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        if choice == 1:
            result = add_session()
            save_session(result)
        elif choice == 2:
            display_sessions()
        elif choice == 3:
            print(calculate_study_time())
            print()
        elif choice == 4:
            print(display_progress())
            print()
        elif choice == 5:
            is_running = False
        else:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()
