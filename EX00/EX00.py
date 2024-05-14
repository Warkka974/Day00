def mile_to_km(distance_miles):
    # Conversion de miles en kilomètres
    distance_km = distance_miles * 1.60934
    return distance_km

# Demande à l'utilisateur la distance en miles
distance_miles = float(input("Entrez la distance en miles : "))

# Appelle la fonction et stocke le résultat dans une variable
distance_km = mile_to_km(distance_miles)

# Affiche le résultat
print(f"{distance_miles} miles équivaut à {distance_km} kilomètres.")
