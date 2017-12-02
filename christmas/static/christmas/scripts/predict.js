if(typeof(Storage) !== "undefined"){
  document.getElementById("address").value = localStorage.getItem("searchedAddress");
}

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 5,
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
  }
  function geocodeAddress(geocoder, resultsMap) {
    var address = document.getElementById('address').value;
    if(typeof(Storage) !== "undefined") {
      localStorage.setItem("searchedAddress", address);
    }
    geocoder.geocode({'address': address}, function(results, status) {
      if (status === 'OK') {
        var loc = results[0].geometry.location;
        window.location.href="/predict/" + loc.lat() + "/" + loc.lng();
      } 
      else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
  }