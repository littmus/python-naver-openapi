import urllib2


def get(request, user_agent):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', user_agent + ' urllib2')]
    
    try:
        response = opener.open(request)
        code = response.code
        data = response.read()
    except urllib2.URLError, e:
        return 500, str(e)
    except urllib2.HTTPError, e:
        code = e.code
        data = e.read()

    return code, data

