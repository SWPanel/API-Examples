from app.helpers.input import Input
from app.services.dnssec_management.dnssec_service import DNSSECService

class DNSSECUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_dnssec():
        service = Input.required("\nService ID: ").upper()

        print("\nLoading DNSSEC records...")

        response = DNSSECService().get_all(service)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_dnssec_record():
        service = Input.required("\nService ID: ").upper()
        domain  = Input.required("Domain: ")
        
        record = {}

        while True:
            print("Type:")

            print("\t1. DNSKEY")
            print("\t2. DS")

            option = Input.get("\nOption: ")

            if option == "1":
                ttl = Input.ask_int("TTL: ")

                flags     = Input.ask_int("Flags: ")
                protocol  = Input.ask_int("Protocol: ")
                algorithm = Input.ask_int("Algorithm: ")
                public_key = Input.required("Public key: ")

                record = {
                    "type": "DNSKEY",
                    "ttl": ttl,
                    "data": {
                        "flags": flags,
                        "protocol": protocol,
                        "algorithm": algorithm,
                        "public_key": public_key
                    }
                }

                break

            elif option == "2":
                ttl = Input.ask_int("TTL: ")

                key_tag     = Input.ask_int("Key tag: ")
                algorithm   = Input.ask_int("Algorithm: ")
                digest_type = Input.ask_int("Digest type: ")
                digest      = Input.required("Digest: ")
                
                record = {
                    "type": "DS",
                    "ttl": ttl,
                    "data": {
                        "key_tag": key_tag,
                        "algorithm": algorithm,
                        "digest_type": digest_type,
                        "digest": digest
                    }
                }

                break
            
            else:
                print("Option not valid")

        body = {
            "domain": domain,
            "record": record
        }

        print("\nCreating new DNSSEC record...")

        response = DNSSECService().post_create_new_dnssec_record(service, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_dnssec_record():
        service = Input.required("\nService ID: ").upper()
        domain  = Input.required("Domain: ")
        
        record = {}

        while True:
            print("Type:")

            print("\t1. DNSKEY")
            print("\t2. DS")

            option = Input.get("\nOption: ")

            if option == "1":
                ttl = Input.ask_int("TTL: ")

                flags      = Input.ask_int("Flags: ")
                protocol   = Input.ask_int("Protocol: ")
                algorithm  = Input.ask_int("Algorithm: ")
                public_key = Input.required("Public key: ")

                record = {
                    "type": "DNSKEY",
                    "ttl": ttl,
                    "data": {
                        "flags": flags,
                        "protocol": protocol,
                        "algorithm": algorithm,
                        "public_key": public_key
                    }
                }

                break

            elif option == "2":
                ttl = Input.ask_int("TTL: ")

                key_tag     = Input.ask_int("Key tag: ")
                algorithm   = Input.ask_int("Algorithm: ")
                digest_type = Input.ask_int("Digest type: ")
                digest      = Input.required("Digest: ")
                
                record = {
                    "type": "DS",
                    "ttl": ttl,
                    "data": {
                        "key_tag": key_tag,
                        "algorithm": algorithm,
                        "digest_type": digest_type,
                        "digest": digest
                    }
                }

                break
            
            else:
                print("Option not valid")

        body = {
            "domain": domain,
            "record": record
        }

        print("\nCreating new DNSSEC record...")

        response = DNSSECService().put_update_dnssec_record(service, body)

        print("Done!\n")

        Input.json_formatter(response)

    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_dnssec_record():
        service = Input.required("\nService ID: ").upper()
        domain  = Input.required("Domain: ")

        body = {
            "domain": domain
        }

        print("\nDeleting DNSSEC record...")

        response = DNSSECService().delete_dnssec_record(service, body)

        print("Done!\n")

        Input.json_formatter(response)
