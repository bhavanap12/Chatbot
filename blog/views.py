from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False,
               logic_adapters = [
                   {
                       'import_path':'chatterbot.logic.BestMatch',
                    #    'default_response':"Sorry, I don't know what that means",
                    #    'maximum_similarity':0.90
                   }
               ])

list_to_train = [
    "Hi",
    "Hi, there",
    "what's your name?",
    "I'm just a chatbot",
    "What is your favourite food?",
    "I like Cheese"
]

chatterbot_corpus_trainer = ChatterBotCorpusTrainer(bot)
# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)
chatterbot_corpus_trainer.train('chatterbot.corpus.english')

# Create your views here.
def home(request):
    title = "Chatbot App"
    context = {
        "title": title 
    }
    return render(request, "home.html", context)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    responseMessage = str(bot.get_response(userMessage))
    return HttpResponse(responseMessage)
