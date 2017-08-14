// ----------------------------------------
// Markers
// ----------------------------------------
var markers = [];

// Delete All markers
function clearMarkers() {
		for (var i = 0; i < markers.length; i++) {
		  	markers[i].setMap(null);
		}
		markers = [];
}

function getPoints(targetMap) {

		clearMarkers();
//		var item = {lat:44.865394, lng:2.539036};
//		placeMarker(item, targetMap, 1)
		$.getJSON('/places/get/', function(data) {
			$.each(data, function(i, places) {
				$.each(places, function(i, place) {
					$.each(place, function(key, item) {
							var item = {title:item.title, lat:item.lat, lng:item.lng};
							placeMarker(item, targetMap, 1);
					});
				});
			});
		});

}

function placeMarker(item, targetMap, detail) {

		var location = {lat: item.lat, lng: item.lng};

		var marker = new google.maps.Marker({
			 position: location,
			 draggable: false,
			 animation: google.maps.Animation.DROP,
			 map: targetMap,
			 title: item.title
		});

		markers.push(marker);

		return marker;

}


// ----------------------------------------
// Map
// ----------------------------------------

function initMap() {
		var center = {lat: 44.865394, lng: 2.539036};
		var map = new google.maps.Map(document.getElementById('map'), {
				zoom: 6,
				center: center
		});

		getPoints(map);

}
