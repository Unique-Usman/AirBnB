$(document).ready(function () {
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

})
