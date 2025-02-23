import streamlit as st
import time


# options for delimeter
delimeter=st.selectbox( 
    "Please Ensure that the delimeters are correct",
    [" ","|",",",".","-"],
)

txt = st.text_area("",placeholder="Enter The Text")

filtered_text=txt.split(delimeter)
filtered_text.sort()

# st.write(filtered_text)

#text generator function
def generate_text():
    st.write("Here is Your Sorted Text...")
    for ch in filtered_text:
        yield ch + delimeter + " "
        time.sleep(0.02)

    st.toast("Text has been Sorted...",icon="✅")

if st.button("Generate",icon="🤖"):

    if len(filtered_text) == 1:
        st.write("Enter the Text first...")
    else:
        st.write_stream(generate_text)

