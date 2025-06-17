
import subprocess

while True:  # Runs until manually exited
    print("\nELH Chain Command Menu")
    print("1: Add Transaction")
    print("2: Mine New Block")
    print("3: View Blockchain")
    print("4: View Filtered Blockchain")
    print("0: Exit")

    x = input("Enter 1, 2, 3, 4, or 0: ")

    if x == "1":
        sender = input("Enter sender name: ")
        recipient = input("Enter recipient name: ")
        amount = input("Enter amount: ")

        command1 = ["curl", "-X", "POST", "-H", "Content-Type: application/json", 
                    "-d", f'{{"sender": "{sender}", "recipient": "{recipient}", "amount": {amount}}}', 
                    "http://localhost:5000/transactions/new"]

        result = subprocess.run(command1, capture_output=True, text=True)
        print(result.stdout)

    elif x == "2":
        command2 = ["curl", "http://localhost:5000/mine"]
        result = subprocess.run(command2, capture_output=True, text=True)
        print(result.stdout)

    elif x == "3":
        command3 = ["curl", "http://localhost:5000/chain"]
        result = subprocess.run(command3, capture_output=True, text=True)
        print(result.stdout)

    elif x == "4":
        command3 = ["curl", "http://localhost:5000/chain/filtered"]
        result = subprocess.run(command3, capture_output=True, text=True)
        print(result.stdout)


    elif x == "0":
        print("Exiting...")
        break  

    else:
        print("Invalid input! Please enter 1, 2, 3, 4 or 0.")
