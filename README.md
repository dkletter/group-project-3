# group-project-3

Our proposal is to look at restaurants in Portland, Oregon. We belive there's an interesting story to tell about nightlife and the variety of options. Our dashboard will have a searchable map of the most popular restaurants with clickable pins, a heat map, and supporting charts.

In order to answer our key question “where do we want to go tonight?", we turned to the Yelp academic data set. It’s a collection of very large JSON files covering a few key cities in the United States and Canada. We originally wanted to use Yelp’s API because it has some additional data points such price and hours of operation which would have been ideal for plotting on a line chart, but surprisingly we found there’s a limit of 50 businesses within a maximum of 25 miles per search which was clearly insufficient.

Our ETL process was fairly straightforward. We removed any columns we didn’t need such as the `is_open` flag which has been implemented inconsistently, then narrowed the data set to filter by all restaurants in Portland, Oregon. This left us with a comfortable 5730 rows of data to work with.

From there, we converted the data frame to GeoJSON format which would accommodate our leaflet maps, before finally uploading to a mongoDB.

We chose a mongoDB over SQL because it was more flexible in handling GeoJSON coordinates.


