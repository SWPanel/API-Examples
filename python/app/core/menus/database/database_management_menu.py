from app.helpers.input import Input
from app.core.menus.database.database_user_menu import DatabaseUserMenu
from app.core.menus.database.database_menu import DatabaseMenu

class DatabaseManagementMenu:
    def run(self):
        while True:
            print("\n=== DATABASE MANAGEMENT ===")
            print("1. Databases users")
            print("2. Databases")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DatabaseUserMenu().run()

            elif option == "2":
                DatabaseMenu().run()

            elif option == "0":
                break

            else:
                print("Option not valid")