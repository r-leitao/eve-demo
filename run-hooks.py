# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

from eve import Eve


def pyconby(endpoint, response):
    for document in response['_items']:
        document['PYCON BELARUS'] = 'IS SO FREAKING COOL!'

app = Eve()
app.on_fetched_resource += pyconby

if __name__ == '__main__':
    app.run()
