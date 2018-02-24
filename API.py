#!flask/bin/python
from flask import Flask, jsonify, request, make_response
from TicTacToe import *

app = Flask(__name__)


@app.route('/api/v1/tictactoe', methods=['POST'])
def post_tasks():
	ht = request.get_json()
	if ("playerSymbol" not in ht or "gameboard" not in ht):
		return make_response(jsonify({'error': 'Could not find playerSymbol and gameboard'}), 400)
	gameboard = ht["gameboard"]
	gameboard = [None if i=="?" else i for i in gameboard]
	tic = Tic(gameboard)
	tic.show()
	a = determine(tic,ht["playerSymbol"])
	tic.make_move(a, ht["playerSymbol"])
	gameboard = ["?" if i==None else i for i in tic.get_gameboard()]
	print("------------------")
	tic.show()
	return(jsonify(
		new_move=a,
		new_gameboard=gameboard
	))

if __name__ == '__main__':
	app.run(debug=True)


