from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatom_game'
    players_per_group = 2
    num_rounds = 1

    pot_size = c(100)

class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.group_randomly()

class Group(BaseGroup):
    proposed_share = models.PositiveIntegerField(
        max= Constants.pot_size,
        verbose_name = "How much do you keep for yourself?"
        )

    accepted = models.BooleanField(choices=[(True, "yes"), (False, "No")])

    def set_payoffs(self):
        proposer = self.get_player_by_role('proposer')
        responder = self.get_player_by_role('responder')

        if not self.accepted:
            responder.payoff = c(0)
            proposer.payoff = c(0)
        else:
            responder.payoff = c(self.proposed_share)
            proposer.payoff = Constants.pot_size - c(self.proposed_share)


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'proposer'
        else:
            return 'responder'
