<?php

class Client
{
    protected string $baseUrl;
    protected string $apiToken;

    public function __construct()
    {
        // Read config file, so we can get the base_url and token (relative route)
        $config = require __DIR__ . '/config.php';

        $this->baseUrl  = rtrim($config['base_url'], '/');
        $this->apiToken = $config['api_token'];
    }

    /**
     * Send GET request
     */
    public function get(string $endpoint, array $params = []): array
    {
        if (!empty($params)) {
            $endpoint .= '?' . http_build_query($params);
        }

        return $this->request('GET', $endpoint);
    }

    /**
     * Send POST request
     */
    public function post(string $endpoint, array $data = []): array
    {
        return $this->request('POST', $endpoint, $data);
    }

    /**
     * Send PUT request
     */
    public function put(string $endpoint, array $data = []): array
    {
        return $this->request('PUT', $endpoint, $data);
    }

    /**
     * Send DELETE request
     */
    public function delete(string $endpoint, array $data = []): array
    {
        return $this->request('DELETE', $endpoint, $data);
    }

    /**
     * Main request handler
     */
    protected function request(string $method, string $endpoint, array $data = []): array 
    {
        // Init cURL session
        $curl = curl_init();

        // Configure cURL options
        curl_setopt_array($curl, [

            // Full request URL
            CURLOPT_URL => $this->baseUrl . '/' . ltrim($endpoint, '/'),
            
            // Return response as string
            CURLOPT_RETURNTRANSFER => true,
            
            // HTTP method
            CURLOPT_CUSTOMREQUEST => $method,

            // Request headers
            CURLOPT_HTTPHEADER => [
                'Authorization: Bearer ' . $this->apiToken,
                'Accept: application/json',
                'Content-Type: application/json',
            ],
        ]);

        // Attach JSON body if data exists
        if (!empty($data)) {
            curl_setopt(
                $curl,
                CURLOPT_POSTFIELDS,
                json_encode($data)
            );
        }

        // Execute request
        $response = curl_exec($curl);

        // Handle cURL errors
        if ($response === false) {

            return [
                'error' => curl_error($curl),
            ];
        }

        // Close cURL connection
        curl_close($curl);

        // Decode response into array
        return json_decode($response, true) ?? [];
    }
}