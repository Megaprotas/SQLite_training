from sql_training.utils import db

USER_CHOICE = '''
Enter Your choice:
    Add new game - a,
    List book - l,
    Mark as played - r,
    Delete - d,
    quit - q
    
Your choice:
'''


def add_game():
    name = input('Enter game name: ')
    studio = input('Enter studio: ')

    db.add_game_db(name, studio)


def list_games():
    games = db.games_list()
    for game in games:
        played = 'YES' if game['played'] else 'NO'
        print(f"{game['name'].title()} made by {game['studio'].title()}. played already: {played.upper()}")


def mark_as_played():
    game = input('Enter the name of a game: ')
    db.mark_as_played_in_db(game)


def delete_game():
    game = input('Enter the name of a game: ')
    db.delete_game_from_db(game)


user_choice = {
    'a': add_game,
    'l': list_games,
    'r': mark_as_played,
    'd': delete_game
}


def choices():
    db.create_games_table()
    choice = input(USER_CHOICE)
    while choice != 'q':
        if choice in user_choice:
            selected_menu_function = user_choice[choice]
            selected_menu_function()

        else:
            print('Unknown command')

        choice = input(USER_CHOICE)


choices()