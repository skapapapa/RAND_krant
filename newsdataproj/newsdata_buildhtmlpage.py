import json

###load contents from file#################################################################################################################
def buildMyNewsFileName(myName = "JohnDoe"):
	from datetime import date
	import json
	# build the file's name
	today = str(date.today())
	fileName = ("_").join(["RandKrant", myName, today])
	return fileName
## ja dit is inderdaad dirty. ik ga er vanuit dat er vandaag al met de andere py file data is opgehaald


def loadNewsContentFromFile(filename = buildMyNewsFileName()):
	# read file
	import json
	import os
	path = os.path.join(os.getcwd(), "rawoutput")
	with open(path + "\\" + filename + ".json", "r") as readFile:
	    data = json.load(readFile)
	return data
	#json format

newscontent = loadNewsContentFromFile()
## it is an array of json objects (i.e. dictionaries)
##print(type(newscontent))
## print(type(newscontent[0]))

#######################################################################################################################

### do a little preprocessing here
### add 'random' header styles for each article. So the final paper will look more fancy and natural.
import random
primaryheaders = ["headline hl1", "headline hl3" , "headline hl5"]
secondaryheaders = ["headline hl2", "headline hl4" ,"headline hl6"]
for i in range(len(newscontent)):
	newscontent[i].update({"primaryheader": primaryheaders[i%3]})
	newscontent[i].update({"secondaryheader": random.choice(secondaryheaders)})

## building the date description we want to show on the paper
from datetime import date
import time
import locale
# Lokale taal omgeving wellicht eerst in te stellen met raspi-config
locale.setlocale(locale.LC_ALL, 'nl_NL')
today = date.today()
paperdate = today.strftime("%A %d %B %Y")



#######################################################################################################################
# use flask to build page

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/rawcontentpage')
def rawcontentpage():
	return render_template('rawpage.html', nc = newscontent)

@app.route('/prettycontentpage')
def prettycontentpage():
	return render_template('prettypage.html', nc = newscontent, pd = paperdate)

@app.route('/buttonpage')
def buttonpage():
	return render_template('buttonpage.html', pd = paperdate)

if __name__ == '__main__':
	app.run(debug = True)



