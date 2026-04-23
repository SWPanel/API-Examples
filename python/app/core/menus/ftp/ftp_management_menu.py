from app.helpers.input import Input
from app.ui.ftp_management.ftp_ui import FTPUI

class FTPMenu:
    def run(self):
        while True:
            print("\n=== FTP MANAGEMENT ===")
            print("1. List FTP accounts")
            print("2. Create new FTP account")
            print("3. Stop FTP account")
            print("4. Start FTP account")
            print("5. Modify FTP account")
            print("6. Delete FTP account")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                FTPUI.get_ftp_accounts()

            elif option == "2":
                FTPUI.post_create_new_account()

            elif option == "3":
                FTPUI.post_stop_account()

            elif option == "4":
                FTPUI.post_start_account()

            elif option == "5":
                FTPUI.put_update_account()

            elif option == "6":
                FTPUI.delete_account()

            elif option == "0":
                break

            else:
                print("Option not valid")