
async function initMap() {

    // acquire json file 
    
    let waypoints=[];
    //;const place_point= await fetch("../json_funtion_test/sample_route_data.json")

  let place_point;
  let temp= locations_list.replaceAll('&#39;', '"');
  let temp2= temp.replaceAll('&#34;', "");

  
  
  place_point=JSON.parse(temp2);
  console.log(place_point);
 
  console.log(place_point['start']['placeName']);
  console.log(place_point['end']['placeName']);

    
  
    //create latlng obj for starting point
    let start=new google.maps.LatLng(place_point["start"]["lat"], place_point["start"]["lng"]);
    

    //create latlng obj for ending point
    let end=new google.maps.LatLng(place_point["end"]["lat"],place_point["end"]["lng"]);
  
    

    const data = place_point["waypoint"];

    for (var i =0 ; i < data.length; i++)
    {
        waypoints[i]=new google.maps.LatLng(data[i]["lat"],data[i]["lng"]);

    }




    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 6,
      center: { lat: 41.85, lng: -87.65 },
    });
  
    directionsRenderer.setMap(map);
   
    calculateAndDisplayRoute(directionsService, directionsRenderer, start, end, waypoints,place_point);
    
  }
  

  

  // customize function add start , end and waypoint(list of dict items)
  async function calculateAndDisplayRoute(directionsService, directionsRenderer,start, end, waypoints,place_point) {
    const waypts = [];
 
   
   
    const wp = place_point["waypoint"];
    console.log("start");
    console.log(start);
    console.log("end");
    console.log(end);
    

    // open file for dropping down time for each leg route
    

  
    for (let i = 0; i < waypoints.length; i++) {
      
        waypts.push({
          location:waypoints[i],
          stopover: true,
        });
      
    }
  
    directionsService
      .route({
        origin: start,
        destination: end,
        waypoints: waypts,
        optimizeWaypoints: true,
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC
      })
      .then((response) => {
        directionsRenderer.setDirections(response);
  
        const route = response.routes[0];

        console.log(route.waypoint_order);
        console.log(route.bounds);
        console.log(start);

        const summaryPanel = document.getElementById("directions-panel");
  
        summaryPanel.innerHTML = "";
  

        var temp_content;
        // For each route, display summary information.
        for (let i = 0; i < route.legs.length; i++) {
          const routeSegment = i + 1;
          temp_content+= route.legs[i].duration.text ;
          console.log(route.legs[i].duration.text );
  
          summaryPanel.innerHTML +=
            "<b>Route Segment: " + routeSegment + "</b><br>";
         // summaryPanel.innerHTML += route.legs[i].start_address + " to ";
          //summaryPanel.innerHTML += route.legs[i].end_address + "<br>";
          //summaryPanel.innerHTML += route.legs[i].duration.text + "<br>";
          //summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";

            if (routeSegment == 1){
                summaryPanel.innerHTML += place_point["start"]["placeName"] + " to ";
                summaryPanel.innerHTML += wp[[route.waypoint_order[i]]]["placeName"] + "<br>";
                summaryPanel.innerHTML += route.legs[i].duration.text + "<br>";
                summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
            }

           else if (routeSegment == route.legs.length){
                console.log("final leg")
                summaryPanel.innerHTML += wp[[route.waypoint_order[i-1]]]["placeName"] + " to ";
                summaryPanel.innerHTML +=  place_point["end"]["placeName"] +  "<br>";
                summaryPanel.innerHTML += route.legs[i].duration.text + "<br>";
                summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
                
            }else{

                
                summaryPanel.innerHTML +=wp[[route.waypoint_order[i-1]]]["placeName"] + " to ";
                summaryPanel.innerHTML +=wp[[route.waypoint_order[i]]]["placeName"] + "<br>";
                summaryPanel.innerHTML += route.legs[i].duration.text + "<br>";
                summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
                


            }
          
          //contents = summaryPanel.innerHTML.innerHTML;
          //fwrite(file, contents);
       }

       console.log(temp_content);
  
      })


  }
  
window.initMap = initMap;