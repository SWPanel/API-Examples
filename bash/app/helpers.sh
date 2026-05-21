#!/usr/bin/env bash

# Load environment variables from .env file
load_env() {

    # Get current script directory
    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    # Build .env absolute path
    # ../.env because the script is inside /scripts
    local env_file="${script_dir}/../.env"

    # Check if .env file exists
    if [ -f "$env_file" ]; then

        # Automatically export all loaded variables
        set -a

        # Load environment variables
        source "$env_file"

        # Disable automatic export
        set +a

    else
        # Show error if file does not exist
        echo ".env not found"
    fi
}