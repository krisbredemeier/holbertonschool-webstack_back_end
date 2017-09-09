#!/usr/bin/python3

'''
Listening on the port 5000, bound publically (0.0.0.0)
GET /c must return "C is fun!"
You must use the option strict_slashes=False in your route definition
Your code should not be executed when imported
(by using if __name__ == "__main__":)
'''


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def run_flask():
    '''
    retrun text from / route
    '''
    return "Holberton School"


@app.route('/c', methods=['GET'])
def retunC():
    '''
    return text from /c route
    '''
    return "C is fun!"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
