import { apiRequest } from "../client.js";

const service_id = 'XX012';

await apiRequest('GET', 'services/');
// await apiRequest('GET', `services/${service_id}/`); // Search for service_id