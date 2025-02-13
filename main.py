import streamlit as st

class WEBSITE:

    def __init__(self):
        st.write("Hello")

    def navigation(self):
        container = st.container(border=True)
        container.write("This is inside the container")
        st.write("This is outside the container")


if __name__=='__main__':
    w = WEBSITE()
    w.navigation()