from flask import Flask, render_template, request, make_response
import requests

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():

    if request.method == 'GET':
        return render_template('latex.html')

    if request.method == 'POST':
        url = 'https://www.writelatex.com/docs'
        payload = {'snip_uri': request.form['snip_uri']}
        r = requests.post(url, payload)
        return render_template('latex.html', data=r.url)




if __name__ == "__main__":
	# app.debug = True
    app.run()