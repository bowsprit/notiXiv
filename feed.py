import feedparser

class Article():
    """ Object where I can store all my articles, which I love
    """

    def __init__(thing, stuff, other_thing):
        self.thing = thing
        self.stuff = stuff
        self.other_thing = other_thing

base_url = 'http://export.arxiv.org/api/query'
search_string = 'all'
sort_by = 'lastUpdatedDate'
sort_order = 'descending'
start = 0
max_results = 200

query_url = base_url + '?search_query=%s&start=%i&max_results=%i&sortBy=%s&sortOrder=%s' % (search_string, start, max_results, sort_by, sort_order)

def pull_feed(url_to_query):
    feed_results = feedpaser.parse(url_to_query)

def save_feed(feed_to_save, output_file_name):
    """ This will return a JSON parsing error. Ignore for now
    """
    with open(output_file_name, 'w') as outfile:
        json.dump(feed_to_save, outfile, indent = 4)
