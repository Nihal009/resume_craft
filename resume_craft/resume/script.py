from langchain_community.llms import Ollama



def craft_resume(latex,Job_desc):
    prompt=f"""
    "You are an AI assistant specialized in generating ATS-optimized resumes in LaTeX format. Your task is to create a comprehensive resume based on the provided job description and required skills. 

The resume should:
- Include relevant keywords from the job description.
- Highlight skills, experiences, and accomplishments that align with the job requirements.
- Be structured and formatted correctly in LaTeX.

Respond with only the LaTeX code for the resume, without any explanations, comments, or additional text. 

Job Description:{Job_desc}
resume original data:{latex}

Ensure that the final resume is professional and tailored specifically to this job.
"""
    llm=Ollama(model="llama3.2:1b")
    output=llm.invoke(prompt)
    return output