
var sideTurn=0;
var unitTurn=0;


function finishCombat()
{
    for (var i=0; i < 4; i++)
    {
	var a = answers[i];
	$("#answer"+(i+1)).unbind("click").text("");
    }

    //TODO: make this an interstitial that will save score before doing relocate
    //TODO: also, make relocate use value from html so we can avoid hardcoding
    window.location.replace("/");
 
}


function setup()
{
    $("#score").text(score);
    for (var i = 0; i < goodguys.length; i++)
    {
	var guy = goodguys[i];
	$("#"+guy.id+"_hp").text(guy.hp + "/" + guy.maxhp);
    }

    for (var i = 0; i < badguys.length; i++)
    {
	var guy = badguys[i];
	$("#"+guy.id+"_hp").text(guy.hp + "/" + guy.maxhp);
    }
    
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
    
    if (sideTurn == 1)
    {
	nextUnit();
	setup();
	return;
    }

    var who = goodGuys[unitTurn];
    if (who.class == "fighter")
    {
	var tgt = badGuys[Math.floor(Math.random() * badGuys.length)];
	while (tgt.hp <= 0) {
	    	tgt = badGuys[Math.floor(Math.random() * badGuys.length)];
	}
	tgt.hp -= who.dmg;
    }
    else if (who.class == "healer")
    {
	for (var i = 0; i < goodGuys.length; i++)
	{
	    var guy = goodGuys[i];
	    if (guy.hp > 0) {
		guy.hp += who.dmg;
		if (guy.hp > guy.maxhp) guy.hp = guy.maxhp;
	    }
	}
    }
    else if (who.class == "wizard")
    {
	for (var i = 0; i < badGuys.length; i++)
	{
	    var guy = badGuys[i];
	    if (guy.hp > 0) {
		guy.hp -= who.dmg;
		if (guy.hp < 0) guy.hp = 0;
	    }
	}
    }

    if (checkWin())
    {
	finishCombat();
	return;
    }

    nextUnit();
    setup();
    return;
    
    /*$("#myship").animate({
	left: "+=50",
    }, 200, function() {
	setup();
    });
    */
    
}

function wrongAnswer(event)
{
    event.stopPropagation();
    $("#message").text("Incorrect");
    score -= 25;

    if (sideTurn == 0)
    {
	nextUnit();
	setup();
	return;
    }

    var who = badGuys[unitTurn];
    if (who.class == "thug" or who.class == "thugleader")
    {
	var tgt = goodGuys[Math.floor(Math.random() * goodGuys.length)];
	while (tgt.hp <= 0) {
	    var tgt = goodGuys[Math.floor(Math.random() * goodGuys.length)];
	}
	tgt.hp -= who.dmg;
    }

    if (checkLose())
    {
	finishCombat();
	return;
    }

    nextUnit();
    setup();
    return false;
}

function checkLose()
{
    for (var i = 0; i < goodGuys.length; i++)
    {
	var guy = goodGuys[i];
	if (guy.hp > 0) return false;
    }
    return true;
}

function checkWin()
{
    for (var i = 0; i < badGuys.length; i++)
    {
	var guy = badGuys[i];
	if (guy.hp > 0) return false;
    }
    return true;
}

function nextUnit()
{
    var cTeam;
    if (sideTurn == 0) { cTeam = goodGuys; }
    else { cTeam = badGuys; }
    unitTurn += 1;
    for (; unitTurn < cTeam.length; unitTurn++)
    {
	var next = cTeam[unitTurn];
	if (next.hp > 0)
	{
	    return;
	}
    }
    unitTurn = 0;
    if (sideTurn == 0)
    {
	cTeam = badGuys;
	sideTurn = 1;
    }
    else
    {
	cTeam = goodGuys;
	sideTurn = 0;
    }
    for (; unitTurn < cTeam.length; unitTurn++)
    {
	var next = cTeam[unitTurn];
	if (next.hp > 0)
	{
	    return;
	}
    }
    console.log("Warning... something isn't right in Denmark");
}


$(setup);
