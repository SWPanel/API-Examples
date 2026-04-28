from app.helpers.input import Input
from app.core.menus.services.services_management_menu import ServicesMenu
from app.core.menus.mail.mail_management_menu import MailMenu
from app.core.menus.ftp.ftp_management_menu import FTPMenu
from app.core.menus.database.database_management_menu import DatabaseManagementMenu
from app.core.menus.dns.dns_management_menu import DNSManagementMenu
from app.core.menus.dnssec.dnssec_managemenet import DNSSECManagementMenu
from app.core.menus.crons.cron_management_menu import CronsManagementMenu


class MainMenu:
    def run(self):
        while True:
            print("\n=== MENU ===")
            print("1. Service Management")
            print("2. Mail Management")
            print("3. FTP Management")
            print("4. Database Management")
            print("5. DNS Management")
            print("6. DNSSec Management")
            print("7. Cron Management")
            print("0. Exit")

            option = Input.get("\nOption: ")

            if option == "1":
                ServicesMenu().run()

            elif option == "2":
                MailMenu().run()

            elif option == "3":
                FTPMenu().run()

            elif option == "4":
                DatabaseManagementMenu().run()

            elif option == "5":
                DNSManagementMenu().run()

            elif option == "6":
                DNSSECManagementMenu().run()

            elif option == "7":
                CronsManagementMenu().run()

            elif option == "0":
                print("\nBye!")
                break

            else:
                print("Option not valid")