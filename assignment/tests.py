from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

from otree.api import SubmissionMustFail

class PlayerBot(Bot):

    def play_round(self):

        invalid_age_data = {
            "age": -1,
            "gender": "Male"
            "student_status": "True",
            "field_of_studíes": "Economics",
            "risk_profile": "Low",
            "nationality": "Germany"
        }

        yield SubmissionMustFail(views.Demographics, invalid_age_data)

        invalid_status_data = {
            "age": 25,
            "gender": "Male"
            "student_status": "No",
            "field_of_studíes": "Economics",
            "risk_profile": "Low",
            "nationality": "Germany"
        }

        yield SubmissionMustFail(views.Demographics, invalid_status_data)

        invalid_status_data = {
            "age": 25,
            "gender": "Male"
            "student_status": "No",
            "field_of_studies": "Law",
            "risk_profile": "Low",
            "nationality": "Canada"
        }

        yield SubmissionMustFail(views.Demographics, invalid_status_data)

        invalid_status_data = {
            "age": 27,
            "gender": "Female"
            "student_status": "Yes",
            "field_of_studies": "",
            "risk_profile": "Low",
            "nationality": "Canada"
        }

        yield SubmissionMustFail(views.Demographics, invalid_status_data)

        invalid_status_data = {
            "age": 27,
            "gender": "Female"
            "student_status": "Yes",
            "field_of_studies": "qwert",
            "risk_profile": "Low",
            "nationality": "Canada"
        }

        yield SubmissionMustFail(views.Demographics, invalid_status_data)

        invalid_status_data = {
            "age": 27,
            "gender": "Female"
            "student_status": "Yes",
            "field_of_studies": "asdfghj",
            "risk_profile": "Low",
            "nationality": "Canada"
        }

        yield SubmissionMustFail(views.Demographics, invalid_status_data)


        valid_demograhics_data = {
            "age": 25,
            "gender": "Male"
            "student_status": "Yes",
            "field_of_studíes": "Economics",
            "risk_profile": "Low",
            "nationality": "Germany" 
        }
        yield (views.Demographics, valid_demograhics_data)
        assert self.player.age == 25
        assert self.player.gender == "Male"
        assert self.player.student_status == "Yes"
        assert self.player.field_of_studíes == "Economics"
        assert self.player.nationality == "Germany"
