
var now = Date.now();
        console.log(Date.parse(now.toLocaleString()));
function updateStatus()
{


    $.getJSON('/status', function( data ) {
        $('#container').empty();
        var items = [];
        $.each(data, function (key, val) {
            var newDiv = $('<div />').attr('class','col-md-4 site text-center');
            newDiv.html("<h1><img width=\"32px\" height=\"32px\" src=\"http://www.google.com/s2/favicons?domain=" + key + "\" /> " + val[0] + "</h1><h2>" + val[1] + " " + val[2] + " " + val[3] + " - " + val[4] + "ms</h2>");
            $('#container').append(newDiv);
            $('#time').html('<h1>Last updated at ' + val[5] + '</h1>');
        });
    });
}

updateStatus();
$(document).ready(setInterval(updateStatus,120000));