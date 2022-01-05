$("select").on("click" , function() {
    $(this).parent(".select-box").toggleClass("open");
});

$(document).mouseup(function (e)
{
    var container = $(".select-box");
    
    if (container.has(e.target).length === 0)
    {
        container.removeClass("open");
    }
});


$("select").on("change" , function() {
    var selection = $(this).find("option:selected").text(),
    labelFor = $(this).attr("id"),
    label = $("[for='" + labelFor + "']");
    label.find(".label-desc").html(selection);
});

$(window).load(function () {
    $("#Neuroticism").click(function() {
        document.getElementById("para").textContent = "Highly neurotic individuals tend to be labile (that is, subject to frequently changing emotions), anxious, tense, and withdrawn. Individuals who are low in neuroticism tend to be content, confident, and stable."
    });
    $("#Extraversion").click(function() {
        document.getElementById("para").textContent = "Extraversion indicates how outgoing and social a person is. A person who scores high in extraversion on a personality test is the life of the party. They enjoy being with people, participating in social gatherings, and are full of energy. A person low in extraversion is less outgoing and is more comfortable working by himself."
    });
    $("#Openness").click(function() {
        document.getElementById("para").textContent = "A person with a high level of openness to experience in a personality test enjoys trying new things. They are imaginative, curious, and open-minded. Individuals who are low in openness to experience would rather not try new things. They are close-minded, literal and enjoy having a routine."
    });
    $("#Agreeableness").click(function() {
        document.getElementById("para").textContent = "A person with a high level of agreeableness in a personality test is usually warm, friendly, and tactful. They generally have an optimistic view of human nature and get along well with others. A person who scores low on agreeableness may put their own interests above those of others. They tend to be distant, unfriendly, and uncooperative."
    });
    $("#Conscientiousness").click(function() {
        document.getElementById("para").textContent = "A person scoring high in conscientiousness usually has a high level of self-discipline. These individuals prefer to follow a plan, rather than act spontaneously. Their methodic planning and perseverance usually makes them highly successful in their chosen occupation."
    });
    $("#Impulsiveness").click(function() {
        document.getElementById("para").textContent = "Impulsivity is the tendency to act without thinking, for example if you blurt something out, buy something you had not planned to, or run across the street without looking."
    });
    $("#Sensation_seeking").click(function() {
        document.getElementById("para").textContent = "Sensation seeking is a trait defined by the seeking of varied, novel, complex, and intense sensations and experiences, and the willingness to take physical, social, legal, and financial risks for the sake of such experience."
    });
    $(".trigger_popup_fricc").click(function(){
        document.getElementById('hover_div').style.display = "block";
    });
    $('.hover_bkgr_fricc').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.hover_bkgr_fricc').hide();
    });

    var element = document.querySelector('#select-box-Age');
    
    var lastWidth = element.offsetWidth;
    var lastHeight = element.offsetHeight;

    var action = function() {
        var currentWidth = element.offsetWidth;
        var currentHeight = element.offsetHeight;

        if (lastWidth !== currentWidth || lastHeight !== currentHeight) {
            console.log(currentWidth);
            var all = document.getElementsByTagName("a");
            for(var i = 0, max = all.length; i < max; i++)
                all[i].style = "margin-left: " + String(currentWidth + 20) + "px;";
            
            lastWidth = currentWidth;
            lastHeight = currentHeight;
        }
    };

    setInterval(action, 10); // checking for changes every 10 ms

});
