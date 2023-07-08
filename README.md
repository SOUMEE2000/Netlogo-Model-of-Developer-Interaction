# Netlogo Models of Developer Interaction
This is my 4th year thesis on **"Agent based models of developer interaction in large scale software ecosystems"**. The model shows the characteristic curves of some graph metrics like Connection, Separation. The software development industry is now in full bloom. With the influx of multi-million dollar enterprise-level projects, like ChatGPT, or Autonumous Driving Cars, huge networks of developers are becoming more and more common behind such projects to drive them to completion. We aim to understand these complex social processes for better disemmination of information between developers, identify bottlenecks in flow of information, allocation of resources and ease of governance.

A promising apporach to simulate such networks is to use the agent based paradigm. One tool to the implement said Agent Based Modelling paradigm is netlogo.

# Main Model

**[Netlogo](https://ccl.northwestern.edu/netlogo/download.shtml).** This is an agent-based modelling software to simulate real world problems. Displayed beneath are pictures of the interface and the output graphs displaying the Degree of Connection. The model has five parameters that control how the network grows and evolves over time:
* Rate-of-Connection
* Number of people in the team
* Number of teams that exist
* Number of people to be added to be th team after each tick.
* Number of random connections between teams

Using these parameters, we have built a model that shows high congruence with characteristics that are shown by real world data obtained from software development projects like **Openstack, Android and Eclipse.**

<p>
<img src="https://github.com/SOUMEE2000/Netlogo-Models-of-Developer-Interaction/blob/main/Images/Interface.png?raw=true" height = "400">
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
