import streamlit as st
import pandas as pd
import altair as alt

container = st.container(border=True)
container.text("Enter Your Data to get Insights in Excel format... 💹📈📉📊")
file = st.file_uploader("Enter a XLSX File:")

if file is not None:
    data = pd.read_excel(file)
    st.write(data)
    
    st.container(border=True).text(f"The Data has {data.shape[0]} Rows and {data.shape[1]} Columns")

    st.markdown("## Column Info")
    st.write(data.columns)
    
    st.markdown("## Description of Data")
    st.write(data.describe())

    st.markdown("## Graphs & Charts")
    
    dt=list(data.columns)

    y_axis = st.multiselect(
        "Select Y Axis",
        dt,
        
    )

    st.write("You selected:", y_axis)

    x_axis = st.selectbox(
        "Select X Axis",
        dt,
    )

    st.write("You selected:", x_axis)


    

    #creating tabs for each type of graph 

    st.markdown("## Basic Charts")

    tab1, tab2, tab3, tab4 = st.tabs(["Scatter Chart", "Area Chart", "Line Chart","Bar Chart"])

    with tab1:
        sc = pd.DataFrame(data.iloc[0:], columns=dt)
        st.scatter_chart(sc,x=x_axis,y=y_axis)
    
    with tab2:
        ac = pd.DataFrame(data.iloc[0:], columns=dt)
        st.area_chart(ac,x=x_axis,y=y_axis)
    
    with tab3:
        lc = pd.DataFrame(data.iloc[0:], columns=dt)
        st.line_chart(lc,x=x_axis,y=y_axis)
    
    with tab4:
        bc = pd.DataFrame(data.iloc[0:], columns=dt)
        st.bar_chart(bc,x=x_axis,y=y_axis)


    st.markdown("## Find Values Unique to a Particular Column")
    uniq=st.selectbox(
        "Select A Column",
        dt
    )
    st.write(data[uniq].unique())