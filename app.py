import streamlit as st
from helper import generate_restaurant_name_and_item

st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Maxica","Arabic","American"))

if cuisine:
    response=generate_restaurant_name_and_item(cuisine)
    
    st.header(response["restaurant_name"].strip())
    menu_items=response['menu_item'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)
        