import tweepy
import time
import string
import random
class TwitterAPI:
    def __init__(self):
    	#insert own consumerkey, consumer secret, access token and access token secret 
    	#these can be found on your twitter account
        consumer_key = ''
        consumer_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ""
        access_token_secret = ""
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)


def readFile(path):#readfile
    with open(path, "rt") as f:
        return f.read()

def generateProfile():
#randomly selects a tempalte and generates the post
	template = random.randint(1,4)
	if template ==1:
		content = template1()
	if template == 2:
		content = template2()
	if template == 3:
		content = template3()
	if template ==4:
		content = template4()
	profile = generateName()+'\n'+content
	if len(profile)>140:
		profile = generateProfile()
	return profile

def collapseWhitespace(s):#return string with no spaces
    result=""
    for c in s:
        if c == '\n':
            continue
        else:
            result+=c
    return result   

def generateName():#generates a genus and species
	genus = collapseWhitespace(readFile("genus.txt")).split(".")
	genint = random.randint(0,len(genus)-1)
	species = collapseWhitespace(readFile("species.txt")).split(".")
	specint = random.randint(0,len(species)-1)
	name = genus[genint] + " " +species[specint]
	return name

def generateLoc():#generates location
	locations = collapseWhitespace(readFile("location.txt")).split('.')
	locint = random.randint(0,len(locations)-1)
	return locations[locint]

def aAn(adj):#generates a or an
	for vowel in "aeiou":
		if adj.startswith(vowel):
			return "An"
	return "A"

def generateAct():#generates an action
	actions = collapseWhitespace(readFile("action.txt")).split(".")
	actint = random.randint(0,len(actions)-1)
	return actions[actint]
	
def generatePhys():# generates a physical feature
	physicals = collapseWhitespace(readFile("phys.txt")).split('.')
	physint = random.randint(0,len(physicals)-1)
	return physicals[physint]

def generateNoun():#generates a noun
	nouns = collapseWhitespace(readFile('nouns.txt')).split(".")
	nounint = random.randint(0,len(nouns)-1)
	return nouns[nounint]

def generateAdj():#generates an adjective
	adjectives = collapseWhitespace(readFile("adj.txt")).split(".")
	adjint = random.randint(0,len(adjectives)-1)
	return adjectives[adjint]

def template1():#chooses words for template1
	adj = generateAdj()
	location = generateLoc()
	action1 =generateAct()
	action2 = generateAct()
	noun1 = generateNoun()
	noun2 = generateNoun()
	start = aAn(adj)
	result = ("%s %s sea creature that dwells in %s, often seen %s %s or %s %s."
		% (start,adj, location,action1,noun1,action2,noun2))
	return result

def template2():#chooses words for template2
	adj = generateAdj()
	location = generateLoc()
	action1 =generateAct()
	action2 = generateAct()
	noun1 = generateNoun()
	noun2 = generateNoun()
	start = aAn(adj)
	result = ("%s %s sea creature spotted in %s. It is believed to love %s %s and %s %s."
		% (start,adj,location,action1,noun1,action2,noun2))
	return result

def template3():#chooses words for template3
	location = generateLoc()
	action = generateAct()
	noun = generateNoun()
	date = ('%d/%d/%d' % (random.randint(1,12),random.randint(1,31),random.randint(100,2015)))
	result = ("A sea creature spotted %s %s in %s on %s."
			% (action,noun, location,date))
	return result

def template4():#chooses words for template 4
	phys1 = generatePhys()
	phys2 = generatePhys()
	adj1 = generateAdj()
	adj2 = generateAdj()
	act = generateAct()
	noun = generateNoun()
	result = ("A sea animal with %s %s and %s %s, also has a habit of %s %s." % (adj1,phys1,adj2,phys2,act,noun))
	return result
	
#runfuncion
if __name__ == "__main__":
	for n in range(20):
	    twitter = TwitterAPI()
	    twitter.tweet(generateProfile())
	    time.sleep(180)