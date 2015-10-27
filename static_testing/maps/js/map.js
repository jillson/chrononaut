var iconStore = {"new": L.icon({iconUrl: baseIconURL + "greendot.png"}),
		 "completed": L.icon({iconUrl:baseIconURL + "bluedot.png"}),
		 "locked": L.icon({iconUrl:baseIconURL + "greydot.png"}),
		 "danger": L.icon({iconUrl:baseIconURL + "alarm.gif"})}

function Adventure(adv)
{
    this.id = adv.id;
    this.name = adv.name;
    this.lat = adv.lat;
    this.lng = adv.lng;
    this.state = adv.state;
    this.description = adv.description;
    this.link = adv.link;
    this.marker = L.marker([adv.lat,adv.lng],{icon: iconStore[adv.state]});
    
    if (adv.state != "locked")
    {
	this.marker.bindPopup("<strong>"+this.name+"</strong><br>" + this.description + "<br>" + this.link); 
	this.marker.addTo(map);
    }
    else
    {
	this.marker.bindPopup("This Adventure hasn't been unlocked").openPopup();
	this.marker.addTo(map);
    }
}

Adventure.prototype.clickme = function(evt)
{
    alert("Would do something");

}

advs = []

for (var ind in adventures)
{
    var adv = adventures[ind];
    advs.push(new Adventure(adv));
}
