import streamlit as st
#st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
import os
import base64
from pathlib import Path

def add_logo(logo_url):
    height = 60
    logo = f"url(data:image/png;base64,{base64.b64encode(Path(logo_url).read_bytes()).decode()})"

    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: {logo};
                background-repeat: no-repeat;
                padding-top: {height - 40}px;
                background-size: 210px 50px;
                background-position: 20px 38px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
def set_page_container_style():
    st.markdown("""
            <style>
                   .css-18e3th9 {
                        padding-top: 2rem;
                        padding-bottom: 10rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
                   .css-1d391kg {
                        padding-top: 3.5rem;
                        padding-right: 1rem;
                        padding-bottom: 3.5rem;
                        padding-left: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)


def save_uploaded(uploadedfile):
    with open(os.path.join(MEDIA, INPUT_DIR, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())

    return os.path.join(MEDIA, INPUT_DIR, uploadedfile.name)
def save_response(response, filename):
    with open(os.path.join(MEDIA, OUTPUT_DIR, filename), "wb") as f:
        f.write(response.content)
    return os.path.join(MEDIA, OUTPUT_DIR, filename)

def format_df(df_label):
    emp = []
    for x in df_label:
        emp.append(eval(x))
    final = []
    for e in emp:
        pre_final = []
        for k, v in e.items():

            pre_final.append({"class": k, "count": v})
        final.append(pre_final)

    return final