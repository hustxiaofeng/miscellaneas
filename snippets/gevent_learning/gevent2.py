import gevent
import urllib2
from gevent import monkey
monkey.patch_all()


def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


def fn(n):
    for i in range(n):
        print i


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://github.com/'),
    gevent.spawn(fn, 10)
])

# f('https://www.python.org/')
# f('https://www.python.org/')
# f('https://www.python.org/')
# f('https://www.python.org/')
# f('https://www.python.org/')
# f('https://github.com/')
