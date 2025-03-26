# Spotter API Postman Collection

This folder contains Postman collection and environment files for testing the Spotter API.

## Files

- `spotter_postman_collection.json` - The Postman collection containing all API endpoints
- `spotter_postman_environment.json` - The Postman environment file with variables

## Setup Instructions

1. Install [Postman](https://www.postman.com/downloads/) if you haven't already
2. Import the collection file (`spotter_postman_collection.json`):
   - Open Postman
   - Click on "Import" button
   - Select the collection file
3. Import the environment file (`spotter_postman_environment.json`):
   - Click on "Import" button again
   - Select the environment file
4. Select the "Spotter API Environment" from the environment dropdown in the top right corner

## Features

### Automatic Token Handling

The collection is configured to automatically extract and store the authentication token when you:

- Create a new user (signup)
- Login with existing credentials

The token is stored in the `auth_token` environment variable and is automatically included in the Authorization header for all protected endpoints.

### Available Endpoints

#### Authentication
- **Signup**: Create a new user account
- **Login**: Login with existing credentials

#### Users
- **Get All Users**: Retrieve a list of all users (protected)
- **Get User Details**: Get details for a specific user (protected)
- **Update User**: Update a user's information (protected)
- **Delete User**: Delete a user (protected)

## Usage

1. Start your Django server (`python manage.py runserver`)
2. Use the Login or Signup request to authenticate
3. After successful authentication, the token will be automatically stored
4. You can now use any of the protected endpoints without manually setting the token