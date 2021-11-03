// function to show/hide password on the login/registration forms. Code taken from https://www.w3schools.com/howto/howto_js_toggle_password.asp
function myFunction() {
    let x = document.getElementById("password");
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

//function to add an image-overlay box on the home page on larger devices https://stackoverflow.com/questions/29593944/css-media-query-adding-class-to-html/29594124
let $homeBox = $('.home-box');

$(window).resize(function() {
  if (window.innerWidth >= 768) $homeBox.addClass('card-img-overlay');
  else $homeBox.removeClass('card-img-overlay');
});
