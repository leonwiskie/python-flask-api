from flask import Flask, jsonify
app = Flask(__name__)

debiteuren = [
    { 
        'id':1,
     'naam': 'LINKIT B.V.',
     'adres':'Rijnzathe 9',
     'postcode':'3454 PV',
     'plaats':'De Meern',
     'mailadres':'facturen@linkit.nl',
     'debnr':'D009',
     'tarief':92,
     'betaaltermijn':30
    },
    {
     'id':2,
     'naam': 'LINKIT B.V.',
     'adres':'Rijnzathe 9',
     'postcode':'3454 PV',
     'plaats':'De Meern',
     'mailadres':'facturen@linkit.nl',
     'debnr':'D010',
     'tarief':92.50,
     'betaaltermijn':30
    },
]




@app.route('/api/v1/debiteuren', methods=['GET'])
def get_debiteuren():
    return jsonify({'debiteuren': debiteuren})

if __name__ == '__main__':
    app.run(host='0.0.0.0')