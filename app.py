from flask import Flask,render_template,request,jsonify
from Projects.Instabot import image_handle, local_image
from Projects.tweeter import run_bot, retweet
from Projects.crawler import run
from time import sleep
import datetime



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/instabot', methods=['POST'])
def instabot():
    if request.form['tpic'] != '':
        photo_url = request.form['tpic']
        image_handle(photo_url,"Projects/image_name.jpg")
        return render_template('index.html',info = 'Okay Image was posted at https://instagram.com/culver_loons ')

    if request.files['file'] != '':
        photo = request.files['file']
        local_image(photo,"Projects/image_name.jpg")
        return render_template('index.html',info = 'Image was posted at https://instagram.com/culver_loons ')



@app.route('/redditbot', methods=['POST'])
def redditbot():
    subkey = request.form['subkey']
    keyword = request.form['redditkeyword']
    sub_list = run(subkey,keyword)
    return render_template('index.html',info = sub_list)


@app.route('/twitterbot',methods = ['POST'])
def twitterbot():
    keyword1,keyword2 = request.form['keyword1'],request.form['keyword2']
    tweeted_list = run_bot(keyword1,keyword2)
    tweet = retweet(tweeted_list)
    return render_template('index.html',info = tweet+' https://twitter.com/GOATconvo ')


@app.route('/num_projects',methods=['GET'])
def num_projects():
    path = Path('Projects')
    counter = 0
    for proj in path.iterdir():
        if '__' not in proj.parts[1]:
            counter +=1
    return jsonify({'value':counter})


if __name__ == '__main__':
    app.run(debug = True,threaded = True,use_reloader = False)
