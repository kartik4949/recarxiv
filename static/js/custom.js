$(document).ready(function(){
    if($("body").hasClass("dashboard")){
        $(".header").removeClass("header-transparent");
    }
    if($("body").hasClass("static")){
        $(".header").removeClass("header-transparent");
    }
    $(".product_menu").click(function(){
        $(".sub-menu-mobile").slideToggle();
    })
    $(".report_menu").click(function(){
        $(".sub-menu-mobile-report").slideToggle();
    })
    $(".sample_report_menu").click(function(){
        $(".sub-menu-mobile-sample_report").slideToggle();
    })
    $(".property_menu").click(function(){
        $(".sub-menu-mobile-property").slideToggle();
    })
     $(".custom_menu").click(function(){
        $(".sub-menu-mobile-custom").slideToggle();
    })
     $(".ap10plus_menu").click(function(){
            $(".sub-menu-mobile-ap10plus").slideToggle();
    })
    $(".product_menu-2").click(function(){
        $(".sub-menu-mobile-2").slideToggle();
    })
    $(".cases_menu").click(function(){
        $(".sub-menu-mobile-cases").slideToggle();
    })
    $(".dropdown_menu").click(function(){
        $(this).siblings(".sub-menu-mobile").slideToggle();
    })
});

function openNav() {
  $("#mySidenav").css("left", "0");
  $("body, html").addClass("pagetransition no-scroll");
  $("html").addClass("no-scroll");
}

function closeNav() {
  $("#mySidenav").css("left", "-250px");
  $("body, html").removeClass("pagetransition no-scroll");
  $("html").removeClass("no-scroll");
}
