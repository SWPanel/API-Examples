from app.helpers.input import Input
from app.core.menus.services.services_menu import ServicesMenu
from app.core.menus.mail.mail_menu import MailMenu
from app.core.menus.ftp.ftp_menu import FTPMenu
from app.core.menus.database.database_menu import DatabaseMenu
from app.core.menus.dns.dns_menu import DNSMenu
from app.core.menus.dnssec.dnssec_menu import DNSSECMenu
from app.core.menus.crons.cron_menu import CronsMenu
from python.app.core.menus.domains.domains_menu import DomainsMenu
from python.app.core.menus.ssl.ssl_menu import SSLMenu

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
            print("8. Domain Management")
            print("9. SSL Management")
            print("0. Exit")

            option = Input.get("\nOption: ")

            if option == "1":
                ServicesMenu().run()

            elif option == "2":
                MailMenu().run()

            elif option == "3":
                FTPMenu().run()

            elif option == "4":
                DatabaseMenu().run()

            elif option == "5":
                DNSMenu().run()

            elif option == "6":
                DNSSECMenu().run()

            elif option == "7":
                CronsMenu().run()

            elif option == "8":
                DomainsMenu().run()

            elif option == "9":
                SSLMenu().run()

            elif option == "0":
                print("\nBye!")
                break

            else:
                print("Option not valid")