
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

$(document).ready(function(){
    $("#authform").submit(function(event){
        event.preventDefault();
        $.post("http://localhost:8000/auth/token", $(this).serialize(), function(data,status){
            setCookie('access_token', data["access_token"], 1);
            window.location.href = "index";
        });
    });
});



