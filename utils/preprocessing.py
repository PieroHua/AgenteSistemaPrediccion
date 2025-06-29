def preprocess_input_data(data):
    """Preprocesar los datos de entrada para el modelo"""
    health_mapping = {
        'Excelente': 5, 'Muy Buena': 4, 'Buena': 3, 'Regular': 2, 'Mala': 1
    }
    smoker_mapping = {
        'Nunca fumó': 0, 'Ex-fumador': 1, 'Fumador ocasional': 2, 'Fumador frecuente': 3
    }
    age_mapping = {
        '18-24': 1, '25-29': 2, '30-34': 3, '35-39': 4, '40-44': 5,
        '45-49': 6, '50-54': 7, '55-59': 8, '60-64': 9, '65-69': 10,
        '70-74': 11, '75-79': 12, '80+': 13
    }

    processed_data = data.copy()
    if 'GeneralHealth' in processed_data.columns:
        processed_data['GeneralHealth'] = processed_data['GeneralHealth'].map(health_mapping)
    if 'SmokerStatus' in processed_data.columns:
        processed_data['SmokerStatus'] = processed_data['SmokerStatus'].map(smoker_mapping)
    if 'AgeCategory' in processed_data.columns:
        processed_data['AgeCategory'] = processed_data['AgeCategory'].map(age_mapping)

    return processed_data
