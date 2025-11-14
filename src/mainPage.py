import streamlit as st
from helperMethods import get_ai_analysis, get_news_for_stock, get_news_for_stock_from_newsdata, load_watchlist, get_news_for_stock_from_newsdata

# ---------------------------------------------
# Streamlit Layout
# ---------------------------------------------


st.set_page_config(layout="wide")
st.title("📊 Live Stock Watchlist Dashboard")

# 4 column grid (2x2 layout)
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Panel 1: Watchlist
with col1:
    st.subheader("1️⃣ Watchlist")
    df = load_watchlist()


    # Use streamlit dataframe with selection
    selected_index = st.selectbox("Select a Stock", df["symbol"].tolist())
    st.dataframe(df, use_container_width=True)

# Panel 2: News
with col2:
    st.subheader("2️⃣ Latest News")
    if selected_index:
        news_list = get_news_for_stock(selected_index)
        #news_list = get_news_for_stock_from_newsdata(selected_index)
        st.dataframe(news_list, use_container_width=True)
        
# Panel 3: Empty for future
with col3:
    st.subheader("3️⃣ (Reserved for Future Expansion)")
    st.info("This section will be developed later.")

# Panel 4: AI Analysis
with col4:
    st.subheader("4️⃣ AI Analysis")
    if selected_index:
        st.write(get_ai_analysis(selected_index))