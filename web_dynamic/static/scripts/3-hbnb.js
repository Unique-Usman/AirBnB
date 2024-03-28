$(document).ready(function () {
   function updateApiStatus() {
        $.get('http://0.0.0.0:5001/api/v1/status/', function(data) {
            if (data.status === "OK") {
                $('#api_status').addClass('available');
            } else {
                $('#api_status').removeClass('available');
            }
        });
    }

    // Check the API status on page load
    updateApiStatus();

  let amenities = [];
  $('input[type="checkbox"]').change (function () {
    let amenityId = $(this).data('id');
    if ($(this).is(":checked")) {
      amenities.push(amenityId); 
    }else {
      let index = amenities.indexOf(amenityId);
      if (index !== -1) {
          amenities.splice(index, 1);
      }
    }
    console.log(amenities)
    let text = "";
        amenities.forEach(function(id) {
            let amenityName = $('input[type="checkbox"][data-id="' + id + '"]').data("name");
            text += amenityName + ", ";
        });

        text = text.slice(0, -2); // Remove the last comma and space
        $('.amenities h4').text("Checked Amenities: " + text);
  }) 

  function fetchPlaces() {
    return $.ajax({
      url: 'http://0.0.0.0:5001/api/v1/places_search/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({})
    });
  }

  // Function to create HTML elements for each place and append them to the DOM
  function renderPlaces() {
    fetchPlaces().done(function(places) {
      let placesSection = $('.places');

      $.each(places, function(index, place) {
        let article = $('<article>');
        article.html(`
          <h2>${place.name}</h2>
          <p>${place.description}</p>
          <p>Price per night: $${place.price_by_night}</p>
        `);
        placesSection.append(article);
      });
    });
}

// Call renderPlaces to fetch data and render HTML elements
renderPlaces();
})
