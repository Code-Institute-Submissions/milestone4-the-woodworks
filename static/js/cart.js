function disableButton() {
    document.getElementById('checkout-anchor').disabled = true;    
    document.getElementById('cart-login-request').style.display = "block";      
}

try { document.getElementById('checkout-anchor').addEventListener("click", disableButton); }
catch(err) {}

