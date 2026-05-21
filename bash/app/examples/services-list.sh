#!/usr/bin/env bash

# Load main API client
source "$(dirname "$0")/../client.sh"

# Example service ID (optional)
service_id="XX012"

# Get all services
response=$(api_request "GET" "/services/" "")

# Get a specific service by ID
#
# Uncomment to use:
# response=$(api_request "GET" "/services/${service_id}" "")

# Print API response
echo "$response"