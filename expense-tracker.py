import json
import os
import datetime

def load():
    filepath = "expense.json"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            content = json.load(file)
    else:
        content = {}
    return content
def view_expense():
    print("""
    1. Today's expenses.
    2. This Week's expenses.
    3. This Month's expenses.
    4. All expenses.
    """)
    print()
    choice = input("Enter a number to proceed: ")
    content = load()
    if choice == "4":
        for index, session in enumerate(content, start=1):
            print(f"{index}.")
            for key, value in session.items():
                print(f"{key}: {value}")
            print()
        return None
    elif choice == "1":
        for index, session in enumerate(content, start=1):
            if session["Time"][:10] == (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[:10]:
                print(f"{index}.")
                for key, value in session.items():
                    print(f"{key}: {value}")
                print()
        return None
    elif choice == "3":
        for index, session in enumerate(content, start=1):
            if session["Time"][:7] == (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[:7]:
                print(f"{index}.")
                for key, value in session.items():
                    print(f"{key}: {value}")
                print()
        return None
    elif choice == "2":
        for index, session in enumerate(content, start=1):
            crip =  (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[8:10]
            crip = int(crip)
            if (crip - 8) < int(session["Time"][8:10]) <= crip:
                print(f"{index}.")
                for key, value in session.items():
                    print(f"{key}: {value}")
                print()
        return None
    else:
        print("Please enter a valid number.")
        print()
        return None
def add_expense():
    diction = {"A": "Academic",
               "H": "Housing",
               "F": "Feeding",
               "T": "Transport",
               "P": "Personal Care",
               "HC": "Health Care",
               "S": "Savings",
               "O": "Others"}

    print("""
    Expense categories include: 
    1. Academic       (A)
    2. Housing        (H)
    3. Feeding        (F)
    4. Transport      (T)
    5. Personal Care  (P)
    6. Health Care   (HC)
    7. Savings        (S)
    8. Others         (O)
    """)
    category = (input("Enter the expense category (In full or with the acronym): ")).upper()
    if category in diction.keys():
        category = diction[category]
    while True:
        try:
            amount = float(input("Enter amount spent : "))
            if amount <= 0:
                print("The amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    payment_method = input("Enter the payment method: ")
    need_or_want = input("Was it a need or want? (N/W): ").upper()
    notes = (input("Any descriptions?: ")).strip()
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session = {
        "Category": category,
        "Amount": amount,
        "Payment_method": payment_method,
        "Need_or_want": need_or_want,
        "Description": notes,
        "Time": time,

    }
    return session
def average_expense():
    content = load()
    total = 0
    count = 0
    for index, session in enumerate(content, start=1):
        total += session["Amount"]
        count += 1
    try:
        average = total/count
    except ZeroDivisionError:
        average = 0
    print(f"Your average expense is ${average:.2f}")
def calculate_expense():
    print("""
    1. Expenses today
    2. Expenses for this month
    3. Expenses by category
    4. Total expenses
    """)
    choice = input("Enter a number to proceed: ")
    content = load()
    total = 0
    if choice == "1":
        for index, session in enumerate(content, start=1):
            if session["Time"][:10] == (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[:10]:
                total += session["Amount"]
        print(f"Your total expenses for today is ${total:.2f}")
    elif choice == "2":
        for index, session in enumerate(content, start=1):
            if session["Time"][:7] == (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))[:7]:
                total += session["Amount"]
        print(f"Your total expenses this month is ${total:.2f}")
    elif choice == "4":
        for index, session in enumerate(content, start=1):
            total += session["Amount"]
        print(f"Your total expenses for today is ${total:.2f}")
    elif choice == "3":
        print("""
        1. Academic       (A)
        2. Housing        (H)
        3. Feeding        (F)
        4. Transport      (T)
        5. Personal Care  (P)
        6. Health Care   (HC)
        7. Savings        (S)
        8. Others         (O)
        """)
        c = input("Enter a number to proceed: ")
        if c == "1":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Academic":
                    total += session["Amount"]
        elif c == "2":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Housing":
                    total += session["Amount"]
        elif c == "3":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Feeding":
                    total += session["Amount"]
        elif c == "4":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Transport":
                    total += session["Amount"]
        elif c == "5":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Personal Care":
                    total += session["Amount"]
        elif c == "6":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Health Care":
                    total += session["Amount"]
        elif c == "7":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Savings":
                    total += session["Amount"]
        elif c == "8":
            for index, session in enumerate(content, start=1):
                if session["Category"] == "Others":
                    total += session["Amount"]
        else:
            print("Please enter a valid input.")
        print(f"Your total expenses for that category is ${total:.2f}")
    else:
        print("Please enter a valid input.")
def save_expense(session):
    filepath = "expense.json"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            sessions = json.load(file)
    else:
        sessions = []
    sessions.append(session)
    with open(filepath, "w") as file:
        json.dump(sessions, file, indent=4)
    return "Session saved successfully."
def main():
    is_running = True
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~WELCOME TO YOUR EXPENSE TRACKER~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    while is_running:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("1. Add an expense."   )
        print("2. View expenses. "   )
        print("3. Average expense. " )
        print("4. Calculate expense.")
        print("5. Quit program."     )
        print("~~~~~~~~~~~~~~~~~~~~~")
        print()
        while True:
            try:
                choice = int(input("Enter a number to proceed: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        if choice == 5:
            is_running = False
        elif choice == 1:
            ses = add_expense()
            save_expense(ses)
        elif choice == 2:
            view_expense()
        elif choice == 3:
            average_expense()
        elif choice == 4:
            calculate_expense()
        else:
            print("Please enter a valid input.")
            continue
if __name__ == "__main__":
    main()