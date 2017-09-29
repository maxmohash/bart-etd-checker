from lxml import etree
import urllib


# Here is the list of abbreviations to be used for all BART reachable stations:
# https://api.bart.gov/docs/overview/abbrev.aspx
from_station = "Mont"
to_station = "Dublin/Pleasanton"
# MW9S-E7SL-26DU-VV8V is the api access key provided by http://www.bart.gov/schedules/developers/api
# But you are encouraged to get your access key from here https://api.bart.gov/api/register.aspx
url = "https://api.bart.gov/api/etd.aspx?cmd=etd&orig={}&key=MW9S-E7SL-26DU-VV8V".format(from_station)
root = etree.parse(urllib.urlopen(url))


def get_bart_etd():
	for dest in root.xpath('/root/station/etd/destination'):
		if dest.text == to_station:
			for x in root.xpath('/root/station/etd/estimate/minutes'):
				if x.text == "Leaving":
					print x.text, "Now"
				else:
					print "Next train in", x.text, "minutes"
		else:
			print "Looks like no train is available at this time!"

get_bart_etd()
