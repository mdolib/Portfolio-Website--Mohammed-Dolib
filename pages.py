import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests


def content_home():
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS -------------
    lottie_images = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_qp1q7mct.json")


    #------------------Header Section-----------
    with st.container():
        st.subheader("Hi, I am Mohammed Dolib :wave:")
        st.title("A Data Analyst From Sudan *Live* in Abu Dhabi - UAE")
        st.write("AS a Data professional I have a strong passion for Python and data sciences")
        #st.write("[Learn More >](https://www.novypro.com/profile_projects/mohammed-dolib)")
    #st.title("Mohammed Dolib Profilio Projects Apps")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write("""
                    On my daily work developing dashboards, reports, data models and performance related insights. 
                    Since i can map the business requirements as business analyst and as Data Analyst/Business intelligence specialist then translated them into operational dashboard and performance related insights. 
                    Develop a solution with communication with stakeholders. with data analyst skills experience i can query Data Warehouse using SQL to perform advanced analytics to large data sets. 
                    Data analytics pipeline to processes and concerning data extraction, data transformation and load ETL into valuable and comprehensible insights with Power BI, Excel, Python.
                    """)
            st.write("[My Linkdin Profile >](https://www.linkedin.com/in/mohammed-dolib-96a09973)")
            
            
        with right_column:
            st_lottie(lottie_images, height=400, key="coding")
            
    # -------- DATA FRAME --------------------------
    df = pd.DataFrame(np.random.randn(20,3), columns=['Length','Width','Size'])

    if st.checkbox('Check Me! To Preview Data'):
        st.write(df.head(5))

    st.line_chart(df)

    st.bar_chart(df)

    st.area_chart(df)
    st.write('---')

















# --------------- HOME PAGE ----------------
def home():
    #st.subheader('Home Page')
    content_home()
    

# --------------- PROJECTS PAGE ----------------
def projects():
    st.subheader('Projects Page 📚')
    
    tab1, tab2, tab3 = st.tabs(['Customers Services Dashboard 📈','Banking Dashboard 🏦','Kaggle Reports 😎'])
    
    with tab1:
        st.header('Al Ain Municiplity Customers Services')
        st.write("""Analyze reports for Al Ain city municipality customer services center data has been collected from different Integrated Management System (IMS). 
                Data has been extracted and clean on SQL server manipulation extract, transform and load (ETL) heavy shifting and lifting lead to SQL server after clean data import to Power BI where visualization and magics has been done.""")
        st.image('images\CSC-Portfalio.png')
    
    with tab2:
        st.header('Banking Dashboard')
        st.warning('WebSite under construction', icon="⚠️")
        
    with tab3:
        st.header('Kaggle Reports')
        st.warning('WebSite under construction',icon="⚠️")
    

# --------------- ABOUT ME PAGE ----------------
def me():
    st.subheader('About Me Page')
    st.write("""
             As a Data analyst professional, I have a keen a strong passion for exploring data and uncovering meaningful insights that can inform business decisions. 
             I have experience developing dashboards, reports, and data models using data from various sources to provide performance-related insights. 
             My ability to interpret find pattrrens and trends in data fit for business requirements and leverage your skills as a Data Analyst and Business Intelligence Specialist allows me to create operational dashboards that provide insightful performance metrics.
             """)
    st.write('---')
    
    st.subheader('Areas of Interest')
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.markdown('**Data Analytics**')
        st.image('images/icons/analytics.png')
        st.write('I love telling a story. Getting to the heart of a problem and coming up with a solution.')
        
    with col2:
        st.markdown('**Cloud Compute**')
        st.image('images/icons/cloud-server.png')
        st.write('I utilize Azure and Streamlit cloud Services to develop and productionize and published Dashboards. reports and machine learning system.')
        
    col3, col4 = st.columns(2, gap='large')
    with col3:
        st.markdown('**Collaboration** ')
        st.image('images/icons/collaborate.png')
        st.write('I enjoy working with my team to create winning strategies.')
        
    with col4:
        st.markdown('**Data Visualization**')
        st.image('images/icons/data-visualization.png')
        st.write('A picture says more than a thousand words..but what exactly do you want to visualize?')
        st.write('it’s hard for a human to compare quantitative data. Until now I have used Power BI, Python, Pandas plotting, Matplotlib, Seaborn and Streamlit for my data visualizations')
    st.write('----')
    st.subheader('Skills Expertise')
    st.markdown("""
                -   Data Pipline
                -	visualization
                -	Power BI 
                -	Data Analyst
                -	Storage
                -	SQL 
                -	Azure Cloud Computing
                -	Deployment
                -	Web Developments
                -	Data Modeling 
                -	Python and libraries framework
                -   Exploratory Data Analysis
                """)

# --------------- SERVICES PAGE ----------------
def services():
    st.subheader('Services Page')
    st.write('''As a freelance data analyst, I translate data into valuable meaing and insights. My goal is to improve results, make the right decisions and save costs. Use data visualization techniques to present the results. 
             I use SQL, Python, Power BI for my data projects.''')
    
    exp_data = st.expander('Data analysis')
    exp_data.write('I am specialized in analyzing data. Results, trends and recommendations are clearly presented in reports or tools.')
    
    exp_Dash = st.expander('Dashboards & Visualization')
    exp_Dash.write('Dashboards show the most recent results in an interactive way. By clicking and drilling, you will examine trends and patterns yourself.')
    exp_Dash.write('Present your data in an inspiring way by using an infographic rather than a piece of text. I create interactive infographics which can be used internally or publicly')
    
    exp_EDA = st.expander('Exploratory Data Analysis')
    exp_EDA.write('Exploratory data analysis (EDA) is a way of exploring data sets to find patterns, anomalies, and insights using statistics and visuals')
    
    exp_Analytics = st.expander('Data analytics')
    exp_Analytics.write('Get more value from your data with prediction models and machine learning techniques, for example by predicting behavior or targeting the right customer.')
    
    exp_ML = st.expander('Machine Learing')
    exp_ML.write('Machine learning is a way of making machines learn from data, without explicitly programming them.')
    

# --------------- CONTACT PAGE ----------------
def contact():
    st.subheader('Contact Page')
    
    st.write('''I would love to hear from you! Please drop me a message and let's see how I can help you.''')
    st.markdown('**FOLLOW ME**')
    col1, col2, col3, col4, col5 = st.columns(5)
    
    
    with col2:
        st.image('images/icons/linkedin.png',width=None)
        st.write('[linkedin](https://www.linkedin.com/in/mohammed-dolib-96a09973)')
    with col3:
        st.image('images/icons/github-sign.png', width=None)
        st.write('[GitHub](https://github.com/mdolib)')
    with col4:
        st.image("images/icons/Kaggle-logo.png", width=None)
        st.write('[Kaggle](https://www.kaggle.com/mohammeddolib/code)')
    
    st.balloons()