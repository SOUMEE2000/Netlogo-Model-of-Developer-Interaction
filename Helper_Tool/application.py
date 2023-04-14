import streamlit as st
from backend import Backend_functions as bf
import io


if "extract_button" not in st.session_state:
    st.session_state["extract_button"] = 0
if "num_params" not in st.session_state:
    st.session_state["num_params"] = 0
if "num_reporters" not in st.session_state:
    st.session_state["num_reporters"] = 0
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
    num_reporters = st.text_input(label = "No. of Reporters")
    extract_button = st.button("Extract Info", disabled = not st.session_state["uploaded_files"] and int(st.session_state["num_params"]))
    if num_params and extract_button == 1:
        st.session_state["extract_button"] = 1
        st.session_state["num_params"] = num_params
        st.session_state["num_reporters"] = num_reporters

st.title("Netlogo Behavior Space Plots")
tab1, tab2 = st.tabs(["**Parameter Space**","**Plots**"])

with tab1:
    if st.session_state["extract_button"] == 1 and st.session_state["uploaded_files"] == 1:
        st.write("**Write the values of the parameter you want to see varied in comma separated values**")
        doc = uploaded_files.getvalue().decode('utf-8').split("\r\n")
        obj = bf()
        param_map, reporters = obj.parse_csv(doc, int(st.session_state["num_params"]), int(st.session_state["num_reporters"]))
        reqd_params = []
        length = -1000000
        st.write("")
        st.subheader("**Parameters:**")
        for i in param_map:
            if i != "[run number]":
                col1, col2, col3, col4 = st.columns([4,1,1,1])
                with col1: lst = st.text_input(label = i, key = i)
                with col2: st.metric(label="Max:", value=str(param_map[i][0]))
                with col3: st.metric(label="Min:", value=str(param_map[i][1]))
                with col4: st.metric(label="Steps:", value=str(param_map[i][2]))
                if len(lst) != 0:
                    lst = list(map(float, lst.split(",")))
                    reqd_params.append(lst)
                    length = max(length, len(lst))

        st.write("")
        st.subheader("**Reporters:**")
        col_list = st.columns(int(st.session_state["num_reporters"]))

        reporter_selected = []
        for i in range(len(reporters)):
            with col_list[i]: lst = st.checkbox(reporters[i])
            if lst:
                reporter_selected.append(i)

        plot = st.button("Plot2D", disabled = len(reqd_params)==st.session_state["num_params"])
        if plot == 1:
            st.session_state["plotted"] = 1



with tab2:
    if st.session_state["plotted"] == 1:

        for i in reporter_selected:
            title, fig = obj.plot_val(reqd_params, length, i)
            st.pyplot(fig)
            img = io.BytesIO()
            fig.savefig(img, format='png')
            st.download_button(label = "Download", data=img, mime="image/png", key = i, file_name=str(title)+".png")
