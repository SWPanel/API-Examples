<?php

// Read .env file (relative route)
$env = parse_ini_file(__DIR__ . '/../.env');

return [
    'base_url'  => $env['BASE_URL'],
    'api_token' => $env['API_TOKEN'],
];