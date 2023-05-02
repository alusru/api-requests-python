import random
import requests
import json


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def joke():
    api = "https://official-joke-api.appspot.com/jokes/random"
    get_joke = requests.get(api)
    data = json.loads(get_joke.text)
    setup = data['setup']
    punch_line = data['punchline']
    print(f"---Random {data['type']} joke---")
    print(setup)
    print(punch_line)


def joke_by_category():
    category = random.choice(['general', 'programming', 'knock-knock'])
    api = f"https://official-joke-api.appspot.com/jokes/{category}/random"
    get_joke = requests.get(api)
    data = json.loads(get_joke.text)

    for i in data:
        print(f"--- {category} joke ---")
        print(i['setup'])
        print(i['punchline'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    joke()
    joke_by_category()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
