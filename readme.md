# Overview

Ho sviluppato un server espone degli endpoint attraverso FastAPI per un'ipotetica pagina di e-commerce.Questo rappresentato soltanto un piccolo esempio, ho messo a disposizione alcune funzionalità base come la ricerca, aggiunta al carrello, la rimozione di un articolo o di tutti all'interno del carrello dell'utente.
Le tecnologie che ho deciso di impiegare sono:
- FastAPI per esporre gli endpoints
- Postgres come database
- Docker come ambiente virtualizzato per far girare entrambi
- SqlAlchemy come interfaccia con il database

# Endpoint description

- Endpoint 1 - Ricerca. Funzionalità di ricerca dei prodotti disponibili mediante una query testuale.
Route: "/search" 
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


- Endpoint 2 - Aggiunta prodotto al carrello dell'utente.
Route: "/add_product"
Input: {"user_id" : "ad5ce827-4a17-4b74-9693-53a2b74f177c", "product_id" : "9e94e4ac-4a33-4945-b4aa-cd10f84e6351", "quantity" : 1}
Output: {"added": true}


- Endpoint 3 - Dettagli prodotto. Funzionalità che restituisce dato un codice i dettagli del prodotto con dato codice.
Route: "/product_details"
Input: {"product_id" : "66373dbe-edcd-41c4-9d29-61f641068312"}
Output: 
{
    "product_name": "Scarf",
    "product_description": "Woolen",
    "product_price": 23.0
}


- Endpoint 4 - Rimozione quantità specifica di un prodotto dal carrello di uno specifico utente.
Route: "/product_removal_quantity"
Input: {"user_id" : "ad5ce927-4a17-4b74-9693-53a2b74f177c", "product_id" : "9e94e4ac-4a33-4945-b4aa-cd10f84e6351", "quantity" : "2"}
Output:
{
    "removed": true
}

- Endpoint 5 - Rimozione di tutti gli elementi nel carrello
Route: "/product_removal_all"
Input: {"user_id": "ad5ce927-4a17-4b74-9693-53a2b74f177c"}
Output:
{
    "removed": true
}

# Local run steps

1) Run docker for postgres (docker-compose -up)
2) Execute the script to populate the database with the sample data
3) docker for API-server (docker qualcosa)

