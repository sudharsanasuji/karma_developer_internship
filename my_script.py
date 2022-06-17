#image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open(r"C:\Users\priyasuji\Downloads\sujipy\assimage.Png")
st.image(img)

st.caption("PLEASE INPUT THE NUMBER OF COINS YOU HAVE FOR EACH COIN TYPE")




#to get input

number_input1 = st.number_input("enter number of copper",min_value=0,max_value=100,step=1)
number_input2 = st.number_input("enter number of silver",min_value=0,max_value=100,step=1)
number_input3 = st.number_input("enter number of electrum",min_value=0,max_value=100,step=1)
number_input4 = st.number_input("enter number of gold",min_value=0,max_value=100,step=1)
number_input5 = st.number_input("enter number of platinum",min_value=0,max_value=100,step=1)




copper=1/100
silver=1/10
electrum=1/2
gold=1
platinum=10

#calculation
total= (number_input1*copper)+(number_input2*silver)+(number_input3*electrum)+(number_input4*gold)+(number_input5*platinum)
total=round(total)
st.subheader(f"YOU HAVE {total:,d} currency pieces")

# table     

tabvalue = [{"values":copper,"count":number_input1},
          {"values":silver,"count":number_input2},
          {"values":electrum,"count":number_input3},
          {"values":gold,"count":number_input4},
          {"values":platinum,"count":number_input5},]



df=pd.DataFrame(tabvalue)
st.dataframe(data=df)

st.bar_chart(data=df)
st.area_chart(data=df)

st.line_chart(tabvalue)
