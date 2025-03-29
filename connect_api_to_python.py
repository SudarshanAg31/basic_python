import requests
base_url="https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    
    if response.status_code==200:#200 code is for oky and 404 is an error
        pokemon_info=response.json()
        return pokemon_info
name_pokemon=input("enter name of pokemon:-")
pokemon_info=get_pokemon_info(name_pokemon)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Weight: {pokemon_info["weight"]} kg")
    print(f"Height: {pokemon_info["height"]} ft")
    
    