import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

def predict_laptop_price_model(data_input):

    #load the model and dataframe
    pipe = pickle.load(open("laptop_price_model.pkl", "rb"))

    # Make prediction
    return pipe.predict(data_input)

label_encoder = LabelEncoder()

def predict_laptop_price(company,lap_type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os):
    # Create a dictionary with the laptop characteristics
    laptop = {
        'Company': [company],
        'TypeName': [lap_type],
        'Ram': [ram],
        'Weight': [weight],
        'Touchscreen': [touchscreen],
        'Ips': [ips],
        'ppi': [ppi],
        'Cpu_brand': [cpu],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu_brand': [gpu],
        'os': [os]
    }
    
    # Create a DataFrame from the laptop dictionary
    df = pd.DataFrame(laptop)
    
    # Encode categorical columns using the label encoder
    categorical_cols =  ['Company', 'TypeName', 'Cpu_brand', 'Gpu_brand', 'os']
    
    for col in categorical_cols:
        df[col] = label_encoder.fit_transform(df[col])
    
    # Make the price prediction using the trained model
    predicted_price = predict_laptop_price_model(df.values)

    # Change INR to MYR
    predicted_price[0] = round(predicted_price[0] * 0.056, 2)

    return predicted_price[0]