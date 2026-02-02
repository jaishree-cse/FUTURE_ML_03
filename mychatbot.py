import streamlit as st

# Hide Streamlit default UI
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

#==================================================
#CHATBOT LOGIC
#==================================================
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "/start" in user_input:
        return "Let's start our chatbot."
    if "what laptop models do you have?" in user_input or "can you show me available models?" in user_input:
        return (
            "We offer Dell, HP, Lenovo, and ASUS laptops.\n"
            "Tell me your budget or usage (student, gaming, office)."
        )
    elif "which is the best laptop for student?" in user_input:
        return "For students, we recommend i5 processor, 8GB RAM, and SSD laptops."
    elif "which is good for gaming?" in user_input:
        return "Gaming laptops include RTX graphics, 16GB RAM, and high refresh rate displays."
    elif "what laptop is good for office?" in user_input or "work" in user_input:
        return "Office laptops are lightweight with long battery life and SSD storage."
    elif "how much do laptops cost?" in user_input:
        return "Laptop prices range from ₹35,000 to ₹1,50,000."
    elif "when will my laptop be delivered?" in user_input:
        return "Delivery takes 3 to 5 working days across India."
    elif "do laptops come with warranty?" in user_input:
        return "Yes, all laptops come with a 1-year manufacturer warranty."
    elif "what is your return policy?" in user_input:
        return "You can return the laptop within 7 days if there are any issues."
    elif "what payment methods are available?" in user_input:
        return "We accept UPI, credit/debit cards, net banking, and EMI options."
    elif "how can i contact customer support?" in user_input:
        return "For assistance, contact us at laptopsupport@example.com"
    elif "hi" in user_input or "hello" in user_input:
        return "Hello! Welcome to our Online Laptop Store 💻 How can I help you?"
    elif "bye" in user_input or "thank you" in user_input:
        return "Thank you for visiting! Have a great day 😊"
    else:
        return "Sorry, I didn't understand. Please ask about laptop models, price, or warranty."

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(page_title="Laptop Chatbot", page_icon="💻", layout="wide")

# ==================================================
# STRONG CSS RESET
# ==================================================
st.markdown("""
    <style>
    /* Remove ALL Streamlit spacing */
    html, body, [class*="css"] {
        margin: 0 !important;
        padding: 0 !important;
    }
    /* Remove Streamlit container padding */
    .block-container {
        padding: 0 !important;
    }
    /* Fixed header */
    .header {
        position: fixed;
        top: 0;
        width: 100%;
        height: 70px;
        background: linear-gradient(90deg, #2563eb, #1e40af);
        color: white;
        text-align: center;
        line-height: 70px;
        font-size: 24px;
        font-weight: bold;
        z-index: 9999;
    }
    /* Chat container */
    .chat-box {
        position: fixed;
        top: 70px;
        bottom: 90px;
        left: 0;
        right: 0;
        padding: 15px;
        overflow-y: auto;
        background-color: #f8fafc;
    }
    /* Chat bubbles */
    .user-msg {
        background-color: #2563eb;
        color: white;
        padding: 10px 14px;
        border-radius: 14px;
        margin-bottom: 8px;
        width: fit-content;
        margin-left: auto;
    }
    .bot-msg {
        background-color: #e5e7eb;
        color: black;
        padding: 10px 14px;
        border-radius: 14px;
        margin-bottom: 8px;
        width: fit-content;
    }
    </style>
    """, unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.markdown('<div class="header">💻 Online Laptop Shopping Chatbot</div>', unsafe_allow_html=True)
st.write("This is a Streamlit-based chatbot for laptop shopping assistance.")
# ==================================================
# CHAT HISTORY
# ==================================================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown('<div class="chat-box">', unsafe_allow_html=True)
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# INPUT  (CORRECT WAY)
# ==================================================
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "",
        placeholder="Type your message here..."
    )

    submitted = st.form_submit_button("Send")

    if submitted:
        if user_input.strip():
            reply = get_bot_response(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", reply))
            st.rerun()