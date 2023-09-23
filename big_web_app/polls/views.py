from django.http import HttpResponse
from django.template import loader
from .models import BetaUser

def index(request):
    latest_question_list = BetaUser.objects.order_by("-reg_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)
