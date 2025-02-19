import streamlit as st
import string

st.markdown("## Text Insights")

txt = st.text_area("Enter The Text to get insights")
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation
clean_txt = txt.translate(translator)
txt_length=len(clean_txt)

list_of_words=clean_txt.split()
no_of_word=len(list_of_words)


#count no of punctuation
cnt_punc=0
cnt_digit=0

for ch in txt:
    if ch in string.punctuation:
        cnt_punc+=1
    
    elif ch.isdigit():
        cnt_digit+=1

container = st.container(border=True)
container.text(f"No of characters in The Text is : {txt_length}")
container.text(f"No of words in The Text is : {no_of_word}")
container.text(f"No of Punctuation in The Text is : {cnt_punc}")
container.text(f"No of Digit in The Text is : {cnt_digit}")

unique_words=set(list_of_words)
st.write(clean_txt)



