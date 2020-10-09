function hide(obj) {
    var el = document.getElementById(obj);
    const style = getComputedStyle(el)
    if (style.display === "none") {
        el.style.display = "block";
    } else if (style.display === "block") {
        el.style.display = "none";
    }
}