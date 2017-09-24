from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Buket Bozduman'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'assignment'
    players_per_group = 4
    num_rounds = 1
   
    
    pot_size=c(200000)

    shock_probability = 0.3

class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.group_randomly()


class Group(BaseGroup):
     

    decision_p1 = models.CharField(choices=["Default", "Repay"])
    decision_p2 = models.CharField(choices=["Default", "Repay"])
    decision_p3 = models.CharField(choices=["Default", "Repay"])
    decision_p4 = models.CharField(choices=["Default", "Repay"])
    decision_p5 = models.CharField(choices=["Default", "Repay"])
    decision_p6 = models.CharField(choices=["Default", "Repay"])
    decision_p7 = models.CharField(choices=["Default", "Repay"])
    decision_p8 = models.CharField(choices=["Default", "Repay"])



    endowment_p1 = models.CurrencyField()
    endowment_p2 = models.CurrencyField()
    endowment_p3 = models.CurrencyField()
    endowment_p4 = models.CurrencyField()
    endowment_p5 = models.CurrencyField()
    endowment_p6 = models.CurrencyField()
    endowment_p7 = models.CurrencyField()
    endowment_p8 = models.CurrencyField()

    def set_other_decisions(self):
        self.decision_p1 = self.get_player_by_id(1).decision
        self.endowment_p1 = self.get_player_by_id(1).endowment

        self.decision_p2 = self.get_player_by_id(2).decision
        self.endowment_p2 = self.get_player_by_id(2).endowment

        if Constants.players_per_group >= 3:
            self.decision_p3 = self.get_player_by_id(3).decision
            self.endowment_p3 = self.get_player_by_id(3).endowment

        if Constants.players_per_group >= 4:
            self.decision_p4 = self.get_player_by_id(4).decision
            self.endowment_p4 = self.get_player_by_id(4).endowment

        if Constants.players_per_group >= 5:
            self.decision_p5 = self.get_player_by_id(5).decision
            self.endowment_p5 = self.get_player_by_id(5).endowment

        if Constants.players_per_group >= 6:
            self.decision_p6 = self.get_player_by_id(6).decision
            self.endowment_p6 = self.get_player_by_id(6).endowment

        if Constants.players_per_group >= 7:
            self.decision_p7 = self.get_player_by_id(7).decision
            self.endowment_p7 = self.get_player_by_id(7).endowment

        if Constants.players_per_group >= 8:
            self.decision_p8 = self.get_player_by_id(8).decision
            self.endowment_p8 = self.get_player_by_id(8).endowment



class Player(BasePlayer):

    decision= models.CharField(choices=["Default","Repay"],
        verbose_name= "What is your choice: Default or Repay?",
        doc= "The data of the choices"
        )

    defaulted = models.BooleanField(choices=[(True, "Yes"), (False, "No")],
        verbose_name='Defaulted or Repay the credit back?'
        )

    the_probability= models.PositiveIntegerField(min=0,
        max=1,
        doc= 'What is the probability of shock?',
        )

    endowment = models.CurrencyField()
        

    def calculate_the_probability(self):
        self.the_probability = random.random()

    def set_endowment(self):
        if self.the_probability <= Constants.shock_probability : 
            self.endowment = c(0)
            self.decision = 'Default'
        else:
            self.endowment = c(200000)

    age = models.PositiveIntegerField(
            max=100,
            verbose_name="How old are you?",
            doc="collect age data between 0 and 100"
        )
   
    gender = models.CharField(
            choices= ["Female", "Male", "Neither"],
            widget=widgets.RadioSelect(),
            verbose_name="What is your gender?",
            doc="what the participants' gender"
        )

    student_status= models.BooleanField(
            widget=widgets.CheckboxInput(),
            verbose_name="I am a student",
            choices=[(True, "Yes"), (False, "No")]
        )


    field_of_studies = models.CharField(
            verbose_name="What do you study if at all?",
            doc="free text input of field of studies",
            blank=True      
        )
    
    
    risk_profile = models.PositiveIntegerField(
            choices = [
                [1, "Very Low"],
                [2, "Low"],
                [3, "Close to Medium"],
                [4, "Medium"],
                [5, "Higher than Medium"],
                [6, "High"],
                [7, "Very High"],

            ],
            widget=widgets.RadioSelect(),
            verbose_name= "Willingness to take risk with Likert Scale",
            doc= "risk profile of the participants"
        )

    nationality = models.CharField(
            choices= ["Germany","Austria","Switzerland","Liechtenstein","Netherlands","Belgium","Czechia","Poland","Luxembourg","Turkey","Canada","USA","Other"],
            verbose_name= "Nationality?",
            doc= "the information of the nationalities of the participants"
        )


        
    



