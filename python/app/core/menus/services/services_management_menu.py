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
            print("4. Delete service")
            print("5. Cloud Management")
            print("6. Hosting Management")
            print("7. Go back")

            option = Input.get("\nOption: ")

            if option == "1":
                ServicesUI.get_services()

            elif option == "2":
                ServicesUI.get_check_status()

            elif option == "3":
                ServicesUI.post_create_new_service()

            elif option == "4":
                ServicesUI.delete_service()

            elif option == "5":
                CloudMenu().run()

            elif option == "6":
                HostingMenu().run()

            elif option == "0":
                break

            else:
                print("Option not valid")

