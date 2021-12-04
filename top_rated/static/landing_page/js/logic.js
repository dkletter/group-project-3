// Create BASE LAYERS
var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });


// Create a baseMaps object
var baseMaps = {
    "Street Map": street,
    "Topographic Map": topo
  };

// Initialize all of the LayerGroups we'll be using
var layers = {
    bestRestaurant: new L.LayerGroup(),
    goodRestaurant: new L.LayerGroup(),

};


// Define a map object
var myMap = L.map("map", {
	center: [45.5, -122.67],
	maxZoom:18,
	zoom: 11,
	layers: [
		layers.bestRestaurant,
		layers.goodRestaurant,
	]
});



// Create an overlay object to add to the layer control
var overlayMaps = {
	"5.0": layers.bestRestaurant,
	"4.5": layers.goodRestaurant,
};

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
  collapsed: false
}).addTo(myMap);


// Create function to filter data for a specific restaurant
// filter = Bars, Pizza, 
function filterData(data, reviewStars) {

	var restaurantData = data.filter(row => row.stars == reviewStars);
	var filteredData = restaurantData.map(function(d) {
		return {
			name: d.name,
			stars:d.stars,
			address: d.address,
			latitude: d.latitude,
			longitude: d.longitude   
		}
	});

	return filteredData;
}


// Create function to create an layer for each filtered restaurant data
function createLayer(filteredData) {

	var markers = L.markerClusterGroup();

	for (var i = 0; i < filteredData.length; i++) {
		var record = filteredData[i];

		var restaurantMarker = L.marker([record.latitude, record.longitude]);
		
		// bind a pop-up to show the some information on each restaurant
		restaurantMarker.bindPopup("<h3>" + record.name +
														"</h3><hr><p>" + record.address +  
														'<br>' + '[' + record.latitude + ', ' + record.longitude + ']' +
														'<br>' + 'Review: ' + record.stars + ' Stars' +"</p>");

		// Add a new marker to the cluster group and bind a pop-up
		markers.addLayer(restaurantMarker);    
	}

	return markers;
}

// Perform an api call to the data
d3.json("api/v1.0/restaurant").then(function(resData) {

	 //Loop through each key value pairs in the overlay Maps object
	Object.entries(overlayMaps).forEach(([key, value]) => {

		var filteredData = filterData(resData, key);
		var markers = createLayer(filteredData);

		// Add the marker cluster to the appropriate layer
		markers.addTo(value);
	});
})
