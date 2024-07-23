def transform_data(data):
    transformed_data = []
    for row in data:
        transformed_row = {
            'code_postal': row['code_postal'],
            'nom_commune_complet': row['nom_commune_complet'].upper()  # Mettre en majuscules
        }
        transformed_data.append(transformed_row)
    return transformed_data
