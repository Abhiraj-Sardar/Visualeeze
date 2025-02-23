import streamlit as st
from Utils import Data
from Components import component
class WEBSITE: 

    def __init__(self):

        heading=st.container(border=True)
        heading.title("Visualezee",anchor="home")
        heading.html("<p>Developed by: <a href='https://github.com/Abhiraj-Sardar'>Abhiraj Sardar</a></p>")
        sidebar = {
                   "Visualezee": [
                    # st.Page("main.py", title="Explore"),
                    st.Page("./pages/Home.py", title="🏠 Home"),
                    st.Page("./pages/Login.py", title="🗝️ Login"),
                    st.Page("./pages/SignUp.py", title="🔓 Sign Up"),
                    ],
                    "Data Based Manipulation":[
                        st.Page("./pages/CSV_Data.py",title="📊 CSV Data"),
                        st.Page("./pages/EXCEL_Data.py",title="📈 Excel Data")
                    ],
                    "Text Based Manipulation":[
                        st.Page("./pages/TextInsight.py",title="📝 Text Insights"),
                        st.Page("./pages/RemoveWhiteSpace.py",title="🧹Remove Whitespace"),
                        st.Page("./pages/SortText.py",title="📶 Sort Text"),
                        st.Page("./pages/TextToTable.py",title="📅 Text To Table")
                    ]
            }
        
        
        navlist=Data.nav_data
        component.navigation(navlist)

        st.logo("./static/logo.png",size="large")
        web_app = st.navigation(sidebar)
        web_app.run()
        

        

if __name__=='__main__':
    w = WEBSITE()