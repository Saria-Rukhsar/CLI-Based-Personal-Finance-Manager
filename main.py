import time
import storage, utils

def main_menu(): 
    while True: 
        print("====== PERSONAL FINANCE MANAGER ======")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Balance")
        print("5. Filter by Category")
        print("6. Monthly Summary")
        print("7. Delete Transaction")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1" or choice == "2":
            amount = input("Enter your Amount: ")
            category = input("Enter your Category: ")
            while True:
                date = input("Enter Date(YYYY-MM-DD): ")
                try:
                    utils.validate_date(date)
                    break
                except Exception as e:
                    print(e)
                    time.sleep(2)
            des = input("Decryption: ")
            if choice == "1":
                storage.save_Data({"id":utils.generate_id(), "type":"income", "amount":amount, "category": category, "date":date, "description":des})
                print("Income Added Successfuly")
            else:
                storage.save_Data({"id":utils.generate_id(), "type":"expense", "amount":amount, "category": category, "date":date, "description":des})
                print("Expense Added Successfuly")
            time.sleep(2)

        elif choice == "3":
            try:
                print(storage.load_data())
            except:
                print("File Empty")
            time.sleep(2)

        elif choice == "4":
            print(utils.calculate_balance())
            time.sleep(2)

        elif choice == "5":
            print(utils.filter_by_category(input("Enter Category: ")))
            time.sleep(2)

        elif choice == "6":
            print(utils.monthly_summary(input("Enter Month (YYYY-MM): ")))
            time.sleep(2)

        elif choice == "7":
            print(utils.delete_transaction(input("Enter id of Transaction: ")))
            time.sleep(2)

        elif choice == "8":
            print("Exiting program...")
            time.sleep(1)
            break

        else:
            print("Invalid choice. Try again.")
            time.sleep(2)

main_menu()