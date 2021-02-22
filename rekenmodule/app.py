from flask import Flask, jsonify,request
app = Flask(__name__)

@app.route('/api/v1/rekenen', methods=['get'])
def get_facturen():
    uren = request.args.get('uren')
    tarief = request.args.get('tarief') 
    if(uren is not None and tarief is not None):
        uren = int(uren)
        tarief = int(tarief)
        omzet = uren * tarief
        inbtw = omzet * 1.21
        return jsonify({'omzet': omzet,'inbtw':inbtw})
    else:
        return jsonify({'omzet': 0,'inbtw': 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0') 