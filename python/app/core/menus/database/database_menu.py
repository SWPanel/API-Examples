from app.helpers.input import Input
from app.ui.database_management.database_ui import DatabaseUI

class DatabaseMenu:
    def run(self):
        while True:
            print("\n=== DATABASES USERS ===")
            print("1. List databases")
            print("2. Create new database")
            print("3. Edit database")
            print("4. Eliminate database")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DatabaseUI.get_db()

            elif option == "2":
                DatabaseUI.post_create_new_db()

            elif option == "3":
                DatabaseUI.put_update_db()

            elif option == "4":
                DatabaseUI.delete_db()

            elif option == "0":
                break

            else:
                print("Option not valid")


