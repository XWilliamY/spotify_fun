import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

left_column, right_column = st.columns(2)
left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
    )
    st.write(f"You are in {chosen} house!")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
st.metric(label="Skill", value="10%", delta="1 %")

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

# spotify geolocation? Where do you listen to your music?
# but apply doesn't track location data
# how about when you're likely to play music? And when do you pay certain music?


# st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None)

