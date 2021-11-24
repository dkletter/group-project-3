-- Create table
CREATE table yelp_data (
	id SERIAL,
	name TEXT,
	address TEXT,
	city TEXT,
	state TEXT,
	postal_code TEXT,
	latitude DEC,
	longitude DEC,
	stars DEC,
	review_count INT,
	categories TEXT,
	PRIMARY KEY(id)
);