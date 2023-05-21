from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    description = request.form.get('description', False)
    temp = request.form.get('temp', False)
    humidity = request.form.get('humidity', False)
    timezone = request.form.get('timezone', False)

    args = ['python', 'a.py', location]

    if description:
        args.append('--description')
    if temp:
        args.append('--temp')
    if humidity:
        args.append('--humidity')
    if timezone:
        args.append('--timezone')

    result = subprocess.run(args, capture_output=True, text=True)
    output = result.stdout

    return render_template('weather.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
