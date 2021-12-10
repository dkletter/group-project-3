# group-project-3

Our proposal is to look at restaurants in Portland, Oregon. We belive there's an interesting story to tell about nightlife and its variety of options. Our dashboard will have a searchable map of the most popular restaurants with clickable pins, a heat map, and supporting charts.

Portland is a city with a population of 652,503 packed into 144.98 square miles, making it the second-most populous city in the Pacific Northwest.

In order to answer our key question “where do you want to go tonight?", we turned to the Yelp academic data set. It’s a collection of very large JSON files covering a few key cities in the United States and Canada. We originally wanted to use Yelp’s API because it has some additional data points such price and hours of operation which would have been ideal for plotting on a line chart, but surprisingly we found there’s a limit of 50 businesses within a maximum of 25 miles per search which was clearly insufficient.

Our ETL process was fairly straightforward. We removed any columns we felt we didn’t need, then narrowed the data set to filter by all restaurants in Portland. This left us with a comfortable 5,730 rows of data to work with.

From there, we converted the data frame to GeoJSON format which would accommodate our leaflet maps, before finally uploading to a mongoDB.

We chose a mongoDB over PostgreSQL because it was more flexible in handling GeoJSON coordinates.

Upon analysis of the data, we found some interesting statistics. There are 4,975 unique restaurants. In other words, counting any restaurant with more than 1 location as 1 business instead of several. The maximum number of reviews a restaurant received was 9,185 (Voodoo Doughnuts) while the average number of reviews is 128. The overall number of top rated restaurants, those with 4.5 stars or greater, is 1,019. The data set doesn't distinguish between good and bad reviews, but at first blush the results suggest people tend to leave more negative reviews more often.

Going deeper, the number of restaurants with 4.5 stars or greater and 128 ore more reviews is 1,177. This number decreases as the number of reviews increases. The number of restaurants with 4.5 stars or greater and 300 or more reviews is 461. The number of restaurants with 4.5 stars or greater and 500 or more reviews is only 196.

Turns out there are 2,626 restaurants or 53% of all restaurants in the Yelp data set that are still in business. In general, we know about 17% of all restaurants fail in the first year. However, failure isn't the same as closure. A thriving business may be forced to close due to family or health problems. Or the building is sold, forcing the restaurant out of business. If there was more time, we would have liked to know how this statistic compares to other cities.

We identified Food, Bars, and Nightlife as the top 3 categories under Restaurants:

**categories** | **count**
----- | -----
Food | 7,263
Bars | 637
Nightlife | 273
**Grand Total** | **8,173**

Important note: the Yelp data set allows for restaurants to be counted under multiple categories. For example, a bar can serve beer, burgers, and pizza, counting it in 3 subscategories. This is why the total number of categories is greater than the actual number of restaurants.

Overall, the top 10 subcategories are as follows:

**subcategories**  |**count**
----- | -----
Sandwiches | 446
Breakfast & Brunch | 423
Food Trucks | 411
American (Traditional) | 393
Food Stands | 351
American (New) | 348
Coffee & Tea | 339
Mexican | 330
Burgers | 237
Pizza | 227
**Grand Total** | **3,505**

The top 10 types of bars are:

**subcategories** | **count**
----- | -----
Pubs | 145
Cocktail Bars | 142
Sports Bars | 81
Wine Bars | 76
Dive Bars | 53
Beer Bar | 50
Tapas Bars | 31
Whiskey Bars | 14
Brewpubs | 11
Pool Halls | 10
**Grand Total** | **613**

Whereas the top 10 types of restaurants are:

**subcategories** | **count**
----- | -----
Cafes | 210
Delis | 109
Sushi Bars | 86
Juice Bars & Smoothies | 57
Diners | 47
Gastropubs | 35
Steakhouses | 31
Buffets | 18
Food Court | 18
Coffee Roasteries | 18
**Grand Total** | **629**

If we had more time, it would be interesting to see how this breaks down when fast food chains are removed from the mix. Perhaps least surprising, we found the most top rated restaurants clustered in the downtown area.

![heat map](images/Heatmap-Screen-Shot.png)
