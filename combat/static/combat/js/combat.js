
var sideTurn=0;
var unitTurn=0;


function finishCombat()
{
    for (var i=0; i < 4; i++)
    {
	var a = answers[i];
	$("#answer"+(i+1)).unbind("click").text("");
    }
    $("#mainContainer").hide();
    $("#finishForm").show();
 
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
    var cTeam;
    if (sideTurn == 0) cTeam = goodguys;
    else cTeam = badguys;
    var cGuy = cTeam[unitTurn];
    $('#'+cGuy.id).pulse({opacity: 0.75}, {duration : 150, pulses : -1});

    
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

    var who = goodguys[unitTurn];
    if (who.class == "fighter")
    {
	var timeout = 10;
	var tgt = badguys[Math.floor(Math.random() * badguys.length)];
	while (tgt.hp <= 0 && timeout > 0) {
	    tgt = badguys[Math.floor(Math.random() * badguys.length)];
	    timeout -= 1;
	}
	if (timeout <= 0 && tgt.hp <= 0)
	{
	    console.log("Huh?");
	    finishTurn();
	}
	
	var whoImg = $("#"+who.id);
	var tgtImg = $("#"+tgt.id);
	var deltaX = tgtImg[0].offsetLeft - whoImg[0].offsetLeft;
	var deltaY = tgtImg[0].offsetRight - whoImg[0].offsetRight;
	tgt.hp -= who.dmg;
	if (tgt.hp < 0) tgt.hp = 0;
	whoImg.animate({left: "+=" + (deltaX),top: "+=" + (deltaY)},200).
	    delay(15).addClass("flipped").animate({left: 0, top: 0}).removeClass("flipped").delay(1,finishTurn);
    }
    else if (who.class == "healer")
    {
	for (var i = 0; i < goodguys.length; i++)
	{
	    var guy = goodguys[i];
	    if (guy.hp > 0) {
		guy.hp += who.dmg;
		if (guy.hp > guy.maxhp) guy.hp = guy.maxhp;
	    }
	}
	var whoImg = $("#"+who.id);
	var deltaX = 30;
	whoImg.animate({"left": 50},20).addClass("flipped").delay(250).animate({"left":0}).removeClass("flipped").delay(5,finishTurn);
    }
    else if (who.class == "wizard")
    {
	for (var i = 0; i < badguys.length; i++)
	{
	    var guy = badguys[i];
	    if (guy.hp > 0) {
		guy.hp -= who.dmg;
		if (guy.hp < 0) guy.hp = 0;
	    }
	}
		var whoImg = $("#"+who.id);
	var deltaX = 30;
	whoImg.animate({"left": 50},20).delay(250).animate({"left":0}).delay(5,finishTurn);
    }
    else
    {
	console.log("Don't have actions for class" + who.class);
	finishTurn();
    }
    

}

function finishTurn()
{
    if (checkWin())
    {
	finishCombat();
	return;
    }
    nextUnit();
    setup();
    return;
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

    var who = badguys[unitTurn];
    if (who.class == "thug" || who.class == "thugleader")
    {
	var tgt = goodguys[Math.floor(Math.random() * goodguys.length)];
	while (tgt.hp <= 0) {
	    var tgt = goodguys[Math.floor(Math.random() * goodguys.length)];
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
    for (var i = 0; i < goodguys.length; i++)
    {
	var guy = goodguys[i];
	if (guy.hp > 0) return false;
    }
    return true;
}

function checkWin()
{
    for (var i = 0; i < badguys.length; i++)
    {
	var guy = badguys[i];
	if (guy.hp > 0) return false;
    }
    return true;
}

function nextUnit()
{
    var cTeam;
    if (sideTurn == 0) { cTeam = goodguys; }
    else { cTeam = badguys; }
    var cGuy = cTeam[unitTurn];
    $("#"+cGuy.id).pulse('destroy');
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
	cTeam = badguys;
	sideTurn = 1;
    }
    else
    {
	cTeam = goodguys;
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

$("#finishForm").hide();
$(setup);
