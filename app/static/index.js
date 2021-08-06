function savePlate() {
    var plate_number = document.getElementById('plate').value;
    $.ajax("/plate", {
        type: "POST",
        data: {plate: plate_number},
        statusCode: {
           200: function (response) {
            console.log("Response: " + response);
            $("#savePlateResponse").text('Response code: 200').removeClass().addClass('text-success');
           },
           400: function (response) {
            console.log("Response: " + response);
            $("#savePlateResponse").text('Response code: 400').removeClass().addClass('text-danger');
           },
           422: function (response) {
            console.log("Response: " + response);
            $("#savePlateResponse").text('Response code: 422').removeClass().addClass('text-danger');
           }
        }
    });
}