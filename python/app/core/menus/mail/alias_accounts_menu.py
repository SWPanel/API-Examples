from app.helpers.input import Input
from app.ui.mail_management.alias_ui import AliasUI

class AliasAccountsMenu:
    def run(self):
        while True:
            print("\n=== ALIAS ACCOUNTS ===")
            print("1. List alias")
            print("2. Create an alias")
            print("3. Update existing alias")
            print("4. Delete alias")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                AliasUI.get_alias()

            elif option == "2":
                AliasUI.post_create_new_alias()

            elif option == "3":
                AliasUI.put_update_alias()

            elif option == "4":
                AliasUI.delete_alias()

            elif option == "0":
                break

            else:
                print("Option not valid")