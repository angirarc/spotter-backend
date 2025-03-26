# Fixture Data for Spotter App

This directory contains fixture data for testing and development purposes.

## Available Fixtures

- `user_data.json`: Contains sample user data
- `trip_data.json`: Contains sample trip data with coordinates for pickup and dropoff locations

## Loading Fixtures

To load the fixture data into your database, run the following commands from the project root:

```bash
python manage.py loaddata api/fixtures/user_data.json
python manage.py loaddata api/fixtures/trip_data.json
```

Make sure to load the user data first since the trip data references users via foreign keys.

## Data Format

### Trip Data

The trip data includes:
- Current location (city name)
- Pickup location (latitude,longitude format)
- Dropoff location (latitude,longitude format)
- Route instructions (array of turn-by-turn directions)
- Cycle used (type of bicycle)
- Creation date

Example coordinate format: `"37.7749,-122.4194"` (San Francisco)

This data can be used for testing map integrations, route calculations, and other location-based features of the application.