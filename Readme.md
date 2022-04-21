# Creating an animal care and rescue helpbot using Rasa

Our aim is to create a chatbot that can help people properly care for and deal with stray animals and help injured animals or animals in distress in general.

For this demonstration, we would like our chatbot to do the following:
- Inform the user about how to safely approach and care for stray animals.
- Inform the user about proper food depending on the type of animal (we will limit our scope to cat, dog or bird).
- Suggest calling professional help in case the animal is sick or injured (we won't be actually be implementing the phonecall and GPS mechanism).

## Environment Setup

First, create a virtual environment to install Rasa and its dependencies. We will use Conda to manage the environment but same can be done with pip.

```
conda create -n rasa python=3.8
```

After the environment is created, activate it and install the necessary packages that we will need for this chatbot.

```
conda activate rasa
pip install rasa
pip install spacy
pip install transformers
python -m spacy download en_core_web_md
```

## Creating the Rasa Project

CD into a directory where you want to create the project and run the following command:

```
rasa init
```