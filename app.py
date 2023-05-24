from PIL import Image
import streamlit as st
import regex as re
import time
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from laptop_price_prediction import predict_laptop_price
import about

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
    manufacturer_options = ['None', 'Acer', 'Apple', 'Asus', 'Chuwi', 'Dell', 'Fujitsu', 'HP', 'Lenovo', 'LG', 'Mediacom', 'MSI', 'Razer', 'Samsung', 'Toshiba', 'Vero', 'Xiaomi']
    sorted_manufacturer_options = sorted(manufacturer_options[1:])
    manufacturer_options_with_other = sorted_manufacturer_options + ['Other'] 
    manufacturer = st.selectbox('Manufacturer*', ['None'] + manufacturer_options_with_other, index=0)

    if manufacturer == 'Other':
        manufacturer = st.text_input('Enter the manufacturer of the laptop')

    category_options = ['None', '2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']
    sorted_category_options = sorted(category_options[1:])
    category_options_with_other = sorted_category_options + ['Other']
    category = st.selectbox('Category*', ['None'] + category_options_with_other, index=0)

    if category == 'Other':
        category = st.text_input('Enter the category of the laptop')

    screen_size = st.number_input('Screen Size (inches)', min_value=10.0, max_value=20.0, value=15.0, step=0.1, format="%.1f")

    ram = st.selectbox('RAM (GB)*', [2, 4, 6, 8, 12, 16, 24, 32, 64, 128], index=0)

    cpu_options = ['None', 'AMD A6-Series 9220', 'AMD A8-Series 7410', 'AMD A9-Series 9420', 'AMD A10-Series 9600P', 'AMD A10-Series A10-9620P', 'AMD E-Series 6110', 'Intel Atom x5-Z8350', 'Intel Celeron Dual Core 3205U', 'Intel Celeron Dual Core N3050', 'Intel Celeron Dual Core N3060', 'Intel Celeron Dual Core N3350', 'Intel Celeron Dual Core 3855U', 'Intel Celeron Quad Core N3160', 'Intel Celeron Quad Core N3450', 'Intel Core i3 6006U', 'Intel Core i3 6100U', 'Intel Core i3 7100U', 'Intel Core i3 7130U', 'Intel Core i5 6200U', 'Intel Core i5 6300HQ', 'Intel Core i5 6300U', 'Intel Core i5 7200U', 'Intel Core i5 7300HQ', 'Intel Core i5 7300U', 'Intel Core i5 8250U', 'Intel Core i5', 'Intel Core i7 6500U', 'Intel Core i7 6600U', 'Intel Core i7 6700HQ', 'Intel Core i7 6820HK', 'Intel Core i7 6820HQ', 'Intel Core i7 7500U', 'Intel Core i7 7600U', 'Intel Core i7 7700HQ', 'Intel Core i7 7820HK', 'Intel Core i7 7820HQ', 'Intel Core i7 8550U', 'Intel Core i7 8650U', 'Intel Core i7 7Y75', 'Intel Core i7 8550U', 'Intel Core M 6Y75', 'Intel Pentium Quad Core N3700', 'Intel Pentium Quad Core N3710', 'Intel Pentium Quad Core N4200', 'Intel Xeon E3-1505M V6', 'AMD Ryzen 1700']
    sorted_cpu_options = sorted(cpu_options[1:])
    category_options_with_other = sorted_cpu_options + ['Other']
    cpu = st.selectbox('CPU*', ['None'] + category_options_with_other, index=0)

    if cpu == 'Other':
        cpu = st.text_input('Enter the CPU of the laptop')

    gpu_options = ['None', 'AMD Radeon R2', 'AMD Radeon R2 Graphics', 'AMD Radeon R4', 'AMD Radeon R4 Graphics', 'AMD Radeon R5', 'AMD Radeon R5 M330', 'AMD Radeon R5 M420', 'AMD Radeon R5 M420X', 'AMD Radeon R7 M445', 'AMD Radeon 520', 'AMD Radeon 530', 'AMD A12-Series 9720P', 'Nvidia GeForce 920M', 'Nvidia GeForce 920MX', 'Nvidia GeForce 930M', 'Nvidia GeForce 930MX', 'Nvidia GeForce 940MX', 'Nvidia GeForce GTX 950M', 'Nvidia GeForce GTX 960M', 'Nvidia GeForce GTX 970M', 'Nvidia GeForce GTX 980M', 'Nvidia GeForce GTX 1050', 'Nvidia GeForce GTX 1050M', 'Nvidia GeForce GTX 1050 Ti', 'Nvidia GeForce GTX 1060', 'Nvidia GeForce GTX 1070', 'Nvidia Quadro M1000M', 'Nvidia Quadro M1200', 'Nvidia Quadro M2200M', 'Nvidia Quadro M520M', 'AMD Radeon RX 580', 'Intel HD Graphics', 'Intel HD Graphics 400', 'Intel HD Graphics 405', 'Intel HD Graphics 500', 'Intel HD Graphics 505', 'Intel HD Graphics 510', 'Intel HD Graphics 515', 'Intel HD Graphics 520', 'Intel HD Graphics 6000', 'Intel HD Graphics 615', 'Intel HD Graphics 620', 'Intel HD Graphics 630', 'Intel Iris Plus Graphics 640', 'Intel UHD Graphics 620']
    sorted_gpu_options = sorted(gpu_options[1:])
    gpu_options_with_other = sorted_gpu_options + ['Other']
    gpu = st.selectbox('GPU*', ['None'] + gpu_options_with_other, index=0)

    if gpu == 'Other':
        gpu = st.text_input('Enter the GPU of the laptop')

    os_options = ['None', 'Chrome OS', 'Linux', 'macOS', 'No OS', 'Windows']
    sorted_os_options = sorted(os_options[1:])
    os_options_with_other = sorted_os_options + ['Other'] 
    os = st.selectbox('Operating System*', ['None'] + os_options_with_other, index=0)

    if os == 'Other':
        os = st.text_input('Enter the operating system of the laptop')

    kg = st.number_input('Weight (kg)', min_value=0.0, max_value=10.0, value=2.0, step=0.1)

    resolution_options = ['None', '1920x1080', '1366x768', '3840x2160', '2560x1440', '3200x1800', '1600x900', '1440x900', '2560x1600', '1920x1200']
    sorted_resolution_options = sorted(resolution_options[1:])
    resolution_options_with_other = sorted_resolution_options + ['Other']
    resolution = st.selectbox('Resolution*', ['None'] + resolution_options_with_other, index=0)

    if resolution == 'Other':
        resolution = st.text_input('Enter the resolution of the laptop')

    screen_type_options = ['None', 'IPSPanel', 'IPSPanelRetinaDisplay']
    sorted_screen_type_options = sorted(screen_type_options[1:])
    screen_type_options_with_other = sorted_screen_type_options + ['Other']
    screen_type = st.selectbox('Screen Type', ['None'] + screen_type_options_with_other, index=0)

    if screen_type == 'Other':
        screen_type = st.text_input('Enter the screen type of the laptop')

    touchscreen = st.selectbox('Touchscreen', ['None', 'Touchscreen'], index=0)

    storage_1_options = ['None', '32GB SSD', '64GB FlashStorage', '128GB SSD', '256GB SSD', '512GB NVMe', '1TB HDD', '2TB HDD']
    sorted_storage_1_options = sorted(storage_1_options[1:])
    storage_1_options_with_other = sorted_storage_1_options + ['Other']
    storage_1 = st.selectbox('Storage 1*', ['None'] + sorted_storage_1_options, index=0)

    if storage_1 == 'Other':
        storage_1 = st.text_input('Enter the storage 1 of the laptop')

    storage_2_options = ['None', '128GB SSD', '256GB SSD', '512GB SSD', '1TB HDD', '2TB HDD']
    sorted_storage_2_options = sorted(storage_2_options[1:])
    storage_2_options_with_other = sorted_storage_2_options + ['Other']
    storage_2 = st.selectbox('Storage 2', ['None'] + storage_1_options_with_other, index=0)

    if storage_2 == 'Other':
        storage_2 = st.text_input('Enter the storage 2 of the laptop')


    if st.button('SUBMIT'):
        with st.spinner('Wait for it...'):
            time.sleep(2)
        
        if manufacturer != "None" and category != "None" and cpu != "None" and gpu != "None" and os != "None" and resolution != "None" and storage_1 != "None":
            # Proceed with the submission
            # Filter the data based on the user inputs
            if screen_size != "None":
                screen_size = float(screen_size)
                screen_size = round(screen_size, 1)

            if kg != "None":
                kg = float(kg)
                kg = round(kg, 1)

            if storage_1 != "None":
                storage_1_type = re.findall(r'(\D+)', storage_1)[0].strip()
                storage_1_gb = re.findall(r'(\d+)', storage_1)[0]
                if "TB" in storage_1:
                    storage_1_gb = int(storage_1_gb) * 1000  # Convert TB to GB
                storage_1_type = storage_1_type.replace("GB", "")  # Remove "GB"
                storage_1_type = storage_1_type.replace("TB", "")  # Remove "GB"
            else:
                storage_1_type = 'NaN'
                storage_1_gb = 0.0

            if storage_2 != "None":
                storage_2_type = re.findall(r'(\D+)', storage_2)[0].strip()
                storage_2_gb = re.findall(r'(\d+)', storage_2)[0]
                if "TB" in storage_2:
                    storage_2_gb = int(storage_2_gb) * 1000  # Convert TB to GB
                storage_2_type = storage_2_type.replace("GB", "")  # Remove "GB"
            else:
                storage_2_type = 'NaN'
                storage_2_gb = 0.0

            if cpu != "None":
                cpu_brand = re.findall(r'^(\w+)', cpu)[0]
                cpu = re.findall(r'^(\w+)\s?(.*)', cpu)[0][1]
            else:
                cpu_brand = 'NaN'

            if gpu != "None":
                gpu_brand = re.findall(r'^(\w+)', gpu)[0]
                gpu = re.findall(r'^(\w+)\s?(.*)', gpu)[0][1]
            else:
                gpu_brand = 'NaN'

            if touchscreen != "None":
                touchscreen = 1
            else:
                touchscreen = 0

            if screen_type == "None":
                screen_type = 'NaN'

            #Predict the price of the laptop
            laptop_info = (manufacturer, category, screen_size, cpu, ram, gpu, os, kg, resolution, screen_type,touchscreen, storage_1_gb, storage_1_type, storage_2_gb, storage_2_type, cpu_brand, gpu_brand)
            predicted_price = predict_laptop_price(*laptop_info)
            
            col1, col2, col3 = st.columns(3)
            col2.metric("Predicted Price: ", f"RM {predicted_price:.2f}")
        else:
            st.warning("Please enter all the features of the laptop to get the price prediction. '*' cannot be 'None'.")


if selected_page == 'About':
    # About page content
    about.show_about_page()






