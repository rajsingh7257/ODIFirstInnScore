import pickle

import pandas as pd
import streamlit as st

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['West Indies',
 'Pakistan',
 'Bangladesh',
 'Australia',
 'England',
 'Sri Lanka',
 'India',
 'New Zealand',
 'Zimbabwe',
 'South Africa']

cities = ['Mirpur',
 'Colombo',
 'London',
 'Harare',
 'Sydney',
 'Rangiri',
 'Abu Dhabi',
 'Melbourne',
 'Centurion',
 'Bulawayo',
 'Adelaide',
 'Johannesburg',
 'Dubai',
 'Perth',
 'Brisbane',
 'Auckland',
 'Pallekele',
 'Wellington',
 'Birmingham',
 'Durban',
 'Port Elizabeth',
 'Nottingham',
 'Cape Town',
 'Manchester',
 'Trinidad',
 'Antigua',
 'Hambantota',
 'Karachi',
 'Hamilton',
 'Southampton',
 'Jamaica',
 'Chandigarh',
 'Cardiff',
 'Napier',
 'Sharjah',
 'Christchurch',
 'Guyana',
 'St Lucia',
 'Mumbai',
 'Leeds',
 'St Kitts',
 'Chester-le-Street',
 'Ahmedabad',
 'Lahore',
 'Chittagong',
 'Barbados',
 'Grenada',
 'Hobart',
 'Dhaka',
 'Jaipur',
 'Chennai',
 'Mount Maunganui',
 'Nagpur',
 'Delhi',
 'Bloemfontein',
 'Visakhapatnam',
 'St Vincent',
 'Dunedin',
 'Rajkot',
 'Hyderabad',
 'Kanpur',
 'Potchefstroom',
 'Fatullah',
 'Bristol',
 'Kuala Lumpur',
 'Kolkata',
 'Nelson',
 'Indore',
 'Canberra',
 'Rawalpindi',
 'Multan']

st.title("ODI Score Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team",sorted(teams))

with col2:
    bowling_team = st.selectbox("Select Bowling Team",sorted(teams))

city = st.selectbox("Select City",sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input("Current Score")
with col4:
    overs = st.number_input("Overs Completed (overs>5)")
with col5:
    wickets = st.number_input("Wickets Fallen")

last_five = st.number_input("Score in last 5 Overs")

if st.button ("Predict Score"):
    balls_left = 300 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],
                             'current_score':[current_score],'balls_left':[balls_left],'wickets_left':[wickets_left],'crr':[crr],'last_five':[last_five]})

    result = pipe.predict(input_df)

    st.text(str(int(result)))


