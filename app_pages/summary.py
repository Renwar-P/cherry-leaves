import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Project Summary")

    st.info(
    f"**General Information**\n"
    f"* Mildew, commonly known as powdery mildew, is a fungal disease that affects various plants, including cherry trees.\n"
    f"* It thrives in warm, humid conditions and appears as a powdery, white growth on the leaves, shoots, "
    f" and sometimes the fruit of trees. This fungal infection typically begins in early summer,\n"
    f" spreading through spores carried by wind or water, causing leaf distortion, premature leaf drop, and weakening the tree's overall health. "
    f"* Cherry trees, susceptible to powdery mildew, can suffer reduced photosynthesis and fruit quality when infected, "
    f"affecting their growth and productivity. Regular pruning, proper air circulation, "
    f"and fungicidal treatments can help prevent and manage mildew infestations in cherry trees.\n\n"
    f"**Project Dataset**\n"
    f"* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). "
    f"The dataset contains +4 thousand images taken from the client's crop fields. "
    f"The images show healthy cherry leaves and cherry leaves that have powdery mildew."
)
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Renwar-P/cherry-leaves/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate, "
        f"a healthy cherry leaf from one with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
        )


