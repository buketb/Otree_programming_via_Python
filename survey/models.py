from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
            max=120,
            verbose_name="How old are you?",
            doc="collect age data between 0 and 120"
        )
   
    gender = models.CharField(
            choices= ["female", "male", "neither"],
            widget=widgets.RadioSelect(),
            verbose_name="What is your gender?",
            doc="what the participants' gender"
        )

    field_of_studies = models.CharField(
            blank=True,
            verbose_name="what do you study if at all?",
            doc="free text input of field of field studies"
        )

    likes_experiment = models.CharField(
            choices= ["Yes, of course!", "No and I don't have a witty comment"],
            widget=widgets.RadioSelect(),
            verbose_name="Did you like the experiment?",
            doc="yes, no, maybe input as a string"
        )

    height = models.FloatField(
            verbose_name="What is your height?",
            doc="collect height data"
        )

    weight = models.FloatField(
             verbose_name="What is your weight?",
             doc="collect the weight data" 
        )
    BMI = models.FloatField(
        doc="collect the BMI from the participant")

    BMI_class = models.CharField()

    def calculate_bmi(self): 
        self.BMI = self.weight / self.height **2

    def classify_bmi(self):
     if 18.5<= self.BMI <= 25: 
        self.BMI_class= "Normal Weigth"

     if self.BMI<18.5:
        self.BMI_class= "Under Weight"

     if self.BMI>25:
        self.BMI_class= "Over Weight"
