from app.helpers.input import Input
from app.ui.mail_management.mail_ui import MailUI

class MailAccountsMenu:
    def run(self):
        while True:
            print("\n=== EMAIL ACCOUNTS ===")
            print("1. Get a list")
            print("2. Get used space")
            print("3. Get login SWPanel information")
            print("4. Create a new mail account")
            print("5. Set login SWPanel information")
            print("6. Stop account")
            print("7. Start account")
            print("8. Update account")
            print("9. Delete account")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                MailUI.get_emails_accounts()

            elif option == "2":
                MailUI.get_used_space_mail_account()

            elif option == "3":
                MailUI.get_login_swpanel_info()

            elif option == "4":
                MailUI.post_create_new_email()

            elif option == "5":
                MailUI.post_update_login_swpanel_info()
            
            elif option == "6":
                MailUI.post_stop_mail()
            
            elif option == "7":
                MailUI.post_start_mail()

            elif option == "8":
                MailUI.put_update_mail_account()

            elif option == "9":
                MailUI.delete_mail_account()

            elif option == "0":
                break

            else:
                print("Option not valid")