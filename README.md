# Netlogo Models of Developer Interaction
This is my 4th year thesis on **"Agent based models of developer interaction in large scale software ecosystems"**. The model shows the characteristic curves of some graph metrics like Connection, Separation. The software development industry is now in full bloom. With the influx of multi-million dollar enterprise-level projects, like ChatGPT, or Autonumous Driving Cars, huge networks of developers are becoming more and more common behind such projects to drive them to completion. We aim to understand these complex social processes for better disemmination of information between developers, identify bottlenecks in flow of information, allocation of resources and ease of governance.

A promising apporach to simulate such networks is to use the agent based paradigm. One tool to the implement said Agent Based Modelling paradigm is netlogo.

# Main Models
<p>
  <img src = "https://github.com/SOUMEE2000/Netlogo-Models-of-Developer-Interaction/assets/52605586/a580c562-3750-4ae2-a27a-68dee7f16f93" height = 350 >
</p>

We assume that a software development ecosystem is divided into many modules, on which the development team works. Each team will also have a team lead who is in charge of co-ordination between the modules as they talk to the other team leads. The developers only interact amongst their team mates. Between the team leads we assume that communication happens following only these three structures as depicted above, a ring, a fully connected graph and a star network where the team leads report to a CEO. Ultimately we have proposed three models following these three structures of communication.

# Model Building

**[Netlogo](https://ccl.northwestern.edu/netlogo/download.shtml).** This is an agent-based modelling software to simulate our models on. The models have five parameters that control how the networks grow and evolve over time:
* Rate-of-Connection
* Number of people in the team
* Number of teams that exist
* Number of people to be added to be th team after each tick.
* Number of random connections between teams
The Netlogo interface for one of the models is present down below.

<p>
<img src="https://github.com/SOUMEE2000/Netlogo-Models-of-Developer-Interaction/blob/main/Images/Interface.png?raw=true" height = "500" label = "The Netlogo Interface">
</p>

# Model Validation
Using these parameters, we have built a model that shows high congruence with characteristics that are shown by real world data obtained from software development projects like **Openstack, Eclipse, Android** 

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
