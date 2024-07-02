import requests

r1 = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")


p1  = r1.json()


print(f"Name: {p1["name"]}, Ability 1: {p1["abilities"][0]["ability"]["name"]}, Ability 2: {p1["abilities"][1]["ability"]["name"]}")



def pokefunction():

    pokemon1 = input("Enter a pokemon ").lower()
    pokemon2 = input("Enter another pokemon ").lower()
    pokemon3 = input("Enter final pokemon ").lower()

    print()


    response1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon1}")
    response2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon2}")
    response3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon3}")

    p1 = response1.json()
    p2 = response2.json()
    p3 = response3.json()

#   ----------------------------------------------------------------------------------

    print("-" * 50) 
    print(f"{p1["name"].upper()}:")
    print(len(p1["name"]) * "~")
    print()                                                                                   #~~~~~~~~~~
    counter = 0                                                                               # Pokemon 1
    for abilities in p1["abilities"]:                                                         #~~~~~~~~~~
        
        print(f"Ability {counter +1} - {p1["abilities"][counter]["ability"]["name"]}")
        counter += 1
    print(f"Weight - {p1["weight"]/10} kg")
    w1 = p1["weight"]

#   ----------------------------------------------------------------------------------

    print("-" * 50) 
    print(f"{p2["name"].upper()}:")
    print(len(p2["name"]) * "~")
    print()                                                                                   #~~~~~~~~~~
    counter = 0                                                                               # Pokemon 2                              
    for abilities in p2["abilities"]:                                                         #~~~~~~~~~~
    
        print(f"Ability {counter +1} - {p2["abilities"][counter]["ability"]["name"]}")
        counter += 1
    print(f"Weight - {p2["weight"]/10} kg")
    w2 = p2["weight"]

#   ----------------------------------------------------------------------------------

    print("-" * 50)  
    print(f"{p3["name"].upper()}:")
    print(len(p3["name"]) * "~")
    print()                                                                                   #~~~~~~~~~~
    counter = 0                                                                               # Pokemon 3
    for abilities in p3["abilities"]:                                                         #~~~~~~~~~~
    
        print(f"Ability {counter +1} - {p3["abilities"][counter]["ability"]["name"]}")
        counter += 1
    print(f"Weight - {p3["weight"]/10} kg")
    print("-" * 50) 
    w3 = p3["weight"]

#   ----------------------------------------------------------------------------------

    print()
    average = ((w1+w2+w3) / 3) / 10        # API lists weight as an integer, but is a float in the pokedex. So, I have divided the average by 10 to get the actual number in kilograms.

    print(f"Average weight of {p1["name"].title()}, {p2["name"].title()}, and {p3["name"].title()}: {average} kilograms")
    print()

pokefunction()