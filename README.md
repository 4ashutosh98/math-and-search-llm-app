# Math and Search LLM Application

A Streamlit-powered application that uses Google Gemma 2 to solve mathematical problems and retrieve information from Wikipedia.

**[Try the live demo here](https://math-and-search-llm-app-ash.streamlit.app/)**

## Live Demo

Access the deployed application at: [https://math-and-search-llm-app-ash.streamlit.app/](https://math-and-search-llm-app-ash.streamlit.app/)

## Features

- **Mathematical Problem Solving**: Solves various mathematical problems with step-by-step reasoning
- **Wikipedia Search**: Retrieves information from Wikipedia on various topics
- **Logical Reasoning**: Provides detailed logical reasoning for questions
- **Interactive Chat Interface**: Maintains conversation history for context

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd math-and-search-llm-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get a Groq API key from [Groq's website](https://www.groq.com)

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Enter your Groq API key in the sidebar when prompted

3. Use the application to:
   - Ask mathematical questions
   - Request information on specific topics
   - Pose logical reasoning questions

4. Click the "Solve the Math problem" button to get your answer

## Example Questions

- "What is the square root of 144?"
- "If I have 5 apples and give away 2, how many do I have left?"
- "Who was Albert Einstein?"
- "What is the capital of France?"
- "Solve for x: 2x + 5 = 15"

## Technologies Used

- **Streamlit**: For the web interface
- **LangChain**: For connecting various LLM tools and utilities
- **Google Gemma 2**: The underlying language model (via Groq)
- **Wikipedia API**: For retrieving information
- **Python**: Programming language

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.