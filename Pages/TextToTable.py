import streamlit as st
import pandas as pd
import time

container=st.container(border=True)
container.write("You can generate tablular data from your text. for these please ensure that you separate each row by a delimeter in your text. The delimeters can be ( . , | ) etc.")

# options for delimeter
row_delimeter=st.selectbox( 
    "Define The row Delimeter",
    ["|",",",".","-"]
)

column_delimeter=st.selectbox( 
    "Define The column Delimeter",
    [" ",",",".","-"],
)

txt = st.text_area("",placeholder="Enter The Text")

rows=txt.split(row_delimeter)
# st.write(rows)

dimension=st.selectbox( 
    "Define The Dimension",
    ["2x2","2x3","3x2","3x3"]
)

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
    try:
        if dimension=="2x2" or dimension=="3x2":
            c1=[]
            c2=[]

            for row in rows:
                txt_list=row.strip().split(column_delimeter)
                # txt_list
                c1.append(txt_list[0])
                c2.append(txt_list[1])

            df  = pd.DataFrame({"C1":c1,"C2":c2})
            st.write(df)

        if dimension=="2x3" or dimension=="3x3":

            c1=[]
            c2=[]
            c3=[]

            for row in rows:
                txt_list=row.strip().split(column_delimeter)
                # txt_list
                c1.append(txt_list[0])
                c2.append(txt_list[1])
                c3.append(txt_list[2])

            df  = pd.DataFrame({"C1":c1,"C2":c2,"C3":c3})
            st.write(df)
    except(Exception):
        st.error(f'Dimension {dimension} is not Compatible with given text', icon="🚨")





        
        
