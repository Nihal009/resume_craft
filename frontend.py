import streamlit as st
import requests
import json
st.title("Resume-Craft")

st.write("hi i am vader")
with st.form("Resume-submit"):
    latex_resume=st.text_area(label='latex_resume',placeholder='Paste The Latex Code of your Resume Here:',height=200)
    job_description=st.text_area(label='job_description',placeholder='Paste The Job Description Here:',height=200)
    if st.form_submit_button('Generate'):
        data={
            'latex_resume':latex_resume,
              'job_description':job_description
              }
        response=requests.post('http://127.0.0.1:8000/api/resume-job/',json=data)
        
        if response.status_code in [200,201]:
            latex_code=response.json().get('latex_resume')
            if latex_code:
                st.text_area("generated latex code",latex_code,height=300)
            else:
                st.error("No Latex code returned")
        else:
            st.error(f"Error converting the resume:{response.status_code}")
            st.write(response.text)
    