import { BASE_URL, API_TOKEN } from "./config.js";

export async function apiRequest(method, endpoint, data = null) {
    const url = `${BASE_URL}/${endpoint}`.replace(/([^:]\/)\/+/g, '$1');

    const options = {
        method,
        headers: {
            Authorization: `Bearer ${API_TOKEN}`,
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(url, options);
    const body     = await response.text();

    console.log(`HTTP STATUS: ${response.status}`);

    try {
        console.log(JSON.stringify(JSON.parse(body), null, 2));
    } catch {
        console.log(body);
    }
}