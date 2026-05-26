<?php

// Load client file
require_once __DIR__ . './../client.php';

// Init client
$client = new Client();

// Assign service_id 
$service_id = 'XX012';

$response = $client->post('/services/' . $service_id . '/cloud/start/'); // Search for specific service

// Print HTTP response
print_r($response);
