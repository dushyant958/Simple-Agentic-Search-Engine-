import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name = "Search")
st.title("Jarvis - Chat & Search")
"""
In this example, we'd be using StreamlitCallbackHandler to display the throughts and actions of the agent in an interactive Streamlit App.
"""

if "data" not in st.session_state:
    st.session_state["data"] = [
        {"role":"assistant", "content": "Hi, I'm Jarvis who can search the web. How can I help you"}
    ]

for msg in st.session_state.data:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="What is Machine Learning?"):
    st.session_state.data.append({"role":"user", "content":prompt}) 
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=groq_api_key, model_name = "Llama3-8b-8192", streaming=True)
    tools = [search, arxiv, wiki]
    search_agent = initialize_agent(tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)  

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(prompt, callbacks=[st_cb])

        st.session_state.data.append({"role":"assistant", "content":response})
        st.write(response)