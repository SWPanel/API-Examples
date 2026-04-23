from app.helpers.input import Input
from app.ui.service_management.cloud_ui import CloudUI

class CloudMenu:
    def run(self):
        while True:
            print("\n=== CLOUD MANAGEMENT ===")
            print("1. Start cloud")
            print("2. Stop cloud")
            print("3. Park cloud")
            print("4. Unpark cloud")
            print("5. Clone cloud")
            print("6. White clone cloud")
            print("0. Go back")

            option = Input.get("\nOption: ")

            if option == "1":
                CloudUI.post_start_cloud()

            elif option == "2":
                CloudUI.post_stop_cloud()

            elif option == "3":
                CloudUI.post_park_cloud()
                
            elif option == "4":
                CloudUI.post_unpark_cloud()

            elif option == "5":
                CloudUI.post_clone_cloud()

            elif option == "6":
                CloudUI.post_white_clone_cloud()

            elif option == "0":
                break

            else:
                print("Option not valid")

