import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

## Set up the Streamlit app
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant", page_icon="🦜")
st.title("Text to Math Problem Solver with Google Gemma 2")
st.write("This is a simple app that uses Google Gemma 2 to solve math problems and search for information on Wikipedia. You can ask math questions or ask for information on a topic, and the app will provide you with the answer.")

groq_api_key = st.sidebar.text_input(label="Groq API key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

llm = ChatGroq(model = "Gemma2-9b-It", groq_api_key = groq_api_key)

## Initializing the tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name = "Wikipedia",
    func=wikipedia_wrapper.run,
    description="Tool for Searching Wikipedia for information on the topics mentioned by the user.",
)

## Initialize the Math tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name = "Calculator",
    func=math_chain.run,
    description="Tool for solving math problems and converting text to math problems. Only input mathematical expression needs to be provided."
)

prompt = """
You are an agent tasked for solving user's mathematical question. Logically arrive at the solution
and display it point wise for question below.
Question: {question}
Answer: 
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template = prompt
)

## Combine all the tools into chain
chain = LLMChain(llm = llm, prompt = prompt_template)

reasoning_tool = Tool(
    name = "Reasoning Tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

## Initialize the agents

assistant_agent = initialize_agent(
    tools = [wikipedia_tool, calculator, reasoning_tool],
    llm = llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = False,
    handle_parsing_errors = True
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi!!!, I'm a Math chatbot who can answer all your math questions."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

## Function to generate the response
def generate_response(question):
    response = assistant_agent.invoke({"input":question})
    return response

## Lets start the interaction
question = st.text_area("Enter your question:", placeholder="Write a math problem or ask for information on a topic to search on Wikipedia.")

if st.button("Solve the Math problem/ Search Wikipedia"):
    if question:
        with st.spinner("Solving the problem/searching wikipedia..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write("### Response:")
            st.success(response)

    else:
        st.warning("Please enter a question.")