from question_model import Questions
from data import question_list

question_bank = []

for i in question_list:
    question_bank.append(Questions(i['text'],i['answer']))

print(question_bank[0].text)