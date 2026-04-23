from app.helpers.input import Input
from app.helpers.main import Helpers
from app.services.dns_management.dns_service import DNSService

class DNSUI:
    DNS_TYPES = [
        "A (Host)",
        "AAA (Host)",
        "CNAME (Alias)",
        "DKIM (TXT register)",
        "DMARC (TXT register)",
        "MX (Mail)",
        "SRV",
        "TLSA",
    ]


    # ====================
    # GET
    # ====================
    @staticmethod
    def get_dns():
        service = Input.required("\nService ID: ").upper()

        print("\nLoading DNS records...")

        response = DNSService().get_all(service)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_dns_record():
        service = Input.required("\nService ID: ").upper()
        zone    = Input.required("DNS zone: ")

        while True:
            print("Type: ")

            for i, type in enumerate(DNSUI.DNS_TYPES, 1):
                print(f"\t{i}. {type}")

            choice = Input.get("\nOption: ")

            if choice == "1":
                host = Input.required("Host name (without extension): ")
                ip = Input.required("Host IP: ")

                record = {
                    "name": host,
                    "type": "A",
                    "data": {
                        "ip": ip
                    }
                }

                break

            elif choice == "2":
                host = Input.required("Host name (without extension): ")
                ip = Input.required("Host IPv6: ")

                record = {
                    "name": host,
                    "type": "AAA",
                    "data": {
                        "ip": ip
                    }
                }

                break

            elif choice == "3":
                alias  = Input.required("Alias (without extension): ")
                target = Input.required("Destination server: ")

                record = {
                    "name": alias,
                    "type": "CNAME",
                    "data": {
                        "target": target
                    }
                }

                break

            elif choice == "4":
                dkim = Input.required("Selector (without extension): ").strip()

                if not dkim.lower().endswith("._domainkey"):
                    dkim += "._domainkey"

                target = Input.required("TXT content: ")

                record = {
                    "name": dkim,
                    "type": "DKIM",
                    "data": {
                        "value": target
                    }
                }

                break

            elif choice == "5":
                dmarc = Input.required("DMARC content (without extension): ").strip()

                if not dmarc.lower().endswith("_dmarc"):
                    dmarc += "_dmarc"

                target = Input.required("TXT content: ")

                record = {
                    "name": dmarc,
                    "type": "DMARC",
                    "data": {
                        "value": target
                    }
                }

                break

            elif choice == "6":
                alias    = Input.required("Alias name: ")
                priority = Helpers.ask_int_with_step("Priority (0...65535): ", 0, 65535, 1)
                exchange = Input.required("Mail server: ")

                record = {
                    "name": alias,
                    "type": "MX",
                    "data": {
                        "priority": priority,
                        "exchange": exchange    
                    }
                }

                break

            elif choice == "7":
                service_autodiscover = Input.required("Service autodiscover (without extension): ").strip()

                if not service_autodiscover.lower().endswith("_autodiscover"):
                    service_autodiscover += "_autodiscover"
   
                priority = Helpers.ask_int_with_step("Priority (0...65535): ", 0, 65535, 1)
                weight   = Helpers.ask_int_with_step("Weight (0...65535): ", 0, 65535, 1)
                port     = Helpers.ask_int_with_step("Port (0...65535): ", 0, 65535, 1)
                target   = Input.required("Target: ")

                record = {
                    "name": service_autodiscover,
                    "type": "SRV",
                    "data": {
                        "priority": priority,
                        "weight": weight,
                        "port": port,
                        "target": target    
                    }
                }

                break

            elif choice == "8":
                alias         = Input.required("Alias: ")
                certificate   = Input.required("TLSA hash: ")
                usage         = Helpers.ask_int_with_step("Usage (0...255): ", 1, 255, 1)
                selector      = Helpers.ask_int_with_step("Usage (0...255): ", 1, 255, 1)
                matching_type = Helpers.ask_int_with_step("Usage (0...255): ", 1, 255, 1)

                record = {
                    "name": alias,
                    "type": "TLSA",
                    "data": {
                        "usage": usage,
                        "selector": selector,
                        "matching_type": matching_type,
                        "certificate": certificate    
                    }
                }

                break

            else:
                print("Option not valid")

        body = {
            "zone": zone,
            "record": record
        }

        print("\nCreating new DNS record...")

        response = DNSService().post_create_new_dns_record(service, body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_create_advanced_dns_record():
        service  = Input.required("\nService ID: ").upper()
        dns_zone = Input.required("DNS Zone: ")

        print("\nCreating advanced DNS record...")

        response = DNSService().post_create_advanced_dns_record(service, dns_zone)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_recreate_dns_zone():
        service  = Input.required("\nService ID: ").upper()
        dns_zone = Input.required("DNS Zone: ")

        print("\nRecreating DNS record...")

        response = DNSService().post_recreate_dns_zone(service, dns_zone)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_change_ttl_dns_zone():
        service  = Input.required("\nService ID: ").upper()
        dns_zone = Input.required("DNS Zone: ")
        ttl      = Input.ask_int("New TTL value: ")

        body = {
            "ttl": {
                "value": ttl
            }
        }

        print("\nRecreating DNS record...")

        response = DNSService().post_change_ttl_dns_zone(service, dns_zone, body)

        print("Done!\n")

        Input.json_formatter(response)

    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_dns_record():
        service   = Input.required("\nService ID: ").upper()
        zone      = Input.required("Zone: ")
        record_id = Input.required("DNS record ID: ")

        name = Input.get("New DNS name (leave empty to skip): ")
        type = Input.get("New Type (leave empty to skip): ")
        ip   = Input.get("New IP (leave empty to skip): ")

        body = {
            "zone": zone
        }

        record = {}
        data = {}

        if name:
            record["name"] = name

        if type:
            record["type"] = type

        if ip:
            data["ip"] = ip

        if data:
            record["data"] = data

        if record:
            body["record"] = record


        if len(body) == 1:
            print("Nothing to update!")
            return


        print(body)


        print("\nUpdating DNS record...")

        response = DNSService().put_update_dns_record(service, record_id, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_dns_record():
        service   = Input.required("\nService ID: ").upper()
        record_id = Input.required("DNS record ID: ")

        print("\nDeleting DNS record...")

        response = DNSService().delete_dns_record(service, record_id)

        print("Done!\n")

        Input.json_formatter(response)
