import streamlit as st
from backend import Backend_functions as bf
import io


if "extract_button" not in st.session_state:
    st.session_state["extract_button"] = 0
if "num_params" not in st.session_state:
    st.session_state["num_params"] = 0
if "plotted" not in st.session_state:
    st.session_state["plotted"] = 0
if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = 0

with st.sidebar:
    uploaded_files = st.file_uploader('**Choose your .csv file:** ', type="csv", accept_multiple_files = False)
    if uploaded_files is not None:
        st.session_state["uploaded_files"] = 1
    else:
        st.session_state["uploaded_files"] = 0
    st.write(" ")
    st.write(" ")
    num_params = st.text_input(label = "No. of Parameters")
    extract_button = st.button("Extract Info", disabled = st.session_state["uploaded_files"] and int(st.session_state["num_params"]))
    if num_params and extract_button == 1:
        st.session_state["extract_button"] = 1
        st.session_state["num_params"] = num_params

st.title("Netlogo Behavior Space Plots")
tab1, tab2 = st.tabs(["**Parameter Space**","**Plots**"])

with tab1:
    if st.session_state["extract_button"] == 1 and st.session_state["uploaded_files"] == 1:
        doc = uploaded_files.getvalue().decode('utf-8').split("\r\n")
        obj = bf()
        param_map = obj.parse_csv(doc, int(st.session_state["num_params"]))
        reqd_params = []
        length = -1000000
        for i in param_map:
            if i != "[run number]":
                lst = st.text_input(label = i, key = i)
                if len(lst) != 0:
                    lst = list(map(float, lst.split(",")))
                    reqd_params.append(lst)
                    length = max(length, len(lst))
        plot = st.button("Plot2D", disabled = len(reqd_params)==st.session_state["num_params"])
        if plot == 1:
            st.session_state["plotted"] = 1

with tab2:
    if st.session_state["plotted"] == 1:
        st.session_state["plotted"] = 0
        #if "graph_in" not in st.session_state:
        #    st.session_state["graph_in"] = []

        title, fig = obj.plot_val(reqd_params, length)
        #st.session_state["graph_in"].append(fig)
        #print(st.session_state["graph_in"])
        count = 0
        # for i in st.session_state["graph_in"]:
        #     st.pyplot(i)
        #     img = io.BytesIO()
        #     i.savefig(img, format='png')
        #     st.download_button(label = "Download", data=img, mime="image/png", key = count)
        #     count += 1
        st.pyplot(fig)
        img = io.BytesIO()
        fig.savefig(img, format='png')
        st.download_button(label = "Download", data=img, mime="image/png", key = count, file_name=title)
