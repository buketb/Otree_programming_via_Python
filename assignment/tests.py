from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

from otree.api import SubmissionMustFail

class PlayerBot(Bot):
    

    def play_round(self):
        yield(views.Instructions)
        if self.player.endowment == c(200000):
            yield(views.NoShockInfo,{"decision":"Default"})
        else:
            yield(views.ShockInfo)
        if self.session.config['treatment'] == 'full_info':
            yield(views.Observations_full)
        else:
            yield(views.Observations_part)
        yield(views.Demographics, {
            "age": 25,
            "gender": "Male",
            "student_status": "Yes",
            "field_of_studies": "Economics",
            "risk_profile": 2,
            "nationality": "Germany"
        })

    def play_round(self):

        yield(views.Instructions)
        if self.player.endowment == c(200000):
            yield(views.NoShockInfo,{"decision":"Default"})
        else:
            yield(views.ShockInfo)
        if self.session.config['treatment'] == 'full_info':
            yield(views.Observations_full)
        else:
            yield(views.Observations_part)
        yield(views.Demographics, {
            "age": 35,
            "gender": "Male",
            "student_status": "Yes",
            "field_of_studies": "Economics",
            "risk_profile": 6,
            "nationality": "Turkey"
        })

    def play_round(self):

        yield(views.Instructions)
        if self.player.endowment == c(200000):
            yield(views.NoShockInfo,{"decision":"Default"})
        else:
            yield(views.ShockInfo)
        if self.session.config['treatment'] == 'full_info':
            yield(views.Observations_full)
        else:
            yield(views.Observations_part)
        yield(views.Demographics, {
            "age": 35,
            "gender": "Female",
            "student_status": "Yes",
            "field_of_studies": "Philosophy",
            "risk_profile": 1,
            "nationality": "Turkey"
        })

    # def play_round(self):

    #     yield(views.Instructions)
    #     if self.player.endowment == c(200000):
    #         yield(views.NoShockInfo,{"decision":"Default"})
    #     else:
    #         yield(views.ShockInfo)
    #     if self.session.config['treatment'] == 'full_info':
    #         yield(views.Observations_full)
    #     else:
    #         yield(views.Observations_part)
    #     yield SubmissionMustFail(views.Demographics, {
    #         "age": 35,
    #         "gender": "Female",
    #         "student_status": "",
    #         "field_of_studies": "Economics",
    #         "risk_profile": 1,
    #         "nationality": "Turkey"})
    #     yield SubmissionMustFail(views.Demographics,{
    #         "age": 35,
    #         "gender": "Female",
    #         "student_status": "Yes",
    #         "field_of_studies": "",
    #         "risk_profile": 1,
    #         "nationality": "Turkey"
    #     }) 
    #     yield(views.Demographics,{
    #         "age": 35,
    #         "gender": "Female",
    #         "student_status": "Yes",
    #         "field_of_studies": "Economics",
    #         "risk_profile": 1,
    #         "nationality": "Turkey"
    #         })