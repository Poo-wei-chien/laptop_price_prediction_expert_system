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

def modelTuning(predictedPrice, company,lap_type,ram,touchscreen,ips,cpu,hdd,ssd,gpu,os):
    totalPredictedPrice = predictedPrice
    #Tuning "Company" feature
    if company == 'Apple':
        totalPredictedPrice += predictedPrice * 0.30
    elif company == 'HP':
        totalPredictedPrice += predictedPrice * 0.10
    elif company == 'Acer':
        totalPredictedPrice -= predictedPrice * 0.05
    elif company == 'Asus':
        totalPredictedPrice += predictedPrice * 0.05
    elif company == 'Dell':
        totalPredictedPrice += predictedPrice * 0.20
    elif company == 'Lenovo':
        totalPredictedPrice += predictedPrice * 0.10
    elif company == 'Chuwi':
        totalPredictedPrice -= predictedPrice * 0.15
    elif company == 'MSI':
        totalPredictedPrice += predictedPrice * 0.15
    elif company == 'Microsoft':
        totalPredictedPrice += predictedPrice * 0.20
    elif company == 'Toshiba':
        totalPredictedPrice -= predictedPrice * 0.05
    elif company == 'Huawei':
        totalPredictedPrice -= predictedPrice * 0.10
    elif company == 'Xiaomi':
        totalPredictedPrice -= predictedPrice * 0.10
    elif company == 'Vero':
        totalPredictedPrice -= predictedPrice * 0.15
    elif company == 'Razer':
        totalPredictedPrice += predictedPrice * 0.25
    elif company == 'Mediacom':
        totalPredictedPrice -= predictedPrice * 0.15
    elif company == 'Samsung':
        totalPredictedPrice += predictedPrice * 0.15
    elif company == 'Google':
        totalPredictedPrice += predictedPrice * 0.15
    elif company == 'Fujitsu':
        totalPredictedPrice += predictedPrice * 0.05
    elif company == 'LG':
        totalPredictedPrice += predictedPrice * 0.10

    #Tuning "Type" feature
    if lap_type == 'Netbook':
        totalPredictedPrice -= predictedPrice * 0.10
    elif lap_type == 'Gaming':
        totalPredictedPrice += predictedPrice * 0.20
    elif lap_type == '2 in 1 Convertible':
        totalPredictedPrice += predictedPrice * 0.10
    elif lap_type == 'Workstation':
        totalPredictedPrice += predictedPrice * 0.30

    #Tuning "Ram" feature
    if ram == 4:
        totalPredictedPrice += predictedPrice * 0.10
    elif ram == 6:
        totalPredictedPrice += predictedPrice * 0.30
    elif ram == 8:
        totalPredictedPrice -= predictedPrice * 0.15
    elif ram == 16:
        totalPredictedPrice -= predictedPrice * 0.10
    elif ram == 32:
        totalPredictedPrice += predictedPrice * 0.20
    elif ram == 64:
        totalPredictedPrice += predictedPrice * 0.50
    
    #Tuning "Touchscreen" feature
    if touchscreen == 1:
        totalPredictedPrice += predictedPrice * 0.20

    #Tuning "IPS" feature
    if ips == 1:
        totalPredictedPrice += predictedPrice * 0.15

    #Tuning "CPU" feature
    if cpu == 'Intel Core i7':
        totalPredictedPrice += predictedPrice * 0.25
    elif cpu == 'AMD Processor':
        totalPredictedPrice -= predictedPrice * 0.15
    elif cpu == 'Intel Core i3':
        totalPredictedPrice -= predictedPrice * 0.15

    #Tuning "HDD" feature
    if hdd == 256:
        totalPredictedPrice += predictedPrice * 0.10
    elif hdd == 512:
        totalPredictedPrice += predictedPrice * 0.15
    elif hdd == 1024:
        totalPredictedPrice += predictedPrice * 0.25
    elif hdd == 2048:
        totalPredictedPrice += predictedPrice * 0.30

    #Tuning "SSD" feature
    if ssd == 8:
        totalPredictedPrice -= predictedPrice * 0.40
    elif ssd == 256:
        totalPredictedPrice += predictedPrice * 0.10
    elif ssd == 512:
        totalPredictedPrice += predictedPrice * 0.15
    elif ssd == 1024:
        totalPredictedPrice += predictedPrice * 0.30

    #Tuning "GPU" feature
    if gpu == 'AMD':
        totalPredictedPrice -= predictedPrice * 0.15
    elif gpu == 'Nvidia':
        totalPredictedPrice += predictedPrice * 0.15

    #Tuning "OS" feature
    if os == 'Mac':
        totalPredictedPrice += predictedPrice * 0.15
    elif os == 'Others/No OS/Linux':
        totalPredictedPrice -= predictedPrice * 0.15

    return totalPredictedPrice
    
