from riotwatcher import LolWatcher, ApiError
import pandas as pd

# global variables
API_KEY = 'RGAPI-736fc9af-0b1a-445e-b7ff-2af12b7d7353'
watcher = LolWatcher(API_KEY)
my_region = 'na1'
me = watcher.summoner.by_name(my_region, 'Fawaz')

if __name__ == '__main__':
    # Get all the information for summoner 'me'
    for i in me:
        print(str(i) + ': ' + str(me[i]))

    print('\n')

    # Return the solo queue rank status for summoner 'me'
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    # Use my_ranked_stats[1] for flex rank
    for i in my_ranked_stats[0]:
        print(str(i) + ': ' + str(my_ranked_stats[0][i]))