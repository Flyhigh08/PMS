setTimeout(function(){
    if ($('#msg').length > 0){
        $('#msg').remove();
    }
}, 8000)

function validate() {
      "use strict";

    
    var first_name = document.reg_form.first_name.value,
    Surname = document.reg_form.Surname.value,
    ID_NO = document.reg_form.ID_NO.value,
    Phone_No = document.reg_form.Phone_No.value,
    DOB = document.reg_form.DOB.value,
    Pswd = document.reg_form.Pswd.value,
    Confirm_Pswd = document.reg_form.Confirm_Pswd.value,
    
    status = false;
  
    if (first_name.length < 1) {
        
        document.getElementById("F_name").innerHTML =  " Please enter your name!";
        status = false;
    } else if (first_name.length <= 1) {
        document.getElementById("F_name").innerHTML="The name is too short!";
        status = false;
                }
    
    else{  
                document.getElementById("F_name").innerHTML="";
                status=true;  
                } 
    
    if(Surname.length < 1){
                    document.getElementById("L_name").innerHTML=  "Please enter your Last name!";  
                    status=false;  
                        }
    
                else if(Surname.length<= 1){
                        document.getElementById("L_name").innerHTML="The name is too short!";
                        status=false;
                        }
    
        else{  
                    document.getElementById("L_name").innerHTML="";
                    status=true;  
                } 
    
    
    if(Pswd.length< 8){
            document.getElementById("Pswd1").innerHTML="Password must be at least 8 characters long!";
            
            status=false;
            }
    
            else if(Pswd!==Confirm_Pswd){  
                document.getElementById("Confir_Pswd").innerHTML="password must be same!";   
                status=false;  
                }
  
        
    
    
return status;  
}

var btt=document.getElementById("back2top"),
    body=document.body,
    docElen=document.documentElement,
    offset=90,
    scrollpos, docHeight,
    isFirefox= navigator.userAgent.toLowerCase().indexOf("firefox") > -1;

//calculate document height
docHeight= Math.max(body.scrollHeight,body.offsetHeight,docElen.clientHeight,docElen.scrollHeight,docElen.offsetHeight);
if (docHeight !='undefined'){
   offset = docHeight / 1.9;
}

// add scroll event listener
window.addEventListener("scroll", function(event ){
    scrollpos = body.scrollTop || docElen.scrollTop;
    
    btt.className = (scrollpos > offset) ? "visible" :"";
});




$('.login a').click(function () {
            $('.login-form ').animate({height:"toggle",opacity:"toggle"},"slow");
            });
                
                $('.register a').click(function(){
                    $('.register-form').animate({height:"fadein",duration:10000,easing:"300s",opacity:"toggle"},"slow"),
                        $('.login-form').hide("");
                 
                            $('.message a').click(function(){
                                $('.register-form').hide(),
                                $('.login-form ').animate({height:"toggle",opacity:"toggle"},"slow");   
                                    }) ;    
                 
                                  });
            





(function ($) {
	/*------------------
		Background Set
	--------------------*/
	$('.Home_bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});


	/*------------------
		Prison_Slider
	--------------------*/
    $(".Home_Slider").owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        items: 1,
        dots: true,
        animateOut: 'fadeOut',
    	animateIn: 'fadeIn',
		navText: ['', ''],
        smartSpeed: 1200,
		autoplay: false,
		mouseDrag: false,
		autoplay: true,
		startPosition: 'URLHash'
    });
	
})(jQuery);


/*$(document).hover(function(){
    
    $('.section-title').fadeIn('900000');
});*/


 

