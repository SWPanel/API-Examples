<?php

// Load client file
require_once __DIR__ . './../client.php';

// Init client
$client = new Client();

// Assign service_id (optional)
$service_id = 'XX012';

// $response = $client->get('/services/' . $service_id); // Search for specific service
$response = $client->get('/services/');   // Search for all services

// Print HTTP response
print_r($response);
