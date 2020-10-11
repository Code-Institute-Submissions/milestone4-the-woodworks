<!--
<div class="row">
    <div class="col-10 offset-1 col-md-8 offset-md-2 border border-dark mt-2 mt-md-4">
        <div class="row">
            <div class="mt-3 col-12 font-weight-bold"> Total: € {{total}} </div>
            <div class="my-2 col-12 font-weight-bold"> Total construction time: {{total_time}} weeks </div>
            <!-- the href in the onclick event had to be hard coded because i couldn't find a way to add another set of
            quotation marks on onclick="location.href={% url 'checkout' %}", the href destiantion needs a set of quotation marks -->
            <button onclick="location.href='../checkout/';" id="submit-button" class="btn btn-primary mx-3 mb-2 mb-sm-3">
                <span class="text-uppercase">Checkout</span>
            </button>
            <div id="cart-login-request" class="login-request-text ml-3 mb-2 mb-sm-0 mt-sm-1"><span>Please login to go to checkout</span></div>
            {% if not user.is_authenticated %}
                <script>
                    disableButton('submit-button', 'cart-login-request');
                    // toggleElementView('cart-login-request');
                </script>
            {% else %}
                <script>
                    enableButton('submit-button', 'cart-login-request');
                    // toggleElementView('cart-login-request');
                </script>
            {% endif %}
        </div>
    </div>
</div>
-->
