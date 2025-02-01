hasher = {
    "N": "S",
    "E": "W",
    "W": "E",
    "S": "N",
    "NE": "SW",
    "NW": "SE",
    "SE": "NW",
    "SW": "NE"
}
entrada = input()
if hasher.get(entrada):
    print(hasher[entrada])