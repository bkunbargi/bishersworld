from flask import Flask,render_template,request,jsonify
import datetime
from time import sleep
from threading import Thread
from Projects.crawler import run
from Projects.Instabot import image_handle,local_image
from Projects.tweeter import run_bot, retweet
from pathlib import Path





app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/num_projects',methods=['GET'])
def num_projects():
    path = Path('Projects')
    counter = 0
    for proj in path.iterdir():
        if '__' not in proj.parts[1]:
            counter +=1
    return jsonify({'value':counter})



@app.route('/instabot', methods=['POST'])
def instabot():
    if request.form['tpic'] != '':
        photo = request.form['tpic']
        image_handle(photo,"Projects/image_name.jpg")
        return render_template('index.html',info = 'success')

    if request.files['file'] != '':
        photo = request.files['file']
        local_image(photo,"Projects/image_name.jpg")
        return render_template('index.html',info = 'Image was posted at https://instagram.com/straighthalal')



@app.route('/redditbot', methods=['POST'])
def redditbot():
    sub_list = run('nba','lebron')
    return render_template('index.html',info = sub_list)


@app.route('/twitterbot',methods = ['POST'])
def twitterbot():
    keyword1,keyword2 = request.form['keyword1'],request.form['keyword2']
    tweeted_list = run_bot(keyword1,keyword2)
    tweet = retweet(tweeted_list)
    return render_template('index.html',info = tweet+' https://twitter.com/GOATconvo')




if __name__ == '__main__':
    app.run(debug = True,threaded = True)
