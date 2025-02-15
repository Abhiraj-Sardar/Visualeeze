import streamlit as st

def navigation(navlist):
    cols = st.columns(len(navlist))
    i=0
    for col in cols:
        col.link_button(navlist[i][0],url=f"{navlist[i][1]}",icon=navlist[i][2])
        i+=1

