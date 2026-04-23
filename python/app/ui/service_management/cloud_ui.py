from app.helpers.input import Input
from app.services.service_management.cloud_service import CloudService

class CloudUI:
    # ====================
    # POST
    # ====================
    @staticmethod
    def post_start_cloud():
        service = Input.required("\nService ID: ")

        print("\nStarting cloud...")

        response = CloudService().post_start_cloud(service)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_stop_cloud():
        service = Input.required("\nService ID: ")

        print("\nStopping cloud...")

        response = CloudService().post_stop_cloud(service)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_park_cloud():
        service = Input.required("\nService ID: ")

        print("\nParking cloud...")

        response = CloudService().post_park_cloud(service)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_unpark_cloud():
        service = Input.required("\nService ID: ")

        print("\nUnparking cloud...")

        response = CloudService().post_unpark_cloud(service)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_clone_cloud():
        service = Input.required("\nService ID: ")

        print("\nClonning cloud...")

        response = CloudService().post_clone_cloud(service)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_white_clone_cloud():
        service = Input.required("\nService ID: ")

        print("\nWhite clonning cloud...")

        response = CloudService().post_white_clone_cloud(service)

        print("Done!\n")

        Input.json_formatter(response)
