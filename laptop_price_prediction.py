import pandas as pd
from sklearn.preprocessing import LabelEncoder

dfmodel = pd.read_csv('laptop-clean-train.csv')
dfmodel['screen size'] = dfmodel['screen size'].str.replace('"', '')

# Initialize the label encoder
cat_cols =  ['manufacturer', 'category', 'cpu', 'gpu', 'operating system',
            'resolution', 'screen_type', 'storage_1_type', 'storage_2_type',
            'gpu_brand', 'cpu_brand']

#One hot encoding
print('Dataframe encoded by OHE dimension : ', pd.get_dummies(dfmodel, columns = cat_cols, drop_first = True).shape)

#Label encoding
en = LabelEncoder()

for cols in cat_cols:
    dfmodel[cols] = en.fit_transform(dfmodel[cols])


x_train = dfmodel.drop('price', axis=1)
x_train = x_train.drop('operating system version', axis=1)
x_train = x_train.drop('model name', axis=1)
x_train = x_train.drop('cpu_freq(GHz)', axis=1)
y_train = dfmodel['price']


def predict_laptop_price_model(data_input):
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score

    # Create an instance of LinearRegression
    model = LinearRegression()

    # Fit the model on the training data
    model.fit(x_train, y_train)

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
    predicted_price[0] = round(predicted_price[0] * 0.0054767, 2)

    if predicted_price[0] < 0:
        predicted_price[0] = predicted_price[0] * -1    
    
    return predicted_price[0]