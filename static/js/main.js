function toggleElementView(obj) {
    var el = document.getElementById(obj);
    const style = getComputedStyle(el);
    if (style.display === "none") {
        el.style.display = "block";
    } else if (style.display === "block") {
        el.style.display = "none";
    }
}

function setProgressBar(productVotes, totalVotes, productID) {
    progressPercentage = Math.round(productVotes/totalVotes * 100);
    document.getElementById(productID).style.width = progressPercentage+"%";
}
