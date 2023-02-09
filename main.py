from config import *
from check_smith import *
from schedule import schedule
import logging
from time import sleep
import tweepy
import traceback


logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

# schedule()

def initialize_api():
    api = CreateApi()
    return api

def smithLoop(api):
    num = 0
    while True:
        print(num)
        if(isSmith(num)):
            api.update_status(num)
            print(f'{num} is a Smith Number')
        else:
            print(f'{num} is not a Smith Number')
            num  += 1
        sleep(60)



def loop(api):
    while True:
        try:
            smithLoop(api)
        except Exception as e:
            print(f'\Exception:\n{e}\n\n{traceback.format_exc()}\n\n')
            sleep(600)
            continue


if __name__ == "__main__":
    api = initialize_api()
    loop(api)







