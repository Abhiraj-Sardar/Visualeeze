import streamlit as st
import pandas as pd
import string

st.markdown("## Text Insights")

txt = st.text_area("",placeholder="Enter The Text to get insights")
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation
clean_txt = txt.translate(translator)
txt_length=len(clean_txt)

whitespace = clean_txt.count(" ")
no_of_character = txt_length - whitespace
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

text_data={"Total":["Character","Words","Punctuations","Digit"],
            "Value":[no_of_character,no_of_word,cnt_punc,cnt_digit]
            }
text_insight=pd.DataFrame(text_data)
text_insight

st.markdown("## Graphical Analysis")
st.area_chart(text_insight, x="Value", y="Total",color="#f1dba0")


unique_words=set(list_of_words)
st.markdown("## Words Occurance")
# st.write(unique_words)

words=[]
cnt_occur_word=[]
cnt_word=0
for word in unique_words:
    words.append(word)
    for w in list_of_words:
        if word==w:
            cnt_word+=1
    cnt_occur_word.append(cnt_word)
    cnt_word=0

word_data = {
    "Word":words,
    "Count":cnt_occur_word
}

word_insight=pd.DataFrame(word_data)
word_insight




