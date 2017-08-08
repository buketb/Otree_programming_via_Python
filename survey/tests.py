from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

from otree.api import SubmissionMustFail
 
class PlayerBot(Bot):

    def play_round(self):
        yield SubmissionMustFail(views.MyPage, {"height":1.00, "weight":100, "age": -5, "gender":'female', "field_of_studies":'economics', "likes_experiment": "Yes, of course!"})
        yield (views.MyPage, {"height":1.00, "weight":100, "age": 25, "gender":'female', "field_of_studies":'economics', "likes_experiment": "Yes, of course!"})
        assert self.player.BMI == 100 
        assert self.player.BMI_class == "Over Weight"

        yield (views.Results)
