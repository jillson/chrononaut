

function finishTravel()
{
    for (var i=0; i < 4; i++)
    {
	var a = answers[i];
	$("#answer"+(i+1)).unbind("click").text("");
    }

    //TODO: make this an interstitial that will save score before doing relocate
    //TODO: also, make relocate use value from html so we can avoid hardcoding
    window.location.replace("/combat/");
 
}


function setup()
{
    $("#score").text(score);
    $("#distance").text(distance);
    get_card(fcard_callback);
}

function fcard_callback(data)
{
    var ldiv = $("#leftDiv");
    var mdiv = $("#middleDiv");
    var rdiv = $("#rightDiv");
    var answers = [data.wrongAnswer1,
		   data.wrongAnswer3,
		   data.wrongAnswer2,
		   data.correctAnswer];
    shuffle(answers);
    for (var i=0; i < 4; i++)
    {
	var a = answers[i];
	$("#answer"+(i+1)).unbind("click");
	if (a == data.correctAnswer) //in case we have a "wrong" answer be the same
	{
	    $("#answer"+(i+1)).click(correctAnswer);
	}
	else
	{
	    $("#answer"+(i+1)).click(wrongAnswer);
	}
	$("#answer"+(i+1)+"> p").text(a);
    }
    $("#mainCard>p").text(data.question);
}

function correctAnswer(event)
{
    event.stopPropagation();
    $("#message").text("Correct!");
    score += 50;
    distance -= 50;
    if (distance <= 0)
    {
	distance = 0;
	finishTravel();
    }

    $("#myship").animate({
	left: "+=50",
    }, 200, function() {
	setup();
    });
}

function wrongAnswer(event)
{
    event.stopPropagation();
    $("#message").text("Incorrect");
    score -= 25;
    setup();
    return false;
}



$(setup);
