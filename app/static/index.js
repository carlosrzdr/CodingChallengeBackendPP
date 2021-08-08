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

function retrievePlates() {
    $.get( "/plate", function( data ) {
        console.log(data)
        var platesListData = '';
        $.each(data, function(key, value) {
            platesListData += "<tr>";
            platesListData += '<td>'+value.plate+'</td>';
            platesListData += '<td>'+value.timestamp+'</td>';
            platesListData += '</tr>';     
        });
        $('#platesList').html(platesListData);
    });
}

function searchPlate() {
    var plate = document.getElementById('plate').value
    var levenshtein = document.getElementById('levenshtein').value
    var platesListData = '';
    $.ajax("/search-plate?key="+plate+"&levenshtein="+levenshtein, {
        type: "GET",
        statusCode: {
           200: function (response) {    
            $.each(response, function(key, value) {
                platesListData += "<tr>";
                platesListData += '<td>'+value.plate+'</td>';
                platesListData += '<td>'+value.timestamp+'</td>';
                platesListData += '</tr>';     
            });
            $("#searchPlateResponse").text('Response code: 200').removeClass().addClass('text-success');
           },
           400: function () {
            $("#searchPlateResponse").text('Response code: 400').removeClass().addClass('text-danger');
           },
           422: function () {
            $("#searchPlateResponse").text('Response code: 422').removeClass().addClass('text-danger');
           }
        },
        complete: function() {
            $('#platesList').html(platesListData);
        }
    }); 
}