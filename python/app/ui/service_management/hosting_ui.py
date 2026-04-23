from app.helpers.input import Input
from app.services.service_management.hosting_service import HostingService

class HostingUI:
    # ====================
    # POST
    # ====================
    @staticmethod
    def post_start_hosting():
        service = Input.required("\nService ID: ").upper()

        print("\nStarting hosting...")

        response = HostingService().post_start_hosting(service)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_stop_hosting():
        service = Input.required("\nService ID: ").upper()

        print("\nStopping hosting...")

        response = HostingService().post_stop_hosting(service)

        print("Done!\n")

        Input.json_formatter(response)
