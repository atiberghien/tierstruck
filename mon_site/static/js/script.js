$(document).foundation();

$(document).ready(function(){


  var mymap = L.map('mapid').setView([44.494203, 3.581269], 10);
  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(mymap);

});
