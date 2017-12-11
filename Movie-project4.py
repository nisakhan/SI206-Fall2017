
# Comparing the box office and revenue of Spider-Man movies on this particular movie database
# This is not 100 interactions, because there are not 100 Spider-Man and Batman movies.
# However, I thought this was an fair visualization of two large groups of information.
#I also thought this would be interesting and fun to look at.
# If anyone is interested, I am a fan of both, but skew towards Spider-Man.

import tmdbsimple as tmdb
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.graph_objs import *
import numpy as np
import sqlite3
import json


CACHE_FNAME = 'cache_movie.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

tmdb.API_KEY = 'c91e04b96d4fdc9e8879a1c5606be639'
S_search = tmdb.Search()
cache_file = open(CACHE_FNAME, "w")

S_response = S_search.movie(query='Spider-Man')

r = json.dumps(S_response)
cache_file.write(r)
cache_file.close()


movie_titles = []
S_boxoffice = []
money = []
budget1 = []
for a in S_search.results:
    d = tmdb.Movies(a["id"])
    dd = d.info()
    #print(type(dd))
    revenue1 = dd["revenue"]
    titles = dd["title"]
    money2 = dd["budget"]
    money.append(money2)
    budget1 = money[:6]
    #There are many, many animated and small productions of Spider-Man. I did this, as revenue is documented
    #With only the live-action Spider-Man productions. These are the only adaptations I wish to view.
    #There, I am eliminating all documentations in which there is 0 revenue.
    if revenue1 != 0:
        S_boxoffice.append(revenue1)
        movie_titles.append(titles)
        # CACHE_DICTION["user"] = x
        # f = open(CACHE_FNAME, 'w')
        # f.write(json.dumps(CACHE_DICTION))
        # f.close()
    # return(x)
connecting = sqlite3.connect('Movie-project4.sqlite')
cur = connecting.cursor()

cur.execute("DROP TABLE IF EXISTS Movies")
cur.execute("CREATE TABLE Movies (movie TEXT, budget TEXT, box_office TEXT )")
# numbers = [0,1,2,3,4,5,6,7]
for r in range(6):
    moviedata = (movie_titles[r], S_boxoffice[r], budget1[r])
    cur.execute('INSERT INTO Movies VALUES (?,?,?)',moviedata)
    connecting.commit()

plotly.tools.set_credentials_file(username='Nisakhan', api_key='sRxZpERQXNPuIZuPOgE4')

trace1 = go.Bar(
    x = movie_titles,
    y = S_boxoffice,
    name = "Box Office"
)
trace2 = go.Bar(
    x = movie_titles,
    y = budget1,
    name = "Budget"
)

data = [trace2, trace1]
layout = go.Layout(
    barmode="group"
)

fig = go.Figure(data=data, layout=layout)
py.iplot(data, filename='movie-bar')

#
# from os import path
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
#
# d = path.dirname(__file__)
#
# # Read the whole text.
# text = open(path.join(d, 'spider_man.txt')).read()
#
# # read the mask image
# # taken from
# # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
# spider_man_mask = np.array(Image.open(path.join(d, "spider-man_mask.png")))
#
# stopwords = set(STOPWORDS)
# stopwords.add("said")
#
# wc = WordCloud(background_color="black", max_words=3000, mask=spider_man_mask,
#                stopwords=stopwords)
# # generate word cloud
# wc.generate(text)
#
# # store to file
# wc.to_file(path.join(d, "spiderman.jpg"))
#
# # show
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.figure()
# plt.imshow(spider_man_mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.axis("off")
# plt.show()
