#!/usr/bin/env bash

load_env() {

    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    local env_file="${script_dir}/../.env"

    if [ -f "$env_file" ]; then

        set -a
        source "$env_file"
        set +a

    else

        echo ".env not found"

    fi
}