#!/usr/bin/env python3

import skynet
import pprint

if __name__=='__main__':
	try:
		#Get a list of all games from the server
		server='https://skynet.cs.uaf.edu'
		games=skynet.list_games(server)
		pprint.pprint(games)
		print()

		#Get info on a specific game
		game_name='test3'
		game_info=skynet.info_game(server,game_name)
		pprint.pprint(game_info)
		print()

		#Make a move (Empty object is good)
		board='rrrrrrrrr_rr_r______bbbbbbbbbbbb'
		game_move=skynet.play_game(server,game_name,board)
		pprint.pprint(game_move)

	except KeyboardInterrupt:
		exit(1)

	except Exception as error:
		print(error)
		exit(1)