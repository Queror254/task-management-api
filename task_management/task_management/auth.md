## Authentication Setup

### Basic Authentication

This API is secured with Django’s built-in Basic Authentication. To access the API, use a username and password.

#### Steps to Test:

1. Use a tool like Postman or `curl`.
2. Add `Authorization: Basic <base64-encoded-credentials>` to the headers.
3. Example `curl` request:
   ```bash
   curl -u username:password http://127.0.0.1:8000/api/tasks/
   ```
