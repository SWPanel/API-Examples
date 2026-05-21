<?php

class Client
{
    protected string $baseUrl;
    protected string $apiToken;

    public function __construct()
    {
        $config = require __DIR__ . '/config.php';

        $this->baseUrl  = rtrim($config['base_url'], '/');
        $this->apiToken = $config['api_token'];
    }

    public function get(string $endpoint, array $params = []): array
    {
        if (!empty($params)) {
            $endpoint .= '?' . http_build_query($params);
        }

        return $this->request('GET', $endpoint);
    }

    public function post(string $endpoint, array $data = []): array
    {
        return $this->request('POST', $endpoint, $data);
    }

    public function put(string $endpoint, array $data = []): array
    {
        return $this->request('PUT', $endpoint, $data);
    }

    public function delete(string $endpoint, array $data = []): array
    {
        return $this->request('DELETE', $endpoint, $data);
    }

    protected function request(
        string $method,
        string $endpoint,
        array $data = []
    ): array {

        $curl = curl_init();

        curl_setopt_array($curl, [
            CURLOPT_URL            => $this->baseUrl . '/' . ltrim($endpoint, '/'),
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CUSTOMREQUEST  => $method,
            CURLOPT_HTTPHEADER     => [
                'Authorization: Bearer ' . $this->apiToken,
                'Accept: application/json',
                'Content-Type: application/json',
            ],
        ]);

        if (!empty($data)) {
            curl_setopt(
                $curl,
                CURLOPT_POSTFIELDS,
                json_encode($data)
            );
        }

        $response = curl_exec($curl);

        if ($response === false) {

            return [
                'error' => curl_error($curl),
            ];
        }

        curl_close($curl);

        return json_decode($response, true) ?? [];
    }
}