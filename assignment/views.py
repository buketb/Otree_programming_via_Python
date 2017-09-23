from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

    def before_next_page(self): 
        self.player.calculate_the_probability()
        self.player.set_endowment()

class WaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class NoShockInfo(Page): 

    form_model=models.Player
    form_fields= ['defaulted']
    form_fields=['decision']

    def is_displayed(self):
        return self.player.endowment == c(200000)


class ShockInfo(Page): 



    def is_displayed(self):
        return self.player.endowment == c(0) 


class WaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_other_decisions()

class Observations_full(Page):
    timeout_second= 120

    def is_displayed(self):
        return self.session.config['treatment'] == 'full_info'

        # this is the long form:
        #if self.session.config['treatment'] == 'full_info':
        #    return True
        #else:
        #    return False

    

class Observations_part(Page):
    timeout_second= 120

    def is_displayed(self):
        return self.session.config['treatment'] == 'part_info'

    

class WaitPage3(WaitPage):

    def after_all_players_arrive(self):
        pass


class Demographics(Page):
    form_model = models.Player
    form_fields = ["age", "gender","student_status", "field_of_studies", "risk_profile", "nationality"] # add student_status


page_sequence = [
    Instructions,
    WaitPage,
    NoShockInfo,
    ShockInfo,
    WaitPage2,
    Observations_full,
    Observations_part,
    WaitPage3,
    Demographics,
]