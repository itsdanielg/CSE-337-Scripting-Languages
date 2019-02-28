from flask import render_template, redirect, url_for, session
from forms import SubmissionForm
from textanalyzer import app
import re
from collections import Counter

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SubmissionForm()
    if form.validate_on_submit():
        text = form.text.data
        radio = form.radio.data
        delimiters = form.delimiters.data
        session['text'] = text
        session['delimiters'] = delimiters
        if (radio == 'wc'):
            return redirect(url_for('wordcount'))
        elif (radio == 'cc'):
            return redirect(url_for('charactercount'))
        else:
            return redirect(url_for('frequent'))
    return render_template('index.html', form=form)

@app.route('/result/wordcount')
def wordcount():
    text = session.get('text', None)
    delimiters = session.get('delimiters', None)
    delimiterArg = '\s'
    for i in range(len(delimiters)):
        delimiterArg += '|'
        delimiterArg += delimiters[i]
    strList = re.split(delimiterArg, text)
    strList = list(filter(None, strList))
    wordCount = len(strList)
    return render_template('wordcount.html', text=text, strList=strList, wordCount=wordCount)

@app.route('/result/charactercount')
def charactercount():
    text = session.get('text', None)
    lenText = len(text)
    return render_template('charactercount.html', text=text, lenText=lenText)

@app.route('/result/frequent')
def frequent():
    text = session.get('text', None)
    delimiters = session.get('delimiters', None)
    delimiterArg = '\s'
    for i in range(len(delimiters)):
        delimiterArg += '|'
        delimiterArg += delimiters[i]
    strList = re.split(delimiterArg, text)
    strList = list(filter(None, strList))
    counter = Counter(strList)
    frequent = counter.most_common(5)
    return render_template('frequent.html', text=text, frequent=frequent)

@app.errorhandler(403)
def not_found_error(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

