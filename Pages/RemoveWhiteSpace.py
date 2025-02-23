import streamlit as st
import time


# options for delimeter
delimeter=st.selectbox( 
    "Select Delimeter",
    [" ","|",",",".","-"]
)

txt = st.text_area("",placeholder="Enter The Text")

filtered_text=txt.replace(delimeter,"")

# st.write(filtered_text)

#text generator function
def generate_text():
    st.write("Here is Your Updated Text...")
    for ch in filtered_text:
        yield ch
        time.sleep(0.02)
    
    st.toast("Text Generation Completed",icon="✅")
    

if st.button("Generate",icon="🤖"):
    if filtered_text == "":
        st.write("Enter the Text first...")
    else:
        st.write_stream(generate_text)