// function to show/hide password on the login/registration forms. Code taken from https://www.w3schools.com/howto/howto_js_toggle_password.asp
function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

// function to fade out flashed messages - https://stackoverflow.com/questions/23101966/bootstrap-alert-auto-close

$("#flash-messages").fadeTo(3000, 500).slideUp(500, function(){
  $("#flash-messages").slideUp(500);
});