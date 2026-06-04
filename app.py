import streamlit as st
from rag_engine import rag

st.set_page_config(
    page_title="IPL Analytics AI Assistant",
    page_icon="https://static.vecteezy.com/system/resources/previews/075/244/948/non_2x/indian-premier-league-ipl-icon-on-transparent-background-free-png.png",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(
180deg,
#001B4D 0%,
#002D72 100%);
}

.stApp::before{
    content:"";
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.65);
    z-index:-1;
}

h1,h2,h3,h4,p,label{
    color:white !important;
}

section[data-testid="stSidebar"]{
    background:rgba(0,0,0,0.75);
}

div[data-testid="metric-container"]{
    background:rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    border-radius:15px;
    padding:15px;
    border:1px solid rgba(255,255,255,0.2);
}


/* Sidebar Buttons */

section[data-testid="stSidebar"] button {
    width: 200px !important;
    height: 55px;
    margin-left: auto;
    margin-right: auto;
    display: block;
    border-radius: 15px;
    font-size: 16px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

col1,col2,col3 = st.columns([1,6,1])

with col1:
    st.image("https://documents.iplt20.com//ipl/assets/images/ipl-logo-new-old.png", width=100)

with col2:
    st.markdown(
        """
        <h1 style='text-align:center;color:white;'>
        🏏 IPL Analytics AI Assistant
        </h1>

        <h4 style='text-align:center;color:#D9E4FF;'>
        Powered by RAG • ChromaDB • Groq
        </h4>
        """,
        unsafe_allow_html=True
    )

with st.sidebar:

    st.image("https://documents.iplt20.com//ipl/assets/images/ipl-logo-new-old.png", width=130)
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "💬  Chat Assistant",
        use_container_width=False,
    ):
        st.session_state.page = "chat"
    if st.button(
        "👤  Player Analytics",
        use_container_width=False
    ):
        st.session_state.page = "player"
    if st.button(
        "🏏  Team Analytics",
        use_container_width=False
    ):
        st.session_state.page = "team"
    if st.button(
        "📊  Match Analytics",
        use_container_width=False
    ):
        st.session_state.page = "match"
    if st.button(
        "🏆  Records & Stats",
        use_container_width=False
    ):
        st.session_state.page = "records"
    if st.button(
        "📚  IPL Knowledge Base",
        use_container_width=False
    ):
        st.session_state.page = "knowledge"
    st.markdown("---")
    if st.button(
        "ℹ️  About",
        use_container_width=False
    ):
        st.session_state.page = "about"

c1,c2,c3,c4 = st.columns(4)

c1.metric("Seasons","2008-2026")

c2.metric("Matches","1500+")

c3.metric("Players","1000+")

c4.metric("Analytics","Orange/Purple Cap")

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask anything about IPL...")

if query:
    st.session_state.messages.append(
        {
            "role":"user",
            "content":query
        }
    )
    with st.chat_message("user"):
        st.markdown(query)
    with st.spinner("Analyzing IPL Statistics..."):
        response = rag.invoke(query)
        answer = response["result"]
    with st.chat_message("assistant"):
        st.markdown(answer)
        with st.expander(
            "Retrieved Sources"):
            for doc in response["source_documents"]:
                st.write(doc.page_content)
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
