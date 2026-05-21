#!/usr/bin/env bash

# Get current script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load helper functions
source "${SCRIPT_DIR}/helpers.sh"

# Load .env variables
load_env

# Load config variables/constants
source "${SCRIPT_DIR}/config.sh"

# Generic API request function
api_request() {
    
    # HTTP method
    local method="$1"

    # API endpoint
    local endpoint="$2"

    # JSON request body
    local data="$3"

    # Execute curl request
    response=$(curl \
        -s \
        -w "\n%{http_code}" \
        -X "$method" \
        "${BASE_URL}/${endpoint}" \
        -H "Authorization: Bearer ${API_TOKEN}" \
        -H "Content-Type: application/json" \
        -d "$data"
    )

    # Extract response body
    http_body=$(echo "$response" | sed '$d')

    # Extract HTTP status code
    http_status=$(echo "$response" | tail -n1)

    # Display HTTP status
    echo "HTTP STATUS: $http_status"

    # Check if jq is installed
    if command -v jq >/dev/null 2>&1; then

        # Check if response is valid JSON
        if echo "$http_body" | jq empty 2>/dev/null; then
            # Pretty print JSON response
            echo "$http_body" | jq
        else
            # Print raw response
            echo "$http_body"
        fi

    else
        # Print raw response if jq is unavailable
        echo "$http_body"
    fi
}