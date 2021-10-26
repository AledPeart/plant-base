// function to show/hide password on the login/registration forms. Code taken from https://www.w3schools.com/howto/howto_js_toggle_password.asp
function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

// function to fade out flashed messages - not working https://stackoverflow.com/questions/51822192/trying-javascript-to-have-my-flash-my-message-disappear-after-a-few-seconds-afte
  setTimeout(function() {
    $('#flash-messages').fadeOut('fast');
}, 30000); 