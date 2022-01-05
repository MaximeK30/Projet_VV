$(window).load(function () {
    $(".trigger_popup_fricc").click(function(){
        document.getElementById('hover_div').style.display = "block";
    });
    $('.hover_bkgr_fricc').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $("#hero_tooltip").click(function() {
        document.getElementById("para").textContent = "The Heroin pleiad (heroinPl) includes crack, cocaine, methadone, and heroin."
    });
    $("#ecsta_tooltip").click(function() {
        document.getElementById("para").textContent = "The Ecstasy pleiad (ecstasyPl) includes amphetamines, cannabis, cocaine, ketamine, LSD, magic mushrooms, legal highs, and ecstasy."
    });
    $("#benzo_tooltip").click(function() {
        document.getElementById("para").textContent = "The Benzodiazepines pleiad (benzoPl) includes contains methadone, amphetamines, and cocaine."
    });    
});