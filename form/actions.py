from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["NAME", "USERID","PHONENUMBER","LICENSE","AMOUNT","EMAIL","payment"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit", 
                                name=tracker.get_slot('NAME'),
                                userid=tracker.get_slot('USERID'),
                                phone_number=tracker.get_slot('PHONENUMBER'),
                                license=tracker.get_slot('LICENSE'),
                                amount=tracker.get_slot('AMOUNT'),
                                email=tracker.get_slot('EMAIL'),
                                payment=tracker.get_slot('payment')
                                )
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="NAME", intent="my_name_is"), self.from_text()],
            "userid": [self.from_entity(entity="USERID", intent="user_id"), self.from_text()],
            "phone_number": [self.from_entity(entity="PHONENUMBER", intent="phone_number"), self.from_text()],
            "license": [self.from_entity(entity="LICENSE", intent="vehicle_no"), self.from_text()], 
            "amount": [self.from_entity(entity="AMOUNT", intent="amount"), self.from_text()],
            "email": [self.from_entity(entity="EMAIL", intent="email"), self.from_text()], 
            "payment": [self.from_entity(entity="", intent=""), self.from_text()],          
        }

