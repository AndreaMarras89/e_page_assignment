
# Overview

I have developed a server that exposes endpoints through FastAPI for a hypothetical e-commerce page. This is just a small example, I have made some basic features available such as search, adding to cart, removing an item or all of them inside the user's shopping cart.
The technologies I decided to use are:
- FastAPI to expose endpoints
- Postgres as database
- Docker as a virtualized environment to run both
- SqlAlchemy as an interface with the database

# Endpoint description

## Endpoint 1 - Research. Product search functionality available via a text query.
```bash
Route: 
"/search"
``` 
Input: {"query" : "Scarf"}
Output: 
{
    "products": [
        {
            "id": "9e94e4ac-4a33-4945-b4aa-cd10f84e6351",
            "name": "Scarf",
            "price": 23.0,
            "description": "Woolen scarf"
        }
    ]
}


## Endpoint 2 - Adding a product to the User's cart
Route: "/add_product"
Input: {"user_id" : "ad5ce827-4a17-4b74-9693-53a2b74f177c", "product_id" : "9e94e4ac-4a33-4945-b4aa-cd10f84e6351", "quantity" : 1}
Output: {"added": true}


## Endpoint 3 - Getting details of a product given the product id
Route: "/product_details"
Input: {"product_id" : "66373dbe-edcd-41c4-9d29-61f641068312"}
Output: 
{
    "product_name": "Scarf",
    "product_description": "Woolen",
    "product_price": 23.0
}


## Endpoint 4 - Removing a specific quantity of a product from a specific user's cart.
Route: "/product_removal_quantity"
Input: {"user_id" : "ad5ce927-4a17-4b74-9693-53a2b74f177c", "product_id" : "9e94e4ac-4a33-4945-b4aa-cd10f84e6351", "quantity" : "2"}
Output:
{
    "removed": true
}

## Endpoint 5 - Removal all items in the user's cart
Route: "/product_removal_all"
Input: {"user_id": "ad5ce927-4a17-4b74-9693-53a2b74f177c"}
Output:
{
    "removed": true
}

# Local run steps

1) Run docker for postgres and fastAPI (docker-compose -up)
2) Execute the script to populate the database with the sample data (psql -h <IP_DATABASE> -p <PORT_DATABASE> -d postgres -U user < dump_file.sql)

