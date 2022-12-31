from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

english_bot = ChatBot("Illya", storage_adapter="chatterbot.storage.SQLStorageAdapter", \
  logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'What is your nane?',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        }
    ]
)
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
exit_conditions = (":q", "quit", "exit")


while True: 
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪢{english_bot.get_response(query)}")
