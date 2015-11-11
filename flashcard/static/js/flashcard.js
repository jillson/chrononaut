
//TODO: is this overkill for a 4 element array?
function shuffle(array) {
    var counter = array.length, temp, index;

    // While there are elements in the array
    while (counter > 0) {
        // Pick a random index
        index = Math.floor(Math.random() * counter);

        // Decrease counter by 1
        counter--;

        // And swap the last element with it
        temp = array[counter];
        array[counter] = array[index];
        array[index] = temp;
    }

    return array;
}
//TODO: add stuff to the function
function get_card(cb) {

    $.getJSON( flashcardURL, {
        filter: "any",
	format: "json"
    }).done(cb);
	
}
