from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logo')
def logo():
    return send_file('./static/images/logo.png', mimetype='image/png')

@app.route('/Community')
def community():
    text = ''
    cmmt = ''
    with open('./templates/dynamic_content/hot_topic.txt', mode='r', encoding='utf-8') as tpc:
        text = tpc.read()
    
    with open('./templates/dynamic_content/comments.txt', mode='r', encoding='utf-8') as cmt:
         cmmt = cmt.read()

    return render_template('community.html', topic = text, comments=cmmt)

@app.route('/Events')
def events():
    new_event = ''
    old_event = ''
    with open('./templates/dynamic_content/new_event.txt', mode='r', encoding='utf-8') as nec:
        new_event = nec.read()
    
    with open('./templates/dynamic_content/past_event.txt', mode='r', encoding='utf-8') as oec:
         old_event = oec.read()

    return render_template('events.html', n_events = new_event, p_events = old_event)

@app.route('/postcomment', methods = ['POST', 'GET'])
def handleComment():
    if request.method == 'POST':
        comment = request.form['cmt_cnt']
        mod_comment = '<p class="cmmnts">' + comment + "</p>\n"
        with open('./templates/dynamic_content/comments.txt', mode='a', encoding='utf-8') as cmmtStr:
            cmmtStr.write(mod_comment)

    return redirect(url_for('community'))

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/update_events', methods = ['POST', 'GET'])
def updateE():
    if request.method == 'POST':
        new_evnt = request.form['n_e']
        pst_evnt = request.form['p_e']
        ht_tpc = request.form['h_t']
        with open('./templates/dynamic_content/new_event.txt', mode='w', encoding='utf-8') as ne:
            ne.write(new_evnt)

        with open('./templates/dynamic_content/past_event.txt', mode='w', encoding='utf-8') as pe:
            pe.write(pst_evnt)

        with open('./templates/dynamic_content/hot_topic.txt', mode='w', encoding='utf-8') as ht:
            ht.write(ht_tpc)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
