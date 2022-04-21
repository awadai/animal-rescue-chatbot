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

Open a terminal in the directory where you want to create the project and run the following command:

```
rasa init
```

This will create the necessary files with some starter content and allow you to train an initial moodbot.

## Training the Chatbot

In order to train the chatbot we need to properly populate the following files:
- domain.yml: lists all the intents, enitites, slots, responses and actions available to the chatbot.
- config.yml: configuration of pipeline components for both the NLU unit and the dialogue manager.
- nlu.yml: contains training data for intent classification and entity recognition.
- stories.yml: contains examples of different conversation scenarios to train the dialogue manager.
- rules.yml: contains actions that the chatbot must always follow when presented with a certain scenario. This requires a RulePolicy components in the dialogue manager.
- actions.py: Python code implementing custom actions that can be done by the chatbot.

Once the files are properly populated, the chatbot can be trained by running:

```
rasa train
```

Rasa can also produce a graph visualization of the conversation flow that you created using:

```
rasa visualize
```

## Using the Chatbot

Once training is complete, you launch and chat with the bot. First run the following command in the terminal:

```
rasa run actions
```

Then keep the terminal open and in another terminal run:

```
rasa shell
```

The first terminal launches an action server that the main chatbot terminal uses to execute custom actions.

You can also run the NLU unit without the dialogue component. This will show the intent classification along with the confidence for all classes and the extracted entities if any. This allows for an inspection of how well the NLU is able to interpret the user's utterances. The actions terminal is not needed for this case.

```
rasa shell nlu
```
