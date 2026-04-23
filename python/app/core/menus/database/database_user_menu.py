from app.helpers.input import Input
from app.ui.database_management.database_user_ui import DatabaseUserUI

class DatabaseUserMenu:
    def run(self):
        while True:
            print("\n=== DATABASES USERS ===")
            print("1. List database users")
            print("2. Create new database user")
            print("3. Edit database user")
            print("4. Eliminate database user")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DatabaseUserUI.get_db_user()

            elif option == "2":
                DatabaseUserUI.post_create_new_user()

            elif option == "3":
                DatabaseUserUI.put_update_account()

            elif option == "4":
                DatabaseUserUI.delete_account()

            elif option == "0":
                break

            else:
                print("Option not valid")