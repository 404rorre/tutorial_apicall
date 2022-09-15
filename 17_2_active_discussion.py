import requests
from plotly.graph_objs import Bar
from plotly import offline
import json
from operator import itemgetter

#Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

submissions_ids = r.json()
submission_dicts = []

for submission_id in submissions_ids[:30]:
	#Seperate API call for each ID
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tStatus Code: {r.status_code}")
	response_dict = r.json()
	hn_link = f"http://news.ycombinator.com/item?id={submission_id}"
	hyperlink = f"<a href='{hn_link}'>{response_dict['title']}</a>"
	#Built dictionary with the required intel
	try: 
		submission_dict = {
			"hyperlink" : hyperlink,
			"titles" : response_dict["title"],
			"comments" : response_dict["descendants"],
			}
	except KeyError:
		print(f"KeyError occured\tid: {submission_id}")
		submission_dict = {
			"hyperlink" : hyperlink,
			"titles" : response_dict["title"],
			"comments" : 0,
			}
	submission_dicts.append(submission_dict)

#Use dict as sorting tool
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"),
							reverse=True)

#Converting to lists for plotly
comments, hyperlinks, titles = [], [], []
for submission_dict in submission_dicts:
	comments.append(submission_dict["comments"])
	hyperlinks.append(submission_dict["hyperlink"])
	titles.append(submission_dict["titles"])


data = [{
	"type" : "bar",
	"x" : hyperlinks,
	"y" : comments,
	"hovertext" : titles,
	"marker" : {
		"color" : "rgb(60, 100, 150)",
		"line" : {
			"width" : 1.5, 
			"color" : 
			"rgb(25, 25, 25)",
			}
		},
	"opacity" : 0.6
	}]

my_layout = {
	"title" : "Most interacted articles on Hacker-News",
	"titlefont" : {"size" : 28},
	"xaxis" : {
		"title" : "Repository",
		"titlefont" : {"size" : 24},
		"tickfont" : {"size" :14},
		},
	"yaxis" : {
		"title" : "Stars",
		"titlefont" : {"size" : 24},
		"tickfont" : {"size" :14},
		}
	}

fig = {
	"data" : data,
	"layout" : my_layout,
	}

offline.plot(fig, filename="articles_hacker-news.html")

