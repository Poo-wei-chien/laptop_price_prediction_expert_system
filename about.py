import streamlit as st
from PIL import Image


def show_about_page():
    st.title('About Us')
    st.sidebar.success('Select a page above')

    # Add your about page content here

    text1 = """The **Laptop Price Prediction Expert System** is a cutting-edge solution developed for companies from any industry to accurately forecast the costs associated with procuring laptops for organizational use. By leveraging knowledge and a comprehensive dataset provided and suggested by our collaborator, this expert system empowers businesses to make informed decisions regarding laptop purchases, optimizing their budget allocation and ensuring efficient procurement strategies."""

    text2= """The system's architecture utilizes predictive modeling techniques and expert knowledge to analyze various laptop attributes such as brand, processor type, memory, screen size, and other relevant specifications. By training on historical data, the expert system has acquired the ability to recognize patterns and correlations between these attributes and the corresponding prices, enabling it to generate reliable price predictions for new laptop models."""

    text3 = """We aim to propose an expert system that will be developed using a rule-based approach, where a set of rules will be created based on the analysis of historical laptop prices and their corresponding specifications. The system will use these rules to generate predictions based on the input specifications of a laptop. The system will be trained using a large dataset of historical laptop prices and specifications."""

    text4 = """User-friendliness and accessibility are integral aspects of our expert system. We aim to design a user-friendly interface that allows users to input laptop specifications and receive accurate price predictions. Even users with limited technical skills or prior experience will be able to easily utilize the system."""

    text5 = """In summary, our expert system serves as a valuable tool for estimating laptop prices, benefiting both larger companies and individuals seeking to make cost-effective purchases. By providing accurate price estimates and enabling users to compare them with market prices, our system empowers users to make informed decisions, ultimately saving money."""

    st.write(text1)
    st.write(text2)
    st.write(text3)
    st.write(text4)
    st.write(text5)


    image = Image.open('about.jpg')
    st.image(image, caption='Credit to: Winnie The Poo Team')