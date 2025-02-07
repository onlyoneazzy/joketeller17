import requests
from pprint import pprint


def joke():

    url = "https://official-joke-api.appspot.com/random_joke"

    joke = requests.get(url).json()
    
    return joke


if __name__ == "__main__":
    print("\n*** Get a joke ***\n")

    _joke = joke()

    print("\n")
    pprint(_joke)