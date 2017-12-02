 function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: {lat: 39.1836, lng: -96.5717}
    });
    var geocoder = new google.maps.Geocoder();
    document.getElementById('submit').addEventListener('click', function() {
      geocodeAddress(geocoder, map);
    });
    document.getElementById('address').addEventListener('keyup', function(event) {
      event.preventDefault();
      if(event.keyCode === 13){
        geocodeAddress(geocoder, map);
      }
      });
      google.maps.event.addListener(map, 'click', function(event) {
        loc = event.latLng;
        placeMarker(loc);
        if(typeof(Storage) !== "undefined") {
          geocodeLatLng(geocoder, map, loc);
        }
        window.location.href="/history/" + loc.lat() + "/" + loc.lng();
      });
      function placeMarker(location) {
          var marker = new google.maps.Marker({
              position: location, 
              map: map
          });
      }
  }
  function geocodeAddress(geocoder, resultsMap) {
    var address = document.getElementById('address').value;
    geocoder.geocode({'address': address}, function(results, status) {
      if (status === 'OK') {
        var loc = results[0].geometry.location;
        resultsMap.setCenter();
        var marker = new google.maps.Marker({map: resultsMap, position: loc});
        window.location.href="/history/" + loc.lat() + "/" + loc.lng();
      } 
      else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
  }

  function geocodeLatLng(geocoder, map, loc){//, infowindow) {
    geocoder.geocode({'location': loc}, function(results, status) {
      if (status === 'OK') {
        if (results[0]) {
          
          localStorage.setItem("searchedAddress", results[0].formatted_address);
        }
      } 
      else {
        window.alert('Geocoder failed due to: ' + status);
      }
    });
  }
