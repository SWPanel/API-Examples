from app.helpers.input import Input
from app.ui.service_management.services_ui import ServicesUI
from app.core.menus.services.cloud_menu import CloudMenu
from app.core.menus.services.hosting_menu import HostingMenu

class ServicesMenu:
    def run(self):
        while True:
            print("\n=== SERVICE MANAGEMENT ===")
            print("1. List services")
            print("2. Check service status")
            print("3. Create new service")
            print("4. Cloud Management")
            print("5. Hosting Management")
            print("6. Go back")

            option = Input.get("\nOption: ")

            if option == "1":
                ServicesUI.get_services()

            elif option == "2":
                ServicesUI.get_check_status()

            elif option == "3":
                ServicesUI.post_create_new_service()

            elif option == "4":
                CloudMenu().run()

            elif option == "5":
                HostingMenu().run()

            elif option == "0":
                break

            else:
                print("Option not valid")

