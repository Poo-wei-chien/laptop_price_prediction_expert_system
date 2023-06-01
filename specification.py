import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('df.csv')
df2 = pd.read_csv('laptop_data.csv')
df1['Price'] = df1['Price']*0.056
df2['Price'] = df2['Price']*0.056

def show_specification_page():
    st.title('Laptop Specification Analysis')
    st.sidebar.success('Select a page above')

    #Brand
    st.markdown("## 1.Brand")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['Company'], y=df1['Price'])
    plt.xticks(rotation="vertical")
    plt.xlabel('Company')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by company is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('Razen laptops have the highest average price, followed by LG and MSI. Vero laptops have the lowest average price.')

    #Type of laptop
    st.markdown("## 2.Type of Laptop")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['TypeName'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('Type of Laptop')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by type is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('The average price of laptops by type is shown in the bar chart above. Workstation laptops have the highest average price, followed by Gaming and 2 in 1 Convertible. Netbook laptops have the lowest average price.')

    #Ram
    st.markdown("## 3.RAM")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['Ram'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('Ram (in GB)')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by ram is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('When the RAM increases, the price of the laptop also increases.')

    #Weight
    st.markdown("## 4.Weight")
    plt.figure(figsize=(16, 9))
    sns.scatterplot(x=df1['Weight'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('Weight (in kg)')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by weight is shown in the scatter plot above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('The price of the laptop is not much affected by the weight of the laptop. Also the most distributed weight is 1 kg to 3 kg.')

    #Touchscreen
    st.markdown("## 5.Touchscreen")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['Touchscreen'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('Touchscreen')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by touchscreen is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('Laptops with touchscreen have a higher average price than laptops without touchscreen.')

    #IPS
    st.markdown("## 6.IPS")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['Ips'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('IPS')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by IPS is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('Laptops with IPS have a higher average price than laptops without IPS.')

    #Screen Size
    st.markdown("## 7.Screen Size")
    plt.figure(figsize=(16, 9))
    sns.scatterplot(x=df2['Inches'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('Screen Size (inches)')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by screen size is shown in the scatter plot above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('The price of the laptop is not much affected by the screen size of the laptop. Also the most distributed screen size is 13 inches to 18 inches.')

    #Screen Resolution
    st.markdown("## 8.Screen Resolution")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df2['ScreenResolution'], y=df1['Price'])
    plt.xticks(rotation="vertical")
    plt.xlabel('Screen Resolution')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by screen resolution is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write('Laptops with screen resolution 3840x2160 have a higher average price than laptops with other screen resolutions.')

    #Cpu
    st.markdown("## 9.CPU")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['Cpu_brand'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('CPU')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by CPU is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write("Laptops with CPU Intel Core i7 have a higher average price than laptops with other CPUs.")

    #Gpu
    st.markdown("## 10.GPU")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['Gpu_brand'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('GPU')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by GPU is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write("Laptops with GPU 'Navidia' have a higher average price than laptops with other GPUs.")

    #OS
    st.markdown("## 11.Operating System")
    plt.figure(figsize=(16, 9))
    sns.barplot(x=df1['os'], y=df1['Price'])
    plt.xticks(rotation="horizontal")
    plt.xlabel('OS')
    plt.ylabel('Price (RM)')
    plt.title('Average Price of Laptops by Company')
    st.pyplot(plt)
    text = "The average price of laptops by OS is shown in the bar chart above."
    st.markdown(f"<p style='text-align: center'><em>{text}</em></p>", unsafe_allow_html=True)
    st.write("Laptops with OS 'Mac' have a higher average price than laptops with other OS.")



