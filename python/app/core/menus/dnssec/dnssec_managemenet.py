from app.helpers.input import Input
from app.ui.dnssec_management.dnssec_ui import DNSSECUI

class DNSSECManagementMenu:
    def run(self):
        while True:
            print("\n=== DNSSEC MANAGEMENT ===")
            print("1. Get DNSSEC records")
            print("2. Create new DNSSEC record")
            print("3. Modify DNSSEC record")
            print("4. Delete DNSSEC record")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                DNSSECUI.get_dnssec()

            elif option == "2":
                DNSSECUI().post_create_dnssec_record()

            elif option == "3":
                DNSSECUI.put_update_dnssec_record()

            elif option == "4":
                DNSSECUI.delete_dnssec_record()

            elif option == "0":
                break

            else:
                print("Option not valid")