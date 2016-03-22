#!/usr/bin/python

#
# This is used to collect information from puppetdb database and generate data for Foreman
#

# By Puppet
import urllib2, urllib
import json
import os

# Global
url = 'http://localhost:8080/nodes'
data = {}
data['query'] = '[\"=\", [\"node\", \"active\"], true]'

url_values = urllib.urlencode(data)
full_url = url + '?' + url_values
f = urllib2.urlopen(full_url)
j = json.load(f)

for b in j:
	result = os.system('curl -k -H \"Accept: yaml\" https://127.0.0.1:8140/production/facts/%s > /var/puppet/yaml/facts/%s.yaml' % (b,b) )

os.system('sudo -u puppet /etc/puppet/node.rb --push-facts')
