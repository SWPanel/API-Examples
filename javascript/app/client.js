// Import results from the config file
import { BASE_URL, API_TOKEN } from "./config.js";

/**
 * Main request
 */
export async function apiRequest(method, endpoint, data = null) {
    // Construct full URL
    const url = `${BASE_URL}/${endpoint}`.replace(/([^:]\/)\/+/g, '$1');

    // Add the method and headers
    const options = {
        method,
        headers: {
            Authorization: `Bearer ${API_TOKEN}`,
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    };

    // Transform the body to a correct JSON format
    if (data) {
        options.body = JSON.stringify(data);
    }

    // Execute the petition using fetch class (javascript vanilla)
    const response = await fetch(url, options);

    // Read the response
    const body     = await response.text();

    // Print the response status
    console.log(`HTTP STATUS: ${response.status}`);

    // Check if errors
    try {
        // Transform the JSON to a correct format
        console.log(JSON.stringify(JSON.parse(body), null, 2));
    } catch {
        // Print error (usually it's on the repsonse of the body)
        console.log(body);
    }
}