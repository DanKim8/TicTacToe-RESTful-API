#!flask/bin/python
from flask import Flask, jsonify, request, make_response


app = Flask(__name__)


@app.route('/api/v1/tictactoe', methods=['POST'])
def post_tasks():
	ht = request.get_json()
	if ("playerSymbol" not in ht or "gameBoard" not in ht):
		return make_response(jsonify({'error': 'Could not find playerSymbol and gameBoard'}), 400)
	return(request.data)

if __name__ == '__main__':
	app.run(debug=True)

