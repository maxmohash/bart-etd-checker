from lxml import etree
import urllib


# Here is the list of abbreviations to be used for all BART reachable stations:
# https://api.bart.gov/docs/overview/abbrev.aspx
from_station = "Mont"
to_station = "Dublin/Pleasanton"
# MW9S-E7SL-26DU-VV8V is the api access key provided by http://www.bart.gov/schedules/developers/api
# But you are encouraged to get your access key from here https://api.bart.gov/api/register.aspx
bart_api_access_key = "MW9S-E7SL-26DU-VV8V"
# Northbound train has dir=n where n is for North.
# In case of southbound train you need to change this to dir=s where s is South in the url below
url = "https://api.bart.gov/api/etd.aspx?cmd=etd&orig={}&dir=n&key={}".format(from_station, bart_api_access_key)
root = etree.parse(urllib.urlopen(url))


def get_count_of_destination():
	count_stations = []
	for dest in root.xpath('/root/station/etd/destination'):
		count_stations.append(dest)
	return count_stations


def get_bart_etd():
	counter = 0
	loop = 0
	for destination in root.xpath('/root/station/etd/destination'):
		loop += 1
		if loop > len(get_count_of_destination()):
			print "Sorry! It looks like BART is not available for your destination right now!"
		if destination.text == to_station:
			for x in root.xpath('/root/station/etd/estimate/minutes'):
				counter += 1
				if x.text == "Leaving":
					print x.text, "Now"
				else:
					print "Next train to {} from {} in".format(to_station, from_station), x.text, "minutes"
					if counter == 3:
						break
			break

get_bart_etd()
