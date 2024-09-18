import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, PortfolioClass, clean_text):
    st.title("📧 Cold Mail Generator")
    st.write("Applying to your dream job becomes easy with our AI-Generated Coldmail generator. Just enter the job URL and portfolio excel sheet and get your personalized coldmail for free.")
    st.image("banner.jpg", width=400)
    
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
    uploaded_file = st.file_uploader("Upload your Portfolio CSV file")
    submit_button = st.button("Submit")

    if submit_button:
        if uploaded_file is not None:
            try:
                # Create an instance of Portfolio using the uploaded file
                portfolio = PortfolioClass(file=uploaded_file)
                
                # Load the portfolio data
                portfolio.load_portfolio()

                # Load job data from the URL
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                
                # Extract jobs using the provided LLM model
                jobs = llm.extract_jobs(data)
                
                # Generate emails based on the job descriptions and portfolio
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)
                    st.code(email, language='markdown')

            except Exception as e:
                st.error(f"An Error Occurred: {e}")
        else:
            st.error("Please upload a valid Portfolio CSV file.")

if __name__ == "__main__":
    chain = Chain()  # Initialize your Chain object
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    
    # Call the Streamlit app
    create_streamlit_app(chain, Portfolio, clean_text)
