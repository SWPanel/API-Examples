// Load main request function
import { apiRequest } from "../client.js";

// Assign service_id (optional)
const service_id = 'XX012';

// Exeucte the request
await apiRequest('GET', 'services/');
// await apiRequest('GET', `services/${service_id}/`); // Search for service_id