import streamlit
import pandas

streamlit.title("My Mom's new healthy diner.")
streamlit.header("Breakfast Favorites")

streamlit.text("🥣 Omega 3 and blueberry oatmeal.")
streamlit.text("🥗 Kale,Spinach and Rocket Smoothie.")
streamlit.text("🐔 Hard-boiled Free ranged Egg.")
streamlit.text("🥑🍞 Avocardo Toast.")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocardo,Strawberries'])

streamlit.dataframe(my_fruit_list)
