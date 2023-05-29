import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

def predict_laptop_price_model(data_input):

    # Open the file
    model = pickle.load(open('laptop_price_prediction_model.pkl', 'rb'))

    # Make prediction
    return model.predict(data_input)

label_encoder = LabelEncoder()

def predict_laptop_price(manufacturer, category, screen_size, cpu, ram, gpu, operating_system, weight, resolution, screen_type, touchscreen, storage_1_gb, storage_1_type, storage_2_gb, storage_2_type, cpu_brand, gpu_brand):
    # Create a dictionary with the laptop characteristics
    laptop = {
        'manufacturer': [manufacturer],
        'category': [category],
        'screen size': [screen_size],
        'cpu': [cpu],
        'ram(GB)': [ram],
        'gpu': [gpu],
        'operating system': [operating_system],
        'weight(kg)': [weight],
        'resolution': [resolution],
        'screen_type': [screen_type],
        'touchscreen': [touchscreen],
        'storage_1_gb': [storage_1_gb],
        'storage_1_type': [storage_1_type],
        'storage_2_gb': [storage_2_gb],
        'storage_2_type': [storage_2_type],
        'cpu_brand': [cpu_brand],
        'gpu_brand': [gpu_brand]
    }
    
    # Create a DataFrame from the laptop dictionary
    df = pd.DataFrame(laptop)
    
    # Encode categorical columns using the label encoder
    categorical_cols =  ['manufacturer', 'category', 'cpu', 'gpu', 'operating system',
                'resolution', 'screen_type', 'storage_1_type', 'storage_2_type',
                'gpu_brand', 'cpu_brand']
    
    for col in categorical_cols:
        df[col] = label_encoder.fit_transform(df[col])
    
    # Make the price prediction using the trained model
    predicted_price = predict_laptop_price_model(df.values)

    # Change INR to MYR
    predicted_price[0] = round(predicted_price[0] * 0.056, 2)

    if predicted_price[0] < 0:
        predicted_price[0] = predicted_price[0] * -1    
    
    return predicted_price[0]