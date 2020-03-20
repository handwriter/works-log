from flask import Flask, render_template, url_for, redirect, request
from static.data import db_session
from static.data.users import User
from static.data.jobs import Jobs
from datetime import datetime
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    config = {'title': 'Works log',
              'db_jobs': session.query(Jobs).all(),
              'db_users': session.query(User).all(),
              'd_list': []}
    for i in session.query(Jobs).all():
        try:
            config['d_list'].append(str(datetime.fromisoformat(i.end_date) - datetime.fromisoformat(i.start_date)))
        except:
            config['d_list'].append('Unknown')
    # print(datetime.fromisoformat(config['mdr'][0].end_date) - datetime.fromisoformat(config['mdr'][0].start_date))
    return render_template('works_log.html', **config)


if __name__ == '__main__':
    db_session.global_init("static/db/blogs.sqlite")
    session = db_session.create_session()
    app.run(port=8080, host='127.0.0.1')