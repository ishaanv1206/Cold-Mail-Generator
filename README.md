
# 📧 Cold Email Generator

A **Cold Email Generator** built with Streamlit that allows you to generate personalized cold emails based on job descriptions and a portfolio of your skills. With the help of **Generative AI**, this app helps automate the process of writing effective cold emails for job applications.

## 🔥 Features

- **URL-based Job Extraction**: Enter a job listing URL and automatically extract relevant job details (skills, requirements, etc.).
- **Personalized Cold Email**: Generate cold emails tailored to your portfolio and the job's specific needs.
- **Portfolio Integration**: Upload your portfolio in CSV format, and the app will match your skills with the job requirements.
- **Streamlit UI**: Easy-to-use interface with real-time email generation.

## 🚀 Tech Stack

- **Python**
- **Streamlit** for the user interface
- **LangChain Community Document Loader** for extracting data from job URLs
- **ChromaDB** for managing a vector store of portfolio skills
- **Llama3.1 8b** model for cold email generation



## 🛠 Usage

1. **Upload your portfolio**: The portfolio should be in CSV format containing at least two columns: `Techstack` (your skills) and `Links` (related project or profile links).
2. **Enter the job listing URL**: Input the URL of the job listing you're applying for.
3. **Generate your cold email**: The app will analyze the job description and your portfolio to generate a cold email with links to your relevant projects.
4. **Copy the email**: The output is shown in Markdown format. Copy it and use it for your applications!

## 🖼 Screenshots
![Alt text](https://i.postimg.cc/SQcgV0M1/colmailgenerator.png)
![Alt text](https://i.postimg.cc/FRCNBf8m/colmailgeneratorsecondimage.png)






