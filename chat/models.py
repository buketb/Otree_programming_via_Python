from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'chat'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def calculate_years_in_prison(self):
        list_of_players_in_group = self.get_players()
        player1 = list_of_players_in_group[0]
        player2 = list_of_players_in_group[1]

        if player1.decision == "stay silent" and player2.decision == "stay silent": 
            player1.years_in_prison = 1
            player2.years_in_prison = 1
            player1.others_decision = "stay silent"
            player2.others_decision = "stay silent"


        if player1.decision == "stay silent" and player2.decision == "betray":
            player1.years_in_prison = 3
            player2.years_in_prison = 0
            player1.others_decision = "stay silent"
            player2.others_decision = "betray"

        if player1.decision == "betray" and player2.decision == "stay silent":
            player1.years_in_prison = 0
            player2.years_in_prison = 3
            player1.others_decision = "betray"
            player2.others_decision = "stay silent"

        if player1.decision == "betray" and player2.decision == "betray":
            player1.years_in_prison = 2
            player2.years_in_prison = 2
            player1.others_decision = "betray"
            player2.others_decision = "betray"


class Player(BasePlayer):
    decision = models.CharField(choices=["stay silent", "betray"],
        verbose_name= "What do you prefer: stay silent or confess?",
        doc= "the data of the choices"
        )

    years_in_prison = models.PositiveIntegerField(
        verbose_name= "How many years will you stay in prison",
        doc= "the data of the years in prison")

    others_decision = models.CharField( choices=["stay silent", "betray"],
        verbose_name= "What is the other's choice?",
        doc= "the data of the other's choice"
        )