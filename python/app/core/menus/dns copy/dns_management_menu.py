from app.helpers.input import Input
from app.ui.dns_management.dns_ui import DNSUI

class DNSManagementMenu:
    def run(self):
        while True:
            print("\n=== DNS MANAGEMENT ===")
            print("1. Get DNS records")
            print("2. Create new DNS record")
            print("3. Create advanced DNS record")
            print("4. Recreate DNS zone")
            print("5. Change TTL DNS zone")
            print("6. Modify DNS record")
            print("7. Delete DNS record")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DNSUI.get_dns()

            elif option == "2":
                DNSUI().post_create_dns_record()

            elif option == "3":
                DNSUI.post_create_advanced_dns_record()

            elif option == "4":
                DNSUI.post_recreate_dns_zone()

            elif option == "5":
                DNSUI.post_change_ttl_dns_zone()

            elif option == "6":
                DNSUI.put_update_dns_record()

            elif option == "7":
                DNSUI.delete_dns_record()

            elif option == "0":
                break

            else:
                print("Option not valid")