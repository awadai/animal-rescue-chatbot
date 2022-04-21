# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCallHelp(Action):

    def name(self) -> Text:
        return "action_call_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #phonecall and GPS mechanism
        
        dispatcher.utter_message(text="Calling Animal Care Services...")

        return []


class ActionFoodInstructions(Action):

    def name(self) -> Text:
        return "action_food_instructions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food_care = {
            'dog': 'Boiled chicken with rice or boiled eggs are convenient and safe food items for dogs.',
            'cat': 'Plain rice and plain scrambled eggs are good quick fixes for a starving cat.',
            'bird': 'Sunflower seeds, fruit or peanuts are suitable meals for a large variety of birds.'
        }
        
        animal_type = tracker.get_slot('animal')

        if 'cat' in animal_type:
            animal_type = 'cat'
        elif 'dog' in animal_type:
            animal_type = 'dog'
        elif 'bird' in animal_type:
            animal_type = 'bird'

        dispatcher.utter_message(text=food_care[animal_type])

        return []