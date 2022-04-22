from flask import Flask, request, jsonify
import threading
import os
import time
app = Flask(__name__)

def update_database():
    while True:
        # i use a time.sleep and while loop since the timer thread didn't work
        time.sleep(600)
        print("Updating database")
        os.system("python server/fa-scraper.py")

# Start thread to update database
threading.Thread(target=update_database).start()

@app.route('/test')
def test():
    return jsonify({'message': 'test'})

if __name__ == '__main__':
    app.run()
