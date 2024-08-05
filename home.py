import streamlit as st
import random
import os

images = os.listdir("images/us/")

def line():
    st.write("---")
# st.error("For **Zeinab**")
st.image("images/cherry tree-amico.png")
st.error("Just for you **Zainaby** :material/local_florist:")
st.audio("Ed Sheeran - Thinking out Loud (Lyrics).mp3", format="audio/wav", autoplay=True)
# line()

messgaes = [
    "Every time I see your smile, my world becomes brighter.",
    "Your beauty shines brighter than the stars in the night sky.",
    "I can't stop thinking about your mesmerizing eyes.",
    "You are the reason why my heart beats faster.",
    "Your love is the greatest gift I've ever received.",
    "You've stolen my heart and I don't want it back. It's in good hands with you.",
    "I can't resist your smile. Can I make it my personal sunshine every day?",
    "Just wanted to let you know that you make my heart skip a beat every time I see you.",
    "Every time I look into your eyes, I get lost in a world full of love and happiness.",
    "You are the most beautiful woman in the world, inside and out.",
    "Just thinking about you makes me feel warm and fuzzy inside. I'm falling for you more and more every day.",
    "You bring out the best in me and make me want to be a better person. Thank you for being in my life.",
    "I hope you know how amazing you are. You deserve all the love and happiness in the world.",
    "You are my sunshine on a cloudy day. Thank you for always brightening up my life.",
    "Every time I see your smile, my world becomes brighter.",
    "Your beauty shines brighter than the stars in the night sky.",
    "You light up my life.",
    "You're the most beautiful girl I've ever seen.",
    "I can't get you out of my mind.",
    "I'm so lucky to have you in my life.",
    "You make my world brighter.",
    "You're the missing piece to my puzzle.",
    "I'm falling for you more and more each day.",
    "You're the reason I smile every day.",
    "I can't wait to see your beautiful smile again.",
    "You make my heart race like no one else can.",
    "I hope you know how amazing you are.",
    "You're the sunshine on a cloudy day.",
    "You're the sweetest thing in my life.",
    "Every day with you is a blessing.",
    "I can't wait to see that beautiful smile of yours again. ",
    "I hope you dream of me tonight, beautiful.",
    "As the stars light up the night sky, know that you light up my world.",
    "Lets flip coin  \nHeads, i'm yours  \nTails you are mine  :material/favorite:"
]

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["First", "Second", "Third", "Fourth", "Fifth","Finally"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Spring flower-pana.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.error("Do you know how much i **Love** you?")
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/cherry blossom-pana.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.error("How much i feel that i can't live without you?")
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/cherry blossom-cuate.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.error("More than the sea!")
with tab4:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/rose flower-amico.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.error("No, more than the planet!")
with tab5:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/rose flower-rafiki.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.error("Also no, I love you more than the whole universe")
with tab6:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Before Dawn-bro.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.warning("Cause you are my :orange[**Sunshine**]")
line()

col1, col2 = st.columns([3,2])
with col1:
    st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
    st.error("You are the place where i feel safe and comfortable in it.")
with col2:
    st.image("images/cherry tree-pana.png")
line()

col1, col2 = st.columns([2,3])
with col1:
    st.image("images/cherry tree-amico.png")
with col2:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.error("You are the best thing happened in my life")
line()

col1, col2 = st.columns([2,2])
with col1:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.error("You are the best thing happened in my life")
with col2:
    st.image("images/magic tree-cuate.png")
line()

col1, col2 = st.columns([2,3])
with col1:
    st.image("images/magic tree-pana.png")
with col2:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.error("You are the best thing happened in my life")
line()

col1, col2 = st.columns([3,2])
with col1:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.warning("Cause you are my :orange[**Sunshine**]")
with col2:
    st.image("images/cherry tree-cuate.png")
line()

# col1, col2 = st.columns([2,3])
# with col1:
#     st.image("images/cherry tree-bro.png")
# with col2:
#     st.write("  \n")
#     st.write("  \n")
#     st.write("  \n")
#     st.write("  \n")
#     st.write("  \n")
#     st.write("  \n")
#     st.write("  \n")
#     st.success("test")
# line()

col1, col2, col3 = st.columns([2,2,2])
with col1:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.success("There is my life with you")
with col2:
    st.image("images/Climate change-rafiki.png")
with col3:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.info("There is my life without you")
line()

st.error("Could be us?")
st.image("images/In love-bro2.png")
line()

st.error("keeps forward and grow together")
st.image("images/Free love-bro.png")
line()

st.error("I will be here for you, **Forever**")
st.image("images/Forever-bro.png")
st.error("And always :material/favorite:")
line()

if st.columns([3,1,3])[1].button("Press me"):
    st.balloons()
    col1, col2 = st.columns([2,3])
    with col1:
        st.image(f"images/us/{images[random.randint(0,len(images)-1)]}")
    with col2:
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.error(f"{messgaes[random.randint(0,len(messgaes)-1)]} :material/favorite:")
