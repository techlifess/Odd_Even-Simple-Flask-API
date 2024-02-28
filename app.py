from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/odd_even/<int:n>', methods=['GET'])
def odd_even(n):
    if n % 2 == 0:
        result ={
            'Even':n
        }
        return jsonify(result)
    else:
        result ={
            'Odd':n
        }
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)