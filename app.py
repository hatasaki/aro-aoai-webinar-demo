from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    # クエリパラメータから数値を取得
    num1 = request.args.get('num1', type=int)
    num2 = request.args.get('num2', type=int)

    # 加算結果を計算
    result = num1 + num2

    # 結果をJSON形式で返す
    return jsonify({'result': result})

if __name__ == '__main__':
    # サーバを公開して起動
    app.run(host='0.0.0.0', port=5000)