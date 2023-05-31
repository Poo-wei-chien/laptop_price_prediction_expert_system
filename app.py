from PIL import Image
import streamlit as st
import regex as re
import time
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from laptop_price_prediction import modelTuning, predict_laptop_price
import about
import pandas as pd

#Set up Page Config
img = Image.open('icon.png')
st.set_page_config(
    page_title="Laptop Price Prediction Expert System",
    page_icon = img,
    layout="centered",
    initial_sidebar_state="expanded",
)

if "balloons_triggered" not in st.session_state:
    st.session_state.balloons_triggered = False

if not st.session_state.balloons_triggered:
    st.balloons()
    st.session_state.balloons_triggered = True

# Page selection
pages = ['Home', 'About']
selected_page = st.sidebar.selectbox('Select Page', pages)

# Display the selected page content
if selected_page == 'Home':
    # Home page content
    st.title('Laptop Price Prediction Expert System :computer:')
    st.caption('Predict the prices of laptops using different features and specifications :sunglasses:')
    st.sidebar.success('Select a page above')
    st.divider()

    st.text('Enter the features of the laptop to get the price prediction \U0001F447')

    # Get the user inputs
    df = pd.read_csv('df.csv')
    #Brand
    company = st.selectbox('Brand', df['Company'].unique())
    #Type of laptop
    lap_type = st.selectbox("Type", df['TypeName'].unique())
    #Ram
    ram = st.selectbox("Ram (in GB)", [2,4,6,8,12,16,24,32,64])
    #weight
    weight = st.number_input("Weight of the Laptop", min_value=0.5, max_value=5.00, step=0.01)
    #Touch screen
    touchscreen = st.selectbox("TouchScreen", ['No', 'Yes'])
    #IPS
    ips = st.selectbox("IPS (In-Plane Switching) monitor ", ['No', 'Yes'])
    #screen size
    screen_size = st.number_input('Screen Size', min_value=10.0, max_value=20.0, step=0.1,format="%.1f")
    # resolution
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
    #cpu
    cpu = st.selectbox('CPU',df['Cpu_brand'].unique())
    hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048])
    ssd = st.selectbox('SSD (in GB)',[0,8,128,256,512,1024])
    gpu = st.selectbox('GPU',df['Gpu_brand'].unique())
    os = st.selectbox('OS',df['os'].unique())

    if st.button('SUBMIT'):
        with st.spinner('Wait for it...'):
            time.sleep(0.1)
        if(hdd == 0 and ssd == 0):
            st.error('Please enter the HDD, SSD or both of the laptop')
            st.stop()
        elif(company == 'Apple' and os != 'Mac'):
            st.error('Please enter the OS as macOS for Apple laptops')
            st.stop()
        elif(company != 'Apple' and os == 'Mac'):
            st.error('Please enter the OS as Windows, Linux or others for non-Apple laptops')
            st.stop()
        else:
            #Prediction
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
            prediction = modelTuning(prediction, company,lap_type,ram,touchscreen,ips,cpu,hdd,ssd,gpu,os)
            st.title("The predicted price of this configuration is RM " + str(prediction))
            

if selected_page == 'About':
    # About page content
    about.show_about_page()






