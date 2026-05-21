#!/usr/bin/env bash

source "$(dirname "$0")/../client.sh"

service_id="XX012"

response=$(api_request "GET" "/services/" "")
# response=$(api_request "GET" "/services/${service_id}" "") # Search with specific service_id

echo "$response"