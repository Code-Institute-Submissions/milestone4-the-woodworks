// toggle the display property of the text (description) on the cards
// on the store page.
function toggleElementView(obj) {
    let el = document.getElementById(obj);
    const style = getComputedStyle(el);
    if (style.display === "none") {
        el.style.display = "block";
    } else if (style.display === "block") {
        el.style.display = "none";
    }
}

// Calculates the percentage of votes of the total votes this 
// choice has and sets the progressbar width accordingly
function setProgressBar(productVotes, totalVotes, productID) {
    var progressPercentage = Math.round(productVotes/totalVotes * 100);
    document.getElementById(productID).style.width = progressPercentage+"%";
}
