import streamlit as st
import pickle

# Load the pickle file containing the trained model
with open('rain_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the streamlit app
if __name__ == '__main__':
    st.title('Rain Prediction App')

    # Create an input form for user inputs
    st.header('Enter Input Features')
    st.sidebar.header('Country Labels')
    st.sidebar.text('''London : 0 
Paris : 1 
New York : 2 
Tokyo : 3 
Beijing : 4 
Istanbul : 5 
Moscow : 6 
Berlin : 7 
Bangkok : 8 
Seoul : 9 
Mumbai : 10 
Rome : 11 
Madrid : 12 
Mexico City : 13 
Shanghai : 14 
Rio de Janeiro : 15
Los Angeles : 16 
Buenos Aires : 17  
Sydney : 18 
Johannesburg : 19''')
    options = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    Location = st.selectbox('Select a Location', options)
    Min_Temperature = st.slider('Min Temperature today (C)', -20.00, 40.00, 0.00)
    Max_Temperature = st.slider('Max Temperature today (C)', -20.00, 40.00, 0.00)
    Wind_Direction = st.slider('Wind Direction in Degrees (°) --> 0° - blowing from the north, 90° - blowing from the east, 180° - blowing from the south, 270° - blowing from the west', 0, 360, 180)
    Wind_Speed = st.slider('Wind Speed (m/s)', 0.00, 13.00, 0.00)
    Humidity = st.slider('Humidity (%)', 7, 100, 50)
    Pressure = st.slider('Pressure (hPa)', 1000, 1036, 1000)
    Cloud = st.slider('Cloud (%)', 0, 100, 50)
    Temperature = st.slider('Present Temperature (C)', -20.00, 40.00, 0.00)
    opt = [0,1]
    Rain = st.selectbox('Is it raining today (0 - No, 1 - Yes)', opt)

    # Use the loaded model to make predictions
    features = [[Location, Min_Temperature, Max_Temperature, Wind_Direction, Wind_Speed, Humidity, Pressure, Cloud, Temperature, Rain]]
    prediction = model.predict(features)

    # Display the prediction results to the user
    st.write('Prediction : ', prediction[0])
    if (prediction[0]==1):
        st.header("Yes, it'll rain tomorrow")
    else:
        st.header("No, it'll not rain tomorrow")
