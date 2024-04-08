from flask import Flask, render_template, request
from flask_cors import CORS
import pyautogui

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/click', methods=['POST'])
def click():
    # Simulate a click at the center of the screen
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.click(screenWidth // 2, screenHeight // 2)
    return 'Click simulated successfully!'

if __name__ == '__main__':
    app.run(debug=True)
