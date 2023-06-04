
async function initMap() {

    // acquire json file 
    
    let waypoints=[];
    //;const place_point= await fetch("../json_funtion_test/sample_route_data.json")

  let place_point;

  // replace html  code to normal code for json parsing
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
  

       // var temp_content;

       let post_data=new Map();
       post_data.set("start", [place_point["start"]["placeName"], route.legs[0].duration.text,route.legs[0].distance.text] );

       console.log("route leg");
       console.log( route.legs.length);
     
        if (route.legs.length==1){
          summaryPanel.innerHTML =place_point["start"]["placeName"] + " to ";
          summaryPanel.innerHTML+=place_point["end"]["placeName"] +  "<br>";
          summaryPanel.innerHTML += route.legs[0].duration.text + "<br>";
          summaryPanel.innerHTML += route.legs[0].distance.text + "<br><br>";
        }

        /* For each route, display summary information. */
        else{
          for (let i = 0; i < route.legs.length; i++) {
            const routeSegment = i + 1;
        
            
            summaryPanel.innerHTML +=
              "<b>Route Segment: " + routeSegment + "</b><br>";


              if (routeSegment == 1){

                post_data.set(routeSegment ,[ wp[[route.waypoint_order[i]]]["placeName"]  ,route.legs[i].duration.text,route.legs[i].distance.text ]);
                  summaryPanel.innerHTML += place_point["start"]["placeName"] + " to ";
                  summaryPanel.innerHTML += wp[[route.waypoint_order[i]]]["placeName"] + "<br>";
                  summaryPanel.innerHTML += route.legs[i].duration.text + "<br>";
                  summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
              }

            else if (routeSegment == route.legs.length){
                  console.log("final leg")
                  
                  post_data.set("final" ,[ place_point["end"]["placeName"]  ,route.legs[i].duration.text,route.legs[i].distance.text ]);
                  summaryPanel.innerHTML += wp[[route.waypoint_order[i-1]]]["placeName"] + " to ";
                  summaryPanel.innerHTML +=  place_point["end"]["placeName"] +  "<br>";
                  summaryPanel.innerHTML += route.legs[i].duration.text + "<br>";
                  summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
                  
              }else{

                post_data.set(routeSegment ,[ wp[[route.waypoint_order[i]]]["placeName"]  ,route.legs[i].duration.text,route.legs[i].distance.text ]);
                  summaryPanel.innerHTML +=wp[[route.waypoint_order[i-1]]]["placeName"] + " to ";
                  summaryPanel.innerHTML +=wp[[route.waypoint_order[i]]]["placeName"] + "<br>";
                  summaryPanel.innerHTML += route.legs[i].duration.text + "<br>";
                  summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
                  


              }
            
      
        }
      }
       post_data.set("end", place_point["end"]["placeName"]);

       console.log(JSON.stringify(Object.fromEntries(post_data)));

       /*steralize data to json format*/
       const serializedData = JSON.stringify(Object.fromEntries(post_data));

      
       console.log(serializedData)

      /* post to flask */
       $.ajax({
        url: "/post_waypoint_order",
        contentType: "application/json",
        type: 'POST',
        data: serializedData,
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
        });



        /* pass sth back form flask , possibily scheudle object for creating itneray*/

  
      })


  }
  
window.initMap = initMap;