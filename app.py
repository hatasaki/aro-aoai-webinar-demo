from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 + num2
    return jsonify({'result': result})

if __name__ == '__main__':
    #appを外部公開して起動
    app.run(host='0.0.0.0', port=5000)