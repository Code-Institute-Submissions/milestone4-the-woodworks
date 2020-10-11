function toggleElementView(obj) {
    var el = document.getElementById(obj);
    const style = getComputedStyle(el);
    console.log(style.display);
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

function disableButton(button, loginText) {
    document.getElementById(button).disabled = true;    
    document.getElementById(loginText).style.display = "block";      

}

function enableButton(button, loginText) {
    document.getElementById(button).disabled = false;
    document.getElementById(loginText).style.display = "none";      
}


