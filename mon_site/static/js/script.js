$(document).foundation();

$(document).ready(function(){


  var mymap = L.map('mapid',
                    {scrollWheelZoom:false ,
                    dragging:false,
                    zoomControl:false}).setView([44.52063000, 3.4990000], 8);

  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    doubleClickZoom: false,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(mymap);
  var marker = L.marker([44.52063000, 3.49660000]).addTo(mymap).bindPopup("Mende");
  var marker = L.marker([44.7269, 3.85472]).addTo(mymap).bindPopup("Langogne"); // Langogne
  var marker = L.marker([44.8012469, 3.2754536]).addTo(mymap).bindPopup("St Chély d'Apcher"); // Saint Chély
  var marker = L.marker([44.8172, 3.11806]).addTo(mymap).bindPopup("Fournels"); // Fournels
  var marker = L.marker([44.5528, 3.28917]).addTo(mymap).bindPopup("Marvejols"); // Marvejols
  var marker = L.marker([44.3091, 3.17264]).addTo(mymap).bindPopup("Massegros"); // Massegros
  var marker = L.marker([44.1783, 3.42972]).addTo(mymap).bindPopup("Meyrueis"); // Meyrueis
  var marker = L.marker([44.3198, 3.5990]).addTo(mymap).bindPopup("Florac"); // Florac
  var marker = L.marker([44.3631, 3.74417]).addTo(mymap).bindPopup("Pont-de-Montvert"); // Pont-de-Monvert
  var marker = L.marker([44.43840, 3.93288]).addTo(mymap).bindPopup("Villefort"); // Villefort
  $(".leaflet-control-attribution").hide();

  L.Routing.control({
  waypoints: [
    L.latLng(44.52063000, 3.49660000),
    L.latLng(44.7269, 3.85472),
    L.latLng(44.8012469, 3.2754536),
    L.latLng(44.8172, 3.11806),
    L.latLng(44.5528, 3.28917),
    L.latLng(44.3091, 3.17264),
    L.latLng(44.1783, 3.42972),
    L.latLng(44.3198, 3.5990),
    L.latLng(44.3631, 3.74417),
    L.latLng(44.43840, 3.93288),
  ]
}).addTo(mymap);

$(".leaflet-control").hide();


});
