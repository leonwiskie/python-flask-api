from flask import Flask, jsonify
app = Flask(__name__)

facturen = [
    {
        'id':2,
        'debnr':'D010',
        'bedrag':10000
    }
]

@app.route('/api/v1/facturen', methods=['GET'])
def get_facturen():
    return jsonify({'facturen': facturen})
if __name__ == '__main__':
    app.run(host='0.0.0.0')