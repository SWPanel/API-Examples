from app.helpers.input import Input
from app.ui.mail_management.mailing_list_ui import MailingListUI

class MailingListMenu:
    def run(self):
        while True:
            print("\n=== MAILING LIST ===")
            print("1. List mailing lists")
            print("2. Create new mailing list")
            print("3. Add/remove emails from list")
            print("4. Modify existing list")
            print("5. Delete list")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                MailingListUI.get_mailing_lists()

            elif option == "2":
                MailingListUI.post_create_new_mailing_list()

            elif option == "3":           
                MailingListUI.post_add_remove_emails_mailing_list()

            elif option == "4":
                MailingListUI.put_update_mailing_list()

            elif option == "5":
                MailingListUI.delete_mailing_list()

            elif option == "0":
                break

            else:
                print("Option not valid")