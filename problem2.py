import requests

def getplanets():

    response = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
    bodies = response.json()["bodies"]
    for body in bodies:
        if not body["isPlanet"]:
            continue
        elif body["isPlanet"]:
            name = body["englishName"]
            mass = body["mass"]["massValue"]
            orbit = body["sideralOrbit"]
            print("-" * 50)
            print(name.upper())
            print("~" * len(name))
            print()
            print(f"- Mass: {mass}")
            print(f"- Orbit: {orbit}")
            print()
            
            

def heaviestplanet():

    response = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
    bodies = response.json()["bodies"]

    counter = 0.0
    planet = []
    for body in bodies:
        if body["mass"] is not None:
            a = body["mass"]["massValue"]

            if a > counter:
                counter = a
                planet.clear()
                planet.append(body["englishName"])
                planet.append(a)

            else:
                continue

    print(planet)
    return planet

heaviestplanet()