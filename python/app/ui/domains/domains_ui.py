from app.helpers.input import Input
from app.services.domains.domains_service import DomainsService

class DomainsUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_domains():
        domain_id = Input.get("\nSearch for domain ID (leave empty for all domains): ")

        if domain_id == "":
            domain_id = None

        print("\nLoading domains...")

        response = DomainsService().get_domains(domain_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_extensions():
        extension = Input.get("\nSearch for extension (leave empty for all extensions): ")

        if extension == "":
            extension = None

        print("\nLoading extensions...")

        response = DomainsService().get_extensions(extension)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_availability():
        domain = Input.required("\nDomain: ")

        print("\nChecking availibility...")

        response = DomainsService().get_availibility(domain)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_whois():
        domain = Input.required("\nDomain: ")

        print("\nChecking WhoIs information...")

        response = DomainsService().get_whois(domain)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_contacts():
        contact_id = Input.get("\nContact ID (leave empty for all contacts): ")

        if contact_id == "":
            contact_id = None

        print("\nLoading contacts...")

        response = DomainsService().get_contacts(contact_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_hostnames():
        hostname_id = Input.required("\nHostname ID (leave empty for all hostnames): ")

        if hostname_id == "":
            hostname_id = None

        print("\nLoading hostnames...")

        response = DomainsService().get_hostnames(hostname_id)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_register_domain():
        print()

        body = {
            "domain": Input.required("Domain: "),
            "years": 1,
            "additional": {
                "autorenew": {
                    "enable": Input.ask_bool("Autorenew (Y/N): ")
                }
            },
            "contacts": {
                "registrant": {
                    "id_contact": Input.required("Registrant contact ID: ")
                },
                "administrative": {
                    "id_contact": Input.required("Administrative contact ID: ")
                },
                "technical": {
                    "id_contact": Input.required("Technical contact ID: ")
                },
            },
        }

        hostnames = []

        while len(hostnames) < 4:
            value = Input.required(
                f"Hostname {len(hostnames) + 1}: "
            )

            hostnames.append(value)

            if len(hostnames) == 4:
                break

            if not Input.ask_bool("Add another hostname? (Y/N): "):
                break

        body["hostname"] = hostnames

        print("\nRegistering domain...")

        response = DomainsService().post_register_domain(body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_transfer_domain():
        print()

        body = {
            "domain": Input.required("Domain: "),
            "authcode": Input.required("Authcode: "),
            "additional": {
                "autorenew": {
                    "enable": Input.ask_bool("Autorenew (Y/N): ")
                }
            },
            "contacts": {
                "registrant": {
                    "id_contact": Input.required("Registrant contact ID: ")
                },
                "administrative": {
                    "id_contact": Input.required("Administrative contact ID: ")
                },
                "technical": {
                    "id_contact": Input.required("Technical contact ID: ")
                },
            },
        }

        hostnames = []

        while len(hostnames) < 4:
            value = Input.required(
                f"Hostname {len(hostnames) + 1}: "
            )

            hostnames.append(value)

            if len(hostnames) == 4:
                break

            if not Input.ask_bool("Add another hostname? (Y/N): "):
                break

        body["hostname"] = hostnames

        print("\nTransfering domain...")

        response = DomainsService().post_transfer_domain(body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_renew_domain():
        print()

        body = {
            "domain": Input.required("Domain: "),
            "years": Input.ask_int_with_step("Years to renew", 1, 10, 1)
        }

        print("\nRenewing domain...")

        response = DomainsService().post_renew_domain(body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_create_contact():
        print()

        body = {
            "address": {},
        }

        body["firstName"]         = Input.required("First name: ")
        body["lastName"]          = Input.required("Last name: ")
        body["company"]           = Input.required("Company name: ")
        body["taxId"]             = Input.required("Tax ID: ")
        body["email"]             = Input.required("Email: ")
        body["phone"]             = Input.required("Phone (extension required): ")
        body["legal_entity_type"] = Input.required("Legal entity type: ")

        print("\nAddress information:")

        address = body["address"]
        
        address["country"]    = Input.required("\tCountry: ")
        address["state"]      = Input.required("\tState: ")
        address["city"]       = Input.required("\tCity: ")
        address["street"]     = Input.required("\tStreet: ")
        address["postalCode"] = Input.required("\tPostal code: ")

        print("\nCreating new contact...")

        response = DomainsService().post_create_contact(body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_create_hostname():
        print()

        body = {}

        body["hostname"] = Input.required("Hostname: ")
        body["ip"]       = Input.required("IP: ")

        print("\nCreating new hostname...")

        response = DomainsService().post_create_hostname(body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_contact():
        print()

        contact_id = Input.required("Contact ID: ")

        body = {}

        def add_if_not_empty(key, value):
            if value.strip():
                body[key] = value

        add_if_not_empty("firstName",         Input.get("First name (leave empty to skip): "))
        add_if_not_empty("lastName",          Input.get("Last name (leave empty to skip): "))
        add_if_not_empty("company",           Input.get("Company name (leave empty to skip): "))
        add_if_not_empty("taxId",             Input.get("Tax ID (leave empty to skip): "))
        add_if_not_empty("email",             Input.get("Email (leave empty to skip): "))
        add_if_not_empty("phone",             Input.get("Phone (extension required) (leave empty to skip): "))
        add_if_not_empty("legal_entity_type", Input.get("Legal entity type (leave empty to skip): "))

        print("\nAddress information:")

        address = {}

        country = Input.get("\tCountry (leave empty to skip): ")
        state   = Input.get("\tState (leave empty to skip): ")
        city    = Input.get("\tCity (leave empty to skip): ")
        street  = Input.get("\tStreet (leave empty to skip): ")
        postal  = Input.get("\tPostal code (leave empty to skip): ")

        if country.strip():
            address["country"] = country

        if state.strip():
            address["state"] = state

        if city.strip():
            address["city"] = city

        if street.strip():
            address["street"] = street

        if postal.strip():
            address["postalCode"] = postal

        if address:
            body["address"] = address

        print("\nCreating new contact...")

        response = DomainsService().put_update_contact(contact_id, body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def put_update_hostname():
        print()

        hostname_id = Input.required("Hostname ID: ")

        body = {}

        def add_if_not_empty(key, value):
            if value.strip():
                body[key] = value

        add_if_not_empty("hostname", Input.get("Hostname (leave empty to skip): "))
        add_if_not_empty("ip",       Input.get("IP (leave empty to skip): "))

        print("\nCreating new hostname...")

        response = DomainsService().put_update_hostname(hostname_id, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_contact():
        print()

        contact_id = Input.required("Contact ID: ")


        print("\nDeleting contact...")

        response = DomainsService().delete_contact(contact_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def delete_hostname():
        print()

        hostname_id = Input.required("Hostname ID: ")

        print("\nDeleting hostname...")

        response = DomainsService().delete_hostname(hostname_id)

        print("Done!\n")

        Input.json_formatter(response)

