# Chocolate House Inventory and Flavor Management

## Description
A simple application to manage seasonal chocolate flavors, ingredient inventory, and customer suggestions, including allergy concerns.

## Setup Instructions

1. Clone this repository:
   git clone <repository_url> cd chocolate_house

2. Install the dependencies:
   pip install -r requirements.txt

3. Run the application:
   python app.py

## Docker Instructions
1. Build the Docker image:
   docker build -t chocolate_house_app .

2. Run the Docker container:
   docker run -p 5000:5000 chocolate_house_app

## API Endpoints

- **Add Flavor**: `POST /flavors`
- **List Flavors**: `GET /flavors`
- **Add Ingredient**: `POST /inventory`
- **List Ingredients**: `GET /inventory`
- **Add Suggestion**: `POST /suggestions`
- **List Suggestions**: `GET /suggestions`

## Testing
Test the endpoints using Postman or `curl` commands.

