from sklearn.calibration import LabelEncoder
import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title("Laptop Price Predictor")

#Now we will take user input one by one as per our dataframe

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


#Front end
df = pd.read_csv('df.csv')
#company = st.selectbox('Brand', df['Company'].unique())
company = st.selectbox('Brand', df['Company'].unique())
#Type of laptop
lap_type = st.selectbox("Type", df['TypeName'].unique())

#Ram
ram = st.selectbox("Ram(in GB)", [2,4,6,8,12,16,24,32,64])
#weight
weight = st.number_input("Weight of the Laptop")
#Touch screen
touchscreen = st.selectbox("TouchScreen", ['No', 'Yes'])
#IPS
ips = st.selectbox("IPS", ['No', 'Yes'])
#screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',df['Cpu_brand'].unique())
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
gpu = st.selectbox('GPU',df['Gpu_brand'].unique())
os = st.selectbox('OS',df['os'].unique())

#Prediction
if st.button('Predict Price'):
    ppi = None
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0
        
    if ips == "Yes":
        ips = 1
    else:
        ips = 0
        
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res**2)) ** 0.5 / screen_size
    prediction = predict_laptop_price(company,lap_type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os)
    st.title("The predicted price of this configuration is " + str(prediction))
    

