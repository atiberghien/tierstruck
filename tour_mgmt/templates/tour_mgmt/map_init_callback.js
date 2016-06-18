function map_init_basic_{{tour.id}} (map, options) {
    map.touchZoom.disable();
    map.dragging.disable();
    map.doubleClickZoom.disable();
    map.scrollWheelZoom.disable();
    map.boxZoom.disable();
    map.keyboard.disable();

    var stages = [
        L.Routing.waypoint(L.latLng(44.526,3.6), "Mende"),
        {% for stage in tour.stages.all %}
        L.Routing.waypoint(L.latLng({{stage.point.y|stringformat:".3f"}}, {{stage.point.x|stringformat:".3f"}}), "{{stage.name}}"),
        {% endfor %}
        L.Routing.waypoint(L.latLng(44.526,3.6), "Mende"),
    ];

    var bounds = []
    var routing = L.Routing.control({
        draggableWaypoints:false,
        addWaypoints:false,
        plan: L.Routing.plan(stages, {
			createMarker: function(i, wp) {
                bounds.push(wp.latLng);
				return L.marker(wp.latLng).bindPopup(wp.name);
			},
			routeWhileDragging: true
		}),
    }).addTo(map);


    routing.on('routesfound', function(e) {
        $("#distance_{{tour.id}}").html(Math.floor(e.routes[0].summary.totalDistance/1000));
        map.fitBounds(bounds)
    });
}
