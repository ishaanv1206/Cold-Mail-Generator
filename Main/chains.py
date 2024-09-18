
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException




class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key="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", model_name="llama3-8b-8192")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Ishaan Verma, a first-year student at Manipal University Jaipur, passionate
            about Machine Learning and Artificial Intelligence. You are enthusiastic about exploring
            new technologies, particularly Generative AI and traditional ML algorithms, with a focus on
            implementing theoretical knowledge through hands-on projects. Your job is to write a personal
            statement or cover letter that highlights your enthusiasm for AI and ML, your readiness to take 
            on challenges, and your ability to learn and solve complex problems as part of a team.
            Also add the most relevant ones from the following links to showcase Ishaan's portfolio: {link_list}
            Remember you are Ishaan, Student at Manipal University Jaipur. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

