from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model=models.Player
    form_fields=["the_bet"]

    def before_next_page(self):
        self.player.calculate_the_probability()
        # self.player.determine_endowment()
        self.player.determine_result()
        self.player.determine_the_totalendowment()

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]

