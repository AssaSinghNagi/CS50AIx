from pagerank import *

corpus = crawl('corpus0')
c = {'1.html': {'2.html'}, '2.html': {'3.html', '1.html'}, '3.html': {'2.html', '4.html'}, '4.html': {'2.html'}} 
print(iterate_pagerank(corpus,DAMPING))