from app.helpers.input import Input
from app.services.ssl.ssl_service import SSLService

class SSLUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_ssl():
        ssl_id = Input.get("\nSearch for SSL ID (leave empty for all SSL): ")

        if ssl_id == "":
            ssl_id = None

        print("\nLoading SSL...")

        response = SSLService().get_ssl(ssl_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_pfx():
        ssl_id = Input.get("\nSSL ID: ")

        if ssl_id == "":
            ssl_id = None

        print("\nDownloading PFX...")

        response = SSLService().get_pfx(ssl_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_tokens_dns():
        ssl_id = Input.get("\nSSL ID: ")

        if ssl_id == "":
            ssl_id = None

        print("\nLoading DNS validation tokens...")

        response = SSLService().get_tokens_dns(ssl_id)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_ssl():
        print()

        body = {}

        body["id_ssl_type"] = Input.required("SSL type ID: ")
        body["id_service"]  = Input.required("Service ID: ")

        print("\nValidation:")

        body["validation"] = {}
        
        validation = body["validation"]

        print("\tType: ")

        while True:
            print("1. DNS")
            print("2. Mail")

            option = Input.get("\nOption: ")

            if option == "1":
                validation["type"] = "DNS"
                break
            
            elif option == "2":
                validation["type"]  = "MAIL"
                validation["value"] = Input.required("Email address: ")

                break

            else:
                print("Option not valid")

        print("\nSubject:")

        body["subject"] = {}
        
        subject = body["subject"]

        subject["commonName"]         = Input.required("\tName: ")
        subject["Organization"]       = Input.required("\tOrganitzation name: ")
        subject["organizationalUnit"] = Input.required("\tDepartment: ")
        subject["country"]            = Input.required("\tCountry: ")

        print("\nContact information")

        contact = subject["contact"]

        contact["email"] = Input.required("\tEmail: ")
        contact["phone"] = Input.required("\tPhone (add extension): ")

        address = contact["address"]

        address["state"]      = Input.required("\tState: ")
        address["province"]   = Input.required("\tProvince: ")
        address["city"]       = Input.required("\tCity: ")
        address["street"]     = Input.required("\tStreet: ")
        address["postalCode"] = Input.required("\tPostal code: ")

        print("\nReissuing SSL...")

        response = SSLService().post_create_ssl(body)

        print("Done!\n")

        Input.json_formatter(response)
    
    @staticmethod
    def post_reissue_ssl():
        ssl_id = Input.get("\nSSL ID: ")

        if ssl_id == "":
            ssl_id = None

        print("\nReissuing SSL...")

        response = SSLService().post_reissue_ssl(ssl_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_renew_ssl():
        ssl_id = Input.get("\nSSL ID: ")

        if ssl_id == "":
            ssl_id = None

        print("\nRenewing SSL...")

        response = SSLService().post_renew_ssl(ssl_id)

        print("Done!\n")

        Input.json_formatter(response)
