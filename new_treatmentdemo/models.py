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
    name_in_url = 'TheNewTreatmentDemo'
    players_per_group = None
    num_rounds = 1

    low_pot_size = c(100)
    high_pot_size = c(1000)

class Subsession(BaseSubsession):
    def before_session_starts(self):
        for player in self.get_players():
            # player.endowment = random.choice([Constants.low_pot_size, Constants.high_pot_size])

            if 'treatment' in self.session.config:
            	player.treatment = self.session.config['treatment']
            else:
            	player.treatment = random.choice(['low', 'high'])
            
            player.endowment = Constants.high_pot_size if player.treatment == "high" else Constants.low_pot_size

            # if player.treatment == "high":
            #     player.endowment =  Constants.high_pot_size
            # else:
            #     player.endowment = Constants.low_pot_size



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    the_bet = models.CurrencyField(
        verbose_name="How much do you want to bet?",
        doc = "the data about amount of bet",
        )

    the_probability = models.PositiveIntegerField(
        max=1, min=0,
        verbose_name = "What is the probability of winning",
        doc = "chance of win",
        )

    the_result = models.CurrencyField(
        verbose_name="How much will you earn with the bet?",
        doc = "the data about amount of rest of money",
        )

    the_totalendowment = models.CurrencyField(
        verbose_name="How much will you have in total?",
        doc = "the data about amount of the total money of the participant",
        )

    endowment = models.CurrencyField()

    treatment= models.CharField()

    def calculate_the_probability(self):
        self.the_probability = random.randint(0,1)

    def determine_result(self):
        if self.the_probability == 1:
            self.the_result = 2*self.the_bet
        else:
            self.the_result = self.endowment - self.the_bet

    def determine_the_totalendowment(self):
        if self.the_probability == 1:
            self.the_totalendowment = 2*self.the_bet + self.endowment
        else:
            self.the_totalendowment = self.the_result


    def the_bet_max(self):
        return self.player.endowment
        

    