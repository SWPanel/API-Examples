<?php

require_once __DIR__ . './../client.php';

$client = new Client();

$service_id = 'XX012';

// $response = $client->get('/services/' . $service_id); // Search for specific service
$response = $client->get('/services/');   // Search for all services

print_r($response);
