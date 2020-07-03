var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', { style: style });
card.mount('#card-element');

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#payment-submit').attr('disabled', true);
    $('.preloader').fadeIn('fast')

    var saveInfo = Boolean($('#id-save-info').prop('checked'));
    var billingSame = Boolean($('#billing-same').prop('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
        'billing-is-delivery': billingSame
    };

    if (billingSame == true) {
        form.billing_full_name.value = form.shipping_full_name.value
        form.billing_phone_number_0.value = form.shipping_phone_number_0.value
        form.billing_phone_number_1.value = form.shipping_phone_number_1.value
        form.billing_street_address_1.value = form.shipping_street_address_1.value
        form.billing_street_address_2.value = form.shipping_street_address_2.value
        form.billing_town_or_city.value = form.shipping_town_or_city.value
        form.billing_country.value = form.shipping_country.value
        form.billing_county.value = form.shipping_county.value
    }

    var url = '/checkout/cache_data/';

    $.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.billing_full_name.value),
                phone: $.trim(form.billing_phone_number_0.value + form.billing_phone_number_1.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.billing_street_address_1.value),
                    line2: $.trim(form.billing_street_address_2.value),
                    city: $.trim(form.billing_town_or_city.value),
                    country: $.trim(form.billing_country.value),
                    state: $.trim(form.billing_county.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.shipping_full_name.value),
            phone: $.trim(form.shipping_phone_number_0.value + form.shipping_phone_number_1.value),
            address: {
                line1: $.trim(form.shipping_street_address_1.value),
                line2: $.trim(form.shipping_street_address_2.value),
                city: $.trim(form.shipping_town_or_city.value),
                country: $.trim(form.shipping_country.value),
                postal_code: $.trim(form.shipping_postcode.value),
                state: $.trim(form.shipping_county.value),
            }
        },
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false });
            $('#payment-submit').attr('disabled', false);
            $('.preloader').fadeOut('fast')
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});