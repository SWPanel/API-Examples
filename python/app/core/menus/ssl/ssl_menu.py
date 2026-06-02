from app.helpers.input import Input
from app.ui.ssl.ssl_ui import SSLUI

class SSLMenu:
    def run(self):
        while True:
            print("\n=== SSL MANAGEMENT ===")
            print("1. List SSL")
            print("2. Download PFX")
            print("3. Get DNS validations tokens")
            print("4. Create new SSL")
            print("5. Reissue SSL")
            print("6. Renew SSL")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                SSLUI().get_ssl()
            
            elif option == "2":
                SSLUI().get_pfx()
            
            elif option == "3":
                SSLUI().get_tokens_dns()
            
            elif option == "4":
                SSLUI().post_create_ssl()
            
            elif option == "5":
                SSLUI().post_reissue_ssl()
            
            elif option == "6":
                SSLUI().post_renew_ssl()
            
            elif option == "0":
                break

            else:
                print("Option not valid")
