from app.helpers.input import Input
from python.app.ui.domains.domains_ui import DomainsUI

class DomainsMenu:
    def run(self):
        while True:
            print("\n=== DOMAIN MANAGEMENT ===")
            print("1. List my domains")
            print("2. Register domain")
            print("3. Transfer domain")
            print("4. Renew domain")
            print("5. List extensions prices")
            print("6. Check availability")
            print("7. Whois")
            print("8. Domain Contacts")
            print("9. Hostnames")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DomainsUI().get_domains()

            elif option == "2":
                DomainsUI().post_register_domain()

            elif option == "3":
                DomainsUI().post_transfer_domain()

            elif option == "4":
                DomainsUI().post_renew_domain()
            
            elif option == "5":
                DomainsUI().get_extensions()
            
            elif option == "6":
                DomainsUI().get_availability()
            
            elif option == "7":
                DomainsUI().get_whois()
            
            elif option == "8":
                self.contacts()
            
            elif option == "9":
                self.hostanmes()

            elif option == "0":
                break

            else:
                print("Option not valid")


    def contacts(self):
        print()
        while True:
            print("\n=== DOMAIN CONTACTS MANAGEMENT ===")
            print("1. List")
            print("2. Create")
            print("3. Modifiy")
            print("4. Delete")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DomainsUI().get_contacts()
            
            elif option == "2":
                DomainsUI().post_create_contact()
            
            elif option == "3":
                DomainsUI().put_update_contact()
            
            elif option == "4":
                DomainsUI().delete_contact()
            
            elif option == "0":
                break

            else:
                print("Option not valid")


    def hostanmes(self):
        print()
        while True:
            print("\n=== HOSTNAMES MANAGEMENT ===")
            print("1. List")
            print("2. Create")
            print("3. Modifiy")
            print("4. Delete")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DomainsUI().get_hostnames()
            
            elif option == "2":
                DomainsUI().post_create_hostname()
            
            elif option == "3":
                DomainsUI().put_update_hostname()
            
            elif option == "4":
                DomainsUI().delete_hostname()
            
            elif option == "0":
                break

            else:
                print("Option not valid")