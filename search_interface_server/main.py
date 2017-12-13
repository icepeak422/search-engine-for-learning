from flask import *
from extensions import db
import config
import requests
from captureGoogleAPI import fetchRecords
from recommend import recommend5url
import json

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods = ['GET', 'POST'])
def wiki_route():
	if request.method == 'POST':
		recommend = True;
		rec5urls=[]
		data = request.get_json()['docs']
		[rec5urls,reasonret]=recommend5url(data)
		options = {
			# 'search': True,
			# 'recommend': recommend,
			'results': rec5urls,
			'reason_results': reasonret,
			'docs': data
		}
		return jsonify(options)

	else:
		search = False;
		docs = []
		query = request.args.get('q')
		urls=[]
		if query :
			search = True
			for k in range(0,2):
				allres=(fetchRecords(query, (k*10)+1))
				for i in range(0,len(allres)):
					urls.append(allres[i]["link"])
			print (len(urls))
				
		options = {
			'search': search,
			'docs': urls
		}
		return render_template("wikipedia.html", **options)
