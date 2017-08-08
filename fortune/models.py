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
    name_in_url = 'fortune'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    the_bet = models.FloatField(
        max=100,
        verbose_name="How much do you want to bet?",
        doc = "the data about amount of bet"
        )

    the_probability = models.FloatField(
        verbose_name = "What is the probability of winning",
        doc = "chance of win",
        )

    the_result = models.CurrencyField()

    def calculate_the_probability(self):
        self.the_probability = random.randint(0,1)

    def determine_result(self):
        if self.the_probability == 1:
            self.the_result = 2*self.the_bet
        else:
            self.the_result = 100 - self.the_bet


        #self.the_probability = random.choice(["Win","Lose"])  # with charfield
            
   
    
