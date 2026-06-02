from app.helpers.input import Input
from app.ui.database.database_ui import DatabaseUI
from app.core.menus.database.database_user_menu import DatabaseUserMenu

class DatabaseMenu:
    def run(self):
        while True:
            print("\n=== DATABASE MANAGEMENT ===")
            print("1. List databases")
            print("2. Create new database")
            print("3. Edit database")
            print("4. Eliminate database")
            print("5. Databases users menu")
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

            elif option == "5":
                DatabaseUserMenu().run()

            elif option == "0":
                break

            else:
                print("Option not valid")


