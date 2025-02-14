import streamlit as st

class WEBSITE: 

    def __init__(self):
        heading=st.container(border=True)
        heading.title("Visualezee",anchor="home")


    def navigation(self,navlist):
        
        cols = st.columns(len(navlist))
        i=0
        for col in cols:
            col.button(navlist[i],icon="🎯",use_container_width=True)
            i+=1

    
    @st.dialog("Login Form")
    def open_login_form(self,data):
        pass
    
    def login(self):


        pass

    def signup(self):
        pass
        

class HOME_PAGE:
    pass

if __name__=='__main__':
    w = WEBSITE()
    w.navigation(["Home","Git","Login","SignUp"])