$(document).foundation();

$(document).ready(function(){


  var mymap = L.map('mapid').setView([51.505, -0.09], 13);
  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(mymap);

});
