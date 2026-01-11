document.addEventListener("DOMContentLoaded", function () {
    const publicKeyEl = document.getElementById("id_stripe_public_key");
    const clientSecretEl = document.getElementById("id_client_secret");

    if (!publicKeyEl || !clientSecretEl) {
        return;
    }

    const stripePublicKey = publicKeyEl.value;
    const clientSecret = clientSecretEl.value;

    const stripe = Stripe(stripePublicKey);
    const elements = stripe.elements();

    const style = {
        base: {
            fontSize: "16px",
        },
    };

    const card = elements.create("card", { style: style });
    card.mount("#card-element");

    const form = document.getElementById("payment-form");
    const submitButton = document.getElementById("submit-button");
    const cardErrors = document.getElementById("card-errors");

    card.addEventListener("change", function (event) {
        if (event.error) {
            cardErrors.textContent = event.error.message;
        } else {
            cardErrors.textContent = "";
        }
    });

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        submitButton.disabled = true;
        cardErrors.textContent = "";

        const fullName = document.getElementById("id_full_name");
        const email = document.getElementById("id_email");

        const result = await stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: fullName ? fullName.value : "",
                    email: email ? email.value : "",
                },
            },
        });

        if (result.error) {
            cardErrors.textContent = result.error.message;
            submitButton.disabled = false;
            return;
        }

        if (result.paymentIntent && result.paymentIntent.status === "succeeded") {
            form.submit();
            return;
        }

        cardErrors.textContent = "Payment was not successful. Please try again.";
        submitButton.disabled = false;
    });
});
