
def game(a, b, correct_answers=0, count=1):

    for i, j in a.items():
        if i in b:
            continue
        else:
            print(f'{count}. ' + i)
            answer = input('Answer ')
            if not answer.lower() in ['a', 'b', 'c', 'd']:
                print('Wrong choice, start game again...')
                b = {}
                return game(a, b)

            if answer == j:
                b.setdefault(i, j)
                correct_answers += 1
                if correct_answers == 5:
                    return 'You Win'
        count += 1
        if count == 6:
            print('return your game while you win')
            return game(a, b)
    else:
        return 'You Lose'



questions = {'What is the capital city of Armenia? \na) Tbilisi , b) Baku, c) Yerevan, d) Ankara': 'c',
     'Can you name some famous landmarks or historical sites in Armenia? \na) Great Wall of China b) Eiffel Tower c) Tatev Monastery d) Sydney Opera House': 'c',
     'What is the significance of Mount Ararat in Armenian culture? \na) It is a holy site for Hindu pilgrims b) It is a symbol of national pride and identity c) It is an ancient Greek temple site d) It is a popular skiing destination': 'b',
     'What are some traditional Armenian dishes or foods? \na) Sushi b) Tacos c) Dolma d) Pizza': 'c',
     'What is the history of Christianity in Armenia? \na) Islam is the predominant religion b) Buddhism is the predominant religion c) Armenia was the first nation to adopt Christianity as its state religion d) Atheism is the predominant belief system': 'c',
     'How has Armenia been influenced by neighboring countries and empires throughout history? \na) It has been isolated from outside influences b) It has been heavily influenced by Persian culture c) It has been subject to various invasions and occupations d) It has remained culturally unchanged for centuries': 'c',
     'What is the current political situation in Armenia? \na) Stable democracy with no political tensions b) Ongoing conflict with neighboring countries c) Authoritarian regime with strict control d) Recent democratic reforms but challenges remain': 'd',
     'How has Armenia been affected by conflicts in the region, such as the Nagorno-Karabakh conflict? \na) Loss of lives and displacement of people b) Economic sanctions imposed on Armenia c) No impact on Armenia  d) Peaceful resolution of conflicts': 'a',
     'What language is spoken in Armenia? \na) Spanish and French b) Armenian c) English and German d) Mandarin and Arabic': 'b',
     'What are some notable Armenian cultural traditions or customs? \na) Oktoberfest celebrations b) Lavash bread making c) Cherry blossom festivals d) St. Patricks Day parades': 'b',
     'Can you name some famous landmarks or historical sites in Armenia? \na) Statue of Liberty b) Great Wall of China c) Garni Temple d) Eiffel Tower': 'c',
     'What is the significance of Mount Ararat in Armenian culture? \na) It is a symbol of Greek mythology b) It is a sacred mountain and symbol of Armenian identity c) It is a dormant volcano in Japan d) It is a popular tourist destination for skiing': 'c',
     'What are some traditional Armenian dishes or foods? \na) Sushi b) Tacos c) Khorovats d) Pasta': 'c',
     'What is the history of Christianity in Armenia? \na) Armenia has always been a Muslim-majority country b) Armenia adopted Christianity as its state religion in the 4th century c) Armenia has a Hindu majority d) Christianity has no historical significance in Armenia': 'b',
     'What is the current political situation in Armenia? \na) Stable democracy with no political tensions b) Ongoing conflict with neighboring countries c) Recent democratic reforms but challenges remain d) Authoritarian regime with strict control': 'c',
     'What are some notable Armenian cultural traditions or customs? \na) Oktoberfest celebrations b) Cherry blossom festivals c) Armenian Genocide Remembrance Day d) St. Patricks Day parades': 'c'}

cor_questions = dict()

print(game(questions, cor_questions))
