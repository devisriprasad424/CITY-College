import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="World’s No 1 Event Managging",
    page_icon="🎉",
    layout="wide"
)

# ================== CUSTOM STYLES ==================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #fdfbfb, #ebedee);
}

/* Animations */
@keyframes fade {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes rise {
    from {transform: translateY(40px); opacity: 0;}
    to {transform: translateY(0); opacity: 1;}
}

/* Titles */
.hero {
    font-size: 52px;
    font-weight: 800;
    color: #e74c3c;
    text-align: center;
    animation: fade 2s;
}

.tagline {
    font-size: 22px;
    text-align: center;
    color: #2c3e50;
    margin-bottom: 30px;
    animation: fade 3s;
}

/* Cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.12);
    animation: rise 1.2s;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.05);
}

/* Section title */
.section {
    font-size: 34px;
    font-weight: 700;
    color: #34495e;
    margin-bottom: 15px;
    animation: fade 1.5s;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: gray;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
st.sidebar.title("🎊 Event Manager")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Schedule", "Planning", "Budget", "Designs", "Catering"]
)
st.sidebar.markdown("---")
st.sidebar.markdown("🌍 **World’s No 1 Event Managging**")

# ================== HOME ==================
if page == "Home":
    st.markdown("<div class='hero'>World’s No 1 Event Managging</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>We Design Moments. You Create Memories 💍✨</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>💒 Weddings</h3><p>Luxury weddings with royal elegance.</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>🎉 Events</h3><p>Corporate & personal celebrations.</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h3>🤝 Trusted Team</h3><p>Experienced planners & designers.</p></div>", unsafe_allow_html=True)

# ================== SCHEDULE ==================
elif page == "Schedule":
    st.markdown("<div class='section'>📅 Event Schedule</div>", unsafe_allow_html=True)
    st.date_input("Select Event Date")
    st.time_input("Select Event Time")
    st.selectbox("Event Type", ["Wedding", "Reception", "Corporate", "Birthday"])
    st.button("Save Schedule")

# ================== PLANNING ==================
elif page == "Planning":
    st.markdown("<div class='section'>📝 Event Planning</div>", unsafe_allow_html=True)
    st.checkbox("Venue Booking")
    st.checkbox("Decoration & Theme")
    st.checkbox("Photography")
    st.checkbox("Entertainment")
    st.checkbox("Guest Management")

# ================== BUDGET ==================
elif page == "Budget":
    st.markdown("<div class='section'>💰 Budget Planner</div>", unsafe_allow_html=True)
    v = st.number_input("Venue Cost", 0)
    c = st.number_input("Catering Cost", 0)
    d = st.number_input("Decoration Cost", 0)
    st.success(f"Total Budget: ₹ {v+c+d}")

# ================== DESIGNS ==================
elif page == "Designs":
    st.markdown("<div class='section'>🎨 Event Designs</div>", unsafe_allow_html=True)
    theme = st.selectbox("Choose Theme", ["Royal", "Beach", "Garden", "Traditional"])
    st.success(f"Theme Selected: {theme}")

    col1, col2, col3 = st.columns(3)
    col1.image("https://images.unsplash.com/photo-1529634597503-139d3726fed5", use_container_width=True)
    col2.image("https://images.unsplash.com/photo-1519741497674-611481863552", use_container_width=True)
    col3.image("https://images.unsplash.com/photo-1507504031003-b417219a0fde", use_container_width=True)

# ================== CATERING ==================
elif page == "Catering":
    st.markdown("<div class='section'>🍽 Catering</div>", unsafe_allow_html=True)
    st.multiselect("Select Cuisine", ["Indian", "Chinese", "Italian", "Continental"])
    st.radio("Meal Type", ["Veg", "Non-Veg", "Both"])

# ================== FOOTER ==================
st.markdown("<div class='footer'>© 2025 | 🌍 World’s No 1 Event Managging</div>", unsafe_allow_html=True)
