function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var cdata = ca[i].split('=');
        
    }
    return cdata[1];
}

$(document).ready(function(){ 
    $("form").submit(function(event){
        event.preventDefault();
        var accessToken = getCookie('access_token');
        var tokenBearer = 'Bearer ' + accessToken;
        var metreKare = parseInt(document.getElementsByName("metreKare")[0].value);
        var odaSayisi = parseInt(document.getElementsByName("odaSayisi")[0].value);
        $.ajax(
        {
        type: "GET",
        beforeSend: function(xhr) {
            xhr.setRequestHeader('Authorization', tokenBearer);
        },
        url: "http://localhost:8000/tahmin/"+metreKare + "/" +odaSayisi+"/",
        cache: true,
        data: $(this).serialize(),
        dataType: 'json',
        success: function(data) { 
            alert("Evin fiyatı: " + data);
            console.log("Evin fiyatı: " + data);
        },
        error: function (xhr, ajaxOptions, thrownError) 
        {
            alert(thrownError);
        }
      });
    });

});