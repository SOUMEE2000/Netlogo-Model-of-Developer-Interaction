# Netlogo Models of Developer Interaction
Agent based models of developer interaction in large scale software ecosystems. The finished model will show the graphs of some social network properties like Connection, Clustering and Separation. The software development industry is now in full bloom. With the influx of multi-million dollar enterprise-level projects, like ChatGPT, or Autonumous Driving Cars, huge networks of developers are becoming more and more common behind such projects to drive them to completion. To understand these complex social processes of our time, it is essential that research draws attention both to human behaviour and to the structure of social networks and their dynamics. A promising approach to address these two aspects is the combination of social network analysis (SNA) and agent-based modelling (ABM).

One such tool is netlogo.

# Main Model

**[Netlogo](https://ccl.northwestern.edu/netlogo/download.shtml).** This is an agent-based modelling software to simulate real world problems. Displayed beneath are pictures of the interface and the output graphs displaying the Degree of Connection. The model has 4 parameters:
* Rate-of-Connection
* Number of people in the team
* Number of teams that exist
* Number of people to be added to be th team after each tick.
* Number of random connections between teams

<p>
<img src="https://github.com/SOUMEE2000/Netlogo-Models-of-Developer-Interaction/blob/main/Images/Interface.png?raw=true" height = "400">
<img src="https://github.com/SOUMEE2000/Netlogo-Models-of-Developer-Interaction/blob/main/Images/Graph-of-Connection.jpg?raw=true" height = "300">
</p>

# Helper Tool
Netlogo spills out csv data while running experiments on model parameters. However, said data is very messy. This is a UI, built on streamlit and deployed on the streamlit cloud at [Behavioural Space Parser](https://soumee2000-netlogo-models-of-deve-helper-toolapplication-0d427y.streamlit.app/) that can appropriately parse the csv files. The code is available in the Helper Tool folder. It can be downloaded and running the following at your terminal will get it fired up.
```
pip install -r requirements.txt
streamlit run application.py
```
### Screenshots of the Tool
<p>
<img src="https://github.com/SOUMEE2000/Netlogo-Models-of-Developer-Interaction/blob/main/Images/Interface_Helper.png?raw=true" height = "300" width = "400">
<img src="https://github.com/SOUMEE2000/Netlogo-Models-of-Developer-Interaction/blob/main/Images/Output_Helper.png?raw=true" height = "300" width="400">
</p>
