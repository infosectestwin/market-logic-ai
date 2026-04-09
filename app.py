import streamlit as st
import requests
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Market Logic AI Dashboard",
    page_icon="📈",
    layout="wide"
)

# Title and Branding
st.title("📈 S&P 500 Intelligence Pipeline")
st.markdown("### *Production-Grade Financial Signals via Zerve DAG*")
st.divider()

# --- API CONNECTION ---
API_URL = "https://market-logic-ai.hub.zerve.cloud"

def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)
        return response.json()
    except Exception as e:
        return None

# Fetch data once at the start
data = fetch_data()

if data:
    # --- ROW 1: METRIC CARDS ---
    # --- 1. Fix the Math (Win Rate) ---
    raw_win_rate = data.get("accuracy_percent", 0)
    
    # If the number is 52.33, we want 52.3.
    # If the number is 0.0052, it means the API is sending a double-decimal.

    if raw_win_rate < 0.01: 
        # This handles the 0.005 case
        formatted_win_rate = raw_win_rate * 10000 
    elif raw_win_rate < 1:
        # This handles the 0.52 case
        formatted_win_rate = raw_win_rate * 100
    else:
        # This handles the 52.3 case
        formatted_win_rate = raw_win_rate

    # --- 2. Dynamic Icons & Colors ---
    signal = data.get("signal", "NEUTRAL").upper()
    
    if "BUY" in signal:
        signal_icon = "🚀"
        signal_color = "green"
    elif "SELL" in signal:
        signal_icon = "⚠️"
        signal_color = "red"
    else:
        signal_icon = "⚖️"
        signal_color = "gray"

    # --- 3. Fix the Date Formatting ---
    raw_date = data.get("market_close_date", "N/A")

    # This takes '2026-04-06 00:00:00' and keeps only the part before the space
    clean_date = raw_date.split(' ')[0] if ' ' in raw_date else raw_date

    # --- 4. Render the UI ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # We use Markdown to add color to the signal text
        st.markdown(f"**Current Market Signal**")
        st.subheader(f"{signal_icon} :{signal_color}[{signal}]")
        
    with col2:
        # Display as a clean percentage (e.g., 52.3%)
        st.metric(label="Backtested Win Rate", value=f"{formatted_win_rate:.1f}%")
        
    with col3:
        # Display the clean date without the time
        st.metric(label="Last Data Update", value=clean_date)

    # --- ROW 2: SYSTEM ARCHITECTURE ---
    st.divider()
    st.subheader("System Architecture")
    st.info("""
    **Pipeline Flow:** Live FRED Data → Zerve DAG (20-day SMA Logic) → FastAPI Microservice → Streamlit Frontend.
    """)
    
    # Sidebar for extra "Impressive" links
    with st.sidebar:
        st.header("Technical Assets")
        st.link_button("View FastAPI Docs (Swagger)", "https://market-logic-ai.hub.zerve.cloud/docs")
        st.link_button("View Zerve Notebook", "https://www.zerve.ai/gallery/073645cd-9e82-42e6-8985-1a423a66fb79")
        
        st.divider()
    
        # The Live Status Indicator
        st.markdown("### 🟢 System Status: **Live**")
        current_time = pd.Timestamp.now().strftime('%I:%M:%S %p')
        st.caption(f"Last API Sync: {current_time}")
        
        st.write("---")
        st.info("This dashboard consumes a live Directed Acyclic Graph (DAG) pipeline built on Zerve.")
        st.caption("Developed for the 2026 Zerve Hackathon")

else:
    st.error("⚠️ Unable to reach the Zerve API. Please ensure the Zerve Deployment is active and Public.")
    if st.button("Retry Connection"):
        st.rerun()