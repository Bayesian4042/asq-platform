from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression



def remove_pattern(intput_text, pattern):
	r = re.findall(pattern, input_text)
	for i in r:
		input_txt = re.sub(i, '', input_text)

	return input_txt


def count_punct(text):
	count = sum([1 for char in text if char in string.punctuation])
	return round(count / (len(text) - len(text.count(" "))), 3) * 100



app = Flask(__name__)

@app.route("/")
def hello_asq():
	target = os.environ.get('TARGET', 'HELLO ASQ')
	return "Hello {}".format(target)


if __name__ == '__main__':
	app.run(port = int(os.environ.get('PORT', 8000)), debug = True, host = '0.0.0.0')
