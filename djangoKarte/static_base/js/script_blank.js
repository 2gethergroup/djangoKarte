



function ubaci(feature, layer){
layer.bindPopup('<h1 class="infoHead"> Ovo je stanica</h1> <p class="infoHead">'
	+ feature.properties.name +'</p></div>');
layer.setIcon(marker);

};

/*var proba=L.geoJson(vreme2,{
	onEachFeature: ubaci
}).addTo(map);
*/

/*var markers= new L.MarkerClusterGroup();
var tacke=L.geoJson(vreme,{
	onEachFeature:ubaci
});

markers.addLayer(tacke);
map.addLayer(markers);
*/



