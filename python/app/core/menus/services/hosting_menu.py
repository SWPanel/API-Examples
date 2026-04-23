from app.helpers.input import Input
from app.ui.service_management.hosting_ui import HostingUI

class HostingMenu:
    def run(self):
        while True:
            print("\n=== HOSTING MANAGEMENT ===")
            print("1. Start hosting")
            print("2. Stop hosting")
            print("0. Go back")

            option = Input.get("\nOption: ")

            if option == "1":
                HostingUI.post_start_hosting()

            elif option == "2":
                HostingUI.post_stop_hosting()

            elif option == "0":
                break

            else:
                print("Option not valid")

