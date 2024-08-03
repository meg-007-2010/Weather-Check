import streamlit as st
import requests

# Function to fetch weather data
def get_weather(lat, lon):
    url = f"https://open-weather13.p.rapidapi.com/city/latlon/{lat}/{lon}"
    headers = {
        "x-rapidapi-host": "open-weather13.p.rapidapi.com",
        "x-rapidapi-key": "84bc5cea51msh95f446733c85d37p1cc4a6jsnb8d1b9f0427a"
    }  
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Streamlit App
st.title("Weather Information App")

# Input latitude and longitude
latitude = st.number_input("Enter Latitude", min_value=-90.0, max_value=90.0, value=53.1)
longitude = st.number_input("Enter Longitude", min_value=-180.0, max_value=180.0, value=-0.13)

# Button to fetch weather data
if st.button("Get Weather Info"):
    querystring = {"q": f"{latitude},{longitude}"}
    weather_data = get_weather(latitude, latitude)
    print(weather_data)   
    st.json(weather_data)


    # Display weather information
    # st.subheader("Location Information:")
    # st.write(f"City: {weather_data['location']['name']}")
    # st.write(f"Region: {weather_data['location']['region']}")
    # st.write(f"Country: {weather_data['location']['country']}")
    # st.subheader("Current Weather:")
    # st.write(f"Temperature: {weather_data['current']['temp_c']}°C")
    # st.write(f"Condition: {weather_data['current']['condition']['text']}")
    # st.write(f"Wind Speed: {weather_data['current']['wind_kph']} kph")
    # st.write(f"Humidity: {weather_data['current']['humidity']}%")
    # st.subheader("Last Updated:")
    # st.write(f"{weather_data['current']['last_updated']}")