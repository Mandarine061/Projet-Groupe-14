def create_board():
    """
    """

def create_players_dictionary():
    """
    """

def create_board_dictionary(board):
    """
    """
def execute_orders(order):
    """
    """


def grass_growth(nbr_of_game_rounds, board_dictionnary, player):
    """
    """

def sheep_fights(board_dictionnary, order):
    """
    """
def move_sheep(board_dictionnary, order):
    """
    """
def capture_seeds(board_dictionnary, order):
    """
    """

def check_end_game():
    """
    """
def execute_orders(order):
    """This function executes orders provided for a single game round.
    
    Parameters
    ----------
    order: The given order by the player(string)
    
    returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)
    
    """
def sheep_apparition():
    """
    """
board_dictionary = {'rocks':[(1,2), (3,6), (9,11), (4,16)], 
                    'map':(20,20), 
                    'spawn':[(12,5), (6,8)],
                    'seeds':[(13,13), (3, 4), (6,8), (9,8)]}
             
             
players_dictionary = {'player_1':{'sheep':[[1,[3,6]], [3,[6,6]]],
                      'grass': [[2, [4, 12]], [2, [5, 12]], [2, [4, 11]], [2, [4, 13]]]},
                      'player_2':{'sheep':[[2,[15,17]], [2,[6,12]]],
                      'grass': [[11, [16, 13]], [1, [16, 12]], [1, [17, 13]], [1, [15, 13]], [1, [16, 14]]]}}


def play_game(file_name, player_1, player_2):
    """This function plays a game of Battle Sheep using the provided board file and player strategies.

    Parameters:
    ----------
    file_name:The name of the file describing the game board.(string)
    player_1: The strategy/order of player 1.(string)
    player_2: The strategy/order of player 2.(string)

    Returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)
    implementation : Malak El Maimouni (v1 18/03/2024)

    """
    round_num = 0
    board = create_board(file_name)
    board_dictionary = create_board_dictionary(board)
    players_dictionary = create_players_dictionary

    for round_num in range(20):
        # Player 1's turn
        order = player_1(board_dictionary,players_dictionary)
        execute_orders(order, players_dictionary, board_dictionary)

        # Player 2's turn
        order = player_2(board_dictionary, players_dictionary)
        execute_orders(order, players_dictionary, board_dictionary)

        # Perform automatic actions (grass growth, sheep fights, etc.)
        grass_growth(board_dictionary)
        sheep_fights(board_dictionary)
        move_sheep(board_dictionary)
        capture_seeds(board_dictionary)

        # Check for end game condition

        if check_end_game(board_dictionary):
            round_num +=1
            print(f"Game over after {round_num + 1} rounds.")
            return

    # Game over after 20 rounds
    print("Game over after 20 rounds.")

def execute_orders(orders):
    """This function executes orders provided for a single game round.
    
    Parameters
    ----------
    order: The given order by the player(string)

    Returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)
    implementation : Malak El Maimouni (v1 18/03/2024)

    
    """
    for order in orders:
        action = order.split('_')
        if action == 'S':
          sheep_apparition(board_dictionary, int([0]), int([1]), int([2]))
        elif action == 'M':
            move_sheep(board_dictionary, int([0]), int([1]), int([2]), int([3]))
        elif action == 'C':
            capture_seeds(board_dictionary, int([0]), int([1]))
        elif action == 'E':
            check_end_game(board_dictionary)
    return board_dictionary


def sheep_apparition(board_dictionary, player, order, nbr_of_grass_tiles):
    """This function allows a sheep to appear each time a player has 30 more grass tiles

    Parameters:
    -----------
    board_dictionary: Represents the current state of the game board.(dict)
    player: Indicates the player's number whose turn it is to make a sheep appear (1 or 2).(int)
    order: Specifies the order for sheep appearances.(str)
    nbr_of_grass_tiles: The total number of grass tiles of the player.(int)

    Returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)
    implementation : Malak El Maimouni (v1 18/03/2024)
    
    """
    # r représente la ligne et c représente la colonne
    if nbr_of_grass_tiles >= 30:
        for spawn in board_dictionary['spawn']:
            r= spawn
            c = spawn
            if board_dictionary['board'][r][c] == 0:
                board_dictionary['board'][r][c] = player
                nbr_of_grass_tiles -= 30
                board_dictionary[f'player_{player}']['sheep'].append([player, [r, c]])


def check_end_game(board_dictionnary, nbr_of_game_rounds):
    """This function checks whether the game has ended based on the given conditions.
    
    Parameters:
    -----------
    board_dictionnary: The current state of the game board.(dict)
    nbr_of_game_rounds: The total number of game rounds played.(int)
    
    Returns
    Result: 'True' if the game has ended, otherwise it returns 'False'.(bool)

    Version
    -------
    specification: Malak El maimouni (v1 26/02/2024)
    implementation : Malak El Maimouni (v1 18/03/2024)
    """
    total_grass= 0
    for player in board_dictionary:
        if player != 'rocks' and player != 'map' and player != 'spawn':
            for grass in board_dictionary[player]:
                grass_count = grass[0]
                total_grass += grass_count

    if total_grass > 100 or nbr_of_game_rounds >= 20:
        return True

    return False

            