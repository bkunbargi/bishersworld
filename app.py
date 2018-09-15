from flask import Flask,render_template,request,jsonify
#import urllib.request as req
from Projects.Instabot import run_insta,image_handle,local_image
from Projects.tweeter import run_bot, run_analysis,respond_to,retweet
from Projects.crawler import run,responder
from time import sleep
import datetime



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projecto')
def projecto():
    return render_template('projecto.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/instabot', methods=['POST'])
def instabot():
    photo_loc = "Projects/image_name.jpg"
    caption = request.form['caption']
    if request.form['tpic'] != '':
        photo_url = request.form['tpic']
        #req.urlretrieve(photo_url, photo_loc)
        run_insta(image_handle,photo_url, photo_loc,caption)
        #image_handle(photo_url,"Projects/image_name.jpg")
        return render_template('index.html',info = 'Okay Image was posted at https://instagram.com/culver_loons ')

    if request.files['file'] != '':
        photo = request.files['file']
        run_insta(local_image,photo,photo_loc,caption)
        #local_image(photo,"Projects/image_name.jpg")
        return render_template('index.html',info = 'Image was posted at https://instagram.com/culver_loons ')



@app.route('/redditbot', methods=['POST'])
def redditbot():


    if request.form['subkey'] != '' and request.form['redditkeyword'] != '':
        sub_list = run(request.form['subkey'],request.form['redditkeyword'])
        return render_template('index.html',info = sub_list)
    if request.form['madecomment'] != '' and request.form['subid'] != '' and request.form['uresponse'] != '':
        made_comment = request.form['madecomment']
        sub_id = request.form['subid']
        u_response = request.form['uresponse']
        responder(sub_id,made_comment,u_response)
        return render_template('index.html',info = 'Responded to comment')




@app.route('/twitterbot',methods = ['POST'])
def twitterbot():
    if request.form['user_tweet'] != '' and request.form['responderhandle'] != ''  and request.form['statusid'] != '' :
        respond_to(request.form['responderhandle'],request.form['user_tweet'],request.form['statusid'])
        tweeted = request.form['user_tweet']
        return render_template('index.html',info = tweeted+' https://twitter.com/GOATconvo ')
    if request.form['user_tweet'] != '':
        tweeted = retweet(request.form['user_tweet'])
        return render_template('index.html',info = tweeted+' https://twitter.com/GOATconvo ')
    if request.form['keyword1'] != '':
        keyword1 = request.form['keyword1']
        tweeted_list = run_bot(keyword1)
        min_t,max_t = run_analysis(tweeted_list)
        return render_template('index.html',info = 'Most Negatively Polarizing: '+min_t+'\n'+'Most Positively Polarizing: '+max_t+'https://twitter.com/GOATconvo')


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
