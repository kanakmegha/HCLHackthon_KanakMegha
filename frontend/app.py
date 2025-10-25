import streamlit as st
import requests
from streamlit_push_notifications import send_push,send_alert

API_URL = "http://localhost:8000"

st.title("Customer Sign up")
#input defined
Name=st.text_area("Enter Name :")
Email=st.text_area("Enter mail: ")
Phoneno=st.text_area("Enter Phone No: ")
Password=st.text_input("Enter password: ",type="password")
Confirm_Password=st.text_input("Confirm Password: ",type="password")

#upload doc
label="KYC Doc"
uploaded_pdf=st.file_uploader(label, type=["pdf"], accept_multiple_files=False)
#print(file1)
#f1=file1.getvalue()
#uploaded_file = requests.post(f"{API_URL}/upload",f1)
#st.write(uploaded_file)

if st.button("Upload PDF"):
    response = requests.post(f"{API_URL}/upload", params=uploaded_pdf.name, files={"uploaded_file": uploaded_pdf.getvalue()})
    st.write(response)




p={
    'Name':Name,
    'Mail':Email,
    'phoneNo':Phoneno,
    'password':Password,
    'passwordchecker':Confirm_Password
}


#validation and submiit
if st.button("Submit"):
    if not Phoneno.isdigit():
        send_alert("Phone No is not valid")
    if Password!=Confirm_Password:
        send_alert("Password does not match")
    #calling fillinfo endpoint
    validate=requests.get(f"{API_URL}/fillinfo", json=p)
    st.success(validate.json())

    response = requests.post(f"{API_URL}/save")
    #response = requests.post(f"{API_URL}/save",params=to_be_saved)
    st.success(response.json())

# Fetch tasks

