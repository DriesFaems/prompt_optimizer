import streamlit as st
from groq import Groq

# Page setup
st.title("Prompt Optimizer")

# Sidebar for API key
with st.sidebar:
    groq_api_key = st.text_input("Enter Groq API Key", type="password")

# Main content
st.write("""
This tool helps optimize your prompts by adding:
1. Chain of thought prompting
2. Few shot examples 
3. Expected output format
4. Rules and constraints
""")

# Input prompt
original_prompt = st.text_area("Enter your original prompt:", height=100)

if st.button("Optimize Prompt") and groq_api_key and original_prompt:
    try:
        client = Groq(api_key=groq_api_key)
        
        optimization_prompt = f"""Please help optimize this prompt: "{original_prompt}"

        Create an enhanced version that includes:
        1. Chain of thought prompting - Break down the steps needed
        2. Few shot examples - Provide 2-3 examples
        3. Expected output format - Clearly specify the desired format
        4. Rules and constraints - Add relevant guidelines

        Format your response as:

        ENHANCED PROMPT:
        [The complete optimized prompt]

        EXPLANATION:
        [Brief explanation of how the prompt was enhanced]
        """
        
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": optimization_prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
        )
        
        # Display results
        st.subheader("Optimized Prompt")
        st.write(response.choices[0].message.content)
        
    except Exception as e:
        st.error(f"Error optimizing prompt: {str(e)}")
else:
    if not groq_api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
    elif not original_prompt:
        st.info("Please enter a prompt to optimize.")
