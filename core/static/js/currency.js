document.addEventListener("DOMContentLoaded", () => {
  console.log("JS CARGADO");
  console.log("currency cargado");

  const rates = {
    CLP: 1,
    USD: 0.0011,
    EUR: 0.0010,
    MXN: 0.018,
    CRC: 0.56,
    BRL: 0.0054,
    DOP: 0.064,
    CAD: 0.0015,
    ARS: 0.95,
    AUD: 0.0017
  };

  const symbols = {
    CLP: "$",
    USD: "US$",
    EUR: "€",
    MXN: "MX$",
    CRC: "₡",
    BRL: "R$",
    DOP: "RD$",
    CAD: "C$",
    ARS: "AR$",
    AUD: "A$"
  };

  const toggle = document.getElementById("priceToggle");
  const priceFilter = document.getElementById("priceFilter");
  const range = document.getElementById("priceRange");
  const priceValue = document.getElementById("priceValue");
  const currency = document.getElementById("currency");
  const cards = document.querySelectorAll(".video-card");

  /* TOGGLE */
  if (toggle && priceFilter) {
    toggle.addEventListener("click", () => {
      const hidden = priceFilter.style.display === "none";
      priceFilter.style.display = hidden ? "block" : "none";
      toggle.textContent = hidden ? "−" : "+";
    });
  }

  /* FILTRO PRECIO */
  if (range && priceValue) {
    range.addEventListener("input", () => {
      const maxPrice = parseInt(range.value, 10);
      priceValue.textContent = "$ " + maxPrice.toLocaleString();

      cards.forEach(card => {
        const price = parseInt(card.dataset.price, 10);
        card.style.display = price <= maxPrice ? "block" : "none";
      });
    });
  }

  /* CAMBIO MONEDA */
  if (currency) {
    currency.addEventListener("change", () => {
      const selected = currency.value;
      const rate = rates[selected] || 1;
      const symbol = symbols[selected] || "$";

        if (cards.length > 0) {
                cards.forEach(card => {
                const basePrice = parseInt(card.dataset.price, 10);
                const converted = Math.round(basePrice * rate);
                card.querySelector(".price-value").textContent =
                converted.toLocaleString();
            });
        }

        const priceElements = document.querySelectorAll(".price-value");

        if (priceElements.length > 0 && cards.length === 0) {
            priceElements.forEach(el => {
                const basePrice = parseInt(el.dataset.price, 10);
                const converted = Math.round(basePrice * rate);
                el.textContent = converted.toLocaleString();
            });
        }


      document.querySelectorAll(".currency-symbol").forEach(el => {
        el.textContent = symbol;
      });

      if (priceValue && range) {
        const convertedMax = Math.round(range.value * rate);
        priceValue.textContent =
          symbol + " " + convertedMax.toLocaleString();
      }
    });
  }

});
