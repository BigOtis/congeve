# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'
#MONGO_AUTH_SOURCE = 'admin'  # needed if --auth mode is enabled

MONGO_DBNAME = 'Congress'

bt115 = {
    'item_title': 'Bill Text, 115th Congress',

    'additional_lookup': {
        'url': 'regex(".*")',
        'field': 'bill_id'
	},
		
    # Schema definition
	'schema': {	
		'bill_id': {
			'type': 'string',
			'minlength': 1,
			'maxlength': 11,
			'required': True,
			'unique': True,
		},
		'text': {
			'type': 'string',
			'minlength': 1,
		},
	}
}

bt114 = {
    'item_title': 'Bill Text, 114th Congress',

    'additional_lookup': {
        'url': 'regex(".*")',
        'field': 'bill_id'
	},
		
    # Schema definition
	'schema': {	
		'bill_id': {
			'type': 'string',
			'minlength': 1,
			'maxlength': 11,
			'required': True,
			'unique': True,
		},
		'text': {
			'type': 'string',
			'minlength': 1,
		},
	}
}

b115 = {
    'item_title': 'Bill Text, 114th Congress',

    'additional_lookup': {
        'url': 'regex(".*")',
        'field': 'bill_id'
	},
	
	# Schema definition
	'schema': {	
		'bill_id': {
			'type': 'string',
			'minlength': 1,
			'maxlength': 11,
			'required': True,
			'unique': True,
		},
		'bill_type': {
			'type': 'string',
		}
	}
}

b114 = {
    'item_title': 'Bill Text, 114th Congress',

    'additional_lookup': {
        'url': 'regex(".*")',
        'field': 'bill_id'
	},
	
	# Schema definition
	'schema': {	
		'bill_id': {
			'type': 'string',
			'minlength': 1,
			'maxlength': 11,
			'required': True,
			'unique': True,
		},
		'bill_type': {
			'type': 'string',
		},
		'short_title': {
			'type': 'string',
		},
		'official_title': {
			'type': 'string',
		},
		'subjects_top_term': {
			'type': 'string',
		},
	}
}

DOMAIN = {
		'People': {},
		'BillText-115': bt115, 
		'BillText-114': bt114, 
		'Bills-115': b115, 
		'Bills-114': b114, 						
}