# Importing Modules:
import pythonwhois

# Specifying what Domains:
domains = ['google.com', 'stackoverflow.com']

# Different Options for this module:
for dom in domains:
	details = pythonwhois.get_whois(dom)
	details['status']
	details['updated_date']
	details['whois_server']
	details['id']
	details['emails']
	details['expiration_date']
	details['contacts']
	#details['tech']
	#details['admin']
	#details['billing']
	#details['registrant']
	details['nameservers']
	details['creation_date']
	#details['registrar']
	# details['raw']
