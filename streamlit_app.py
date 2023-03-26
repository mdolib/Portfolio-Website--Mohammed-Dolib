import requests
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from pages import *


st.set_page_config(page_title="Portfolio Website- Mohammed Dolib", page_icon=":📊:")

# ------------ REMOVE FOOTER AND HAMBRUGER -----------
st.markdown("""
            <style>
            #MainMenu{
                visibility: hidden;
            }
            footer{
                visibility: hidden;
            }
            </style>
            """,
            unsafe_allow_html=True)



    
# -------------OPTION MENU -------------
menu_selected = option_menu(
    menu_title= None,
    options= ['Home','Projects','About me','Services','Contact'],
    icons= ['house','bar-chart-line','file-person','activity','chat-text'],
    orientation='horizontal',
    default_index= 0
)

if menu_selected == 'Projects':
    projects()
if menu_selected == 'Home':
    home()
if menu_selected == 'About me':
    me()
if menu_selected == 'Services':
    services()
if menu_selected == 'Contact':
    contact()




