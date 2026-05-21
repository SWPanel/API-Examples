#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "${SCRIPT_DIR}/helpers.sh"

load_env

source "${SCRIPT_DIR}/config.sh"

api_request() {
    
    local method="$1"
    local endpoint="$2"
    local data="$3"

    response=$(curl \
        -s \
        -w "\n%{http_code}" \
        -X "$method" \
        "${BASE_URL}/${endpoint}" \
        -H "Authorization: Bearer ${API_TOKEN}" \
        -H "Content-Type: application/json" \
        -d "$data"
    )

    http_body=$(echo "$response" | sed '$d')
    http_status=$(echo "$response" | tail -n1)

    echo "HTTP STATUS: $http_status"

    if command -v jq >/dev/null 2>&1; then

        if echo "$http_body" | jq empty 2>/dev/null; then
            echo "$http_body" | jq
        else
            echo "$http_body"
        fi

    else

        echo "$http_body"

    fi
}