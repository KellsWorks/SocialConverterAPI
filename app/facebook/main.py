import urllib.request

class Facebook(object):

    def __init__(self):
        super(Facebook, self).__init__()
    
    def convert(self, url):

        response = urllib.request.urlopen(url)
        video_content = response.read()

        return video_content

    