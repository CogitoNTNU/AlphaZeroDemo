# from TicTacToe import Gamelogic
import MCTS
import MCTSTraining
import ResNet
# from TicTacToe import Config
import os

from FourInARow import Config
from FourInARow import Gamelogic

game = Gamelogic.FourInARow()
config = Config

# Creating the NN
h, w, d = game.get_board().shape
agent = ResNet.ResNet.build(h, w, d, 128, config.policy_output_dim, num_res_blocks=10)
agent2 = ResNet.ResNet.build(h, w, d, 128, config.policy_output_dim, num_res_blocks=10)

# Creating the MCTS
# tree = MCTS.MCTS(game, game.get_board(), agent, Config)
# # tree.dirichlet_noise = False
# tree.NN_input_dim = config.board_dims
# tree.policy_output_dim = config.policy_output_dim
# tree.NN_output_to_moves_func = config.NN_output_to_moves
# tree.move_to_number_func = config.move_to_number
# tree.number_to_move_func = config.number_to_move
# tree.set_game(game)
tree = MCTSTraining.MCTS()
tree.NN_output_to_moves_func = Config.NN_output_to_moves
tree.number_to_move_func = Config.number_to_move
tree.move_to_number_func = Config.move_to_number
tree.policy_output_dim = Config.policy_output_dim
tree.dirichlet_noise = False



for opponent in os.listdir("Models/FourInARow/"):
    won = 0
    sum = 0
    draw = 0
    agent.load_weights("Models/FourInARow/10_5_121.h5")
    agent2.load_weights("Models/FourInARow/" + opponent)

    for player_start in range(2):
        for start in range(7):
            for next_start in range(7):
                game.__init__()
                game.execute_move(start)
                game.execute_move(next_start)
                tree.set_game(game)
                while not game.is_final():
                    if game.get_turn() == player_start:
                        tree.set_evaluation(agent)
                    else:
                        tree.set_evaluation(agent2)
                    tree.search_series(2)
                    game.execute_move(tree.get_most_searched_move(game.get_state()))
                    tree.reset_search()
                won += game.get_outcome()[player_start] == 1
                draw += game.get_outcome()[player_start] == 0
                sum += 1
    print("Result against", opponent, "-", won, "/", draw, "/", sum - won - draw)
