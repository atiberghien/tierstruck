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

  var villesEtapes = [
    {"nom" : "Mende", "coord" : [44.52063000, 3.49660000]},
    {"nom" : "Langogne", "coord" : [44.7269, 3.85472]},
    {"nom" : "St Chély d'Apcher", "coord" : [44.8012469, 3.2754536]},
    {"nom" : "Fournels", "coord" : [44.8172, 3.11806]},
    {"nom" : "Marvejols", "coord" : [44.5528, 3.28917]},
    {"nom" : "Massegros", "coord" : [44.3091, 3.17264]},
    {"nom" : "Meyrueis", "coord" : [44.1783, 3.42972]},
    {"nom" : "Florac", "coord" : [44.3198, 3.5990]},
    {"nom" : "Pont-de-Montvert", "coord" : [44.3631, 3.74417]},
    {"nom" : "Villefort", "coord" : [44.43840, 3.93288]},
  ];

  var mesWaypoints = []

  for (var i = 0; i < villesEtapes.length; i++) {
    L.marker(villesEtapes[i].coord).addTo(mymap).bindPopup(villesEtapes[i].nom);
    mesWaypoints.push(villesEtapes[i].coord);
  }

  L.Routing.control({
      waypoints: mesWaypoints
  }).addTo(mymap);

  $(".leaflet-control-attribution").hide();
  $(".leaflet-control").hide();


});
