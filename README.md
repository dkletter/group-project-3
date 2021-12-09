# group-project-3

Our proposal is to look at restaurants in Portland, Oregon. We belive there's an interesting story to tell about nightlife and its variety of options. Our dashboard will have a searchable map of the most popular restaurants with clickable pins, a heat map, and supporting charts.

Portland, Oregon is a city with a population of 652,503 packed into 144.98 square miles, making it the second-most populous city in the Pacific Northwest.

In order to answer our key question “where do you want to go tonight?", we turned to the Yelp academic data set. It’s a collection of very large JSON files covering a few key cities in the United States and Canada. We originally wanted to use Yelp’s API because it has some additional data points such price and hours of operation which would have been ideal for plotting on a line chart, but surprisingly we found there’s a limit of 50 businesses within a maximum of 25 miles per search which was clearly insufficient.

Our ETL process was fairly straightforward. We removed any columns we didn’t need such as the `is_open` flag which has been implemented inconsistently, then narrowed the data set to filter by all restaurants in Portland, Oregon. This left us with a comfortable 5,730 rows of data to work with.

From there, we converted the data frame to GeoJSON format which would accommodate our leaflet maps, before finally uploading to a mongoDB.

We chose a mongoDB over SQL because it was more flexible in handling GeoJSON coordinates.

Upon analysis of the data, we found some interesting statistics. There are 4,975 unique restaurants. In other words, counting a chain as 1 business instead of several. The maximum number of reviews a restaurant received was 9,185 while the average number of reviews is 128. The overall number of top rated restaurants, those with 4.5 stars or greater, is 1,019.

Going deeper, the number of restaurants with 4.5 stars or greater and 128 ore more reviews is 1,177. This number decreases as the number of reviews increases. The number of restaurants with 4.5 stars or greater and 300 or more reviews is 461. The number of restaurants with 4.5 stars or greater and 500 or more reviews is only 196.

Turns out there are 2,626 restaurants or 53% of all restaurants in the Yelp data set that are still in business. In general, we know 17% of all restaurants fail in the first year. However, failure isn't the same as closure. A thriving business may be forced to close due to family or health problems. Or the building is sold, forcing the restaurant out of business. If there was more time, we would have liked to know how Portland restaurants still in business compare to other cities.

Possibly least surprising, we found the most top rated restaurants clustered in the downtown area.

![heat map](images/Heatmap-Screen-Shot.png)
