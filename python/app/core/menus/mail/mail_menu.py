from app.helpers.input import Input
from app.core.menus.mail.mail_accounts_menu import MailAccountsMenu
from app.core.menus.mail.alias_accounts_menu import AliasAccountsMenu
from app.core.menus.mail.mailing_list_menu import MailingListMenu

class MailMenu:
    def run(self):
        while True:
            print("\n=== MAIL MANAGEMENT ===")
            print("1. Email account")
            print("2. Email alias")
            print("3. Mailing list")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                MailAccountsMenu().run()

            elif option == "2":
                AliasAccountsMenu().run()

            elif option == "3":
                MailingListMenu().run()

            elif option == "0":
                break

            else:
                print("Option not valid")