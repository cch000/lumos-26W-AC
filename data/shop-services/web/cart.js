// Zenith storefront cart helper (BF22 relaunch, Alex T.)
// Loaded by the Shopify theme: <script src="https://api.zenithactive.com/static/cart.js">
// Totals are estimated here so the drawer feels instant; the real price comes from /cart/quote at checkout.

const API_BASE = "https://api.zenithactive.com";
const FREE_SHIPPING_MIN = 75;

// keep in sync with config/promos.yaml
const PROMOS = { WELCOME10: 0.10, NEWS5: 0.05, LOYAL15: 0.15, ZENITH30: 0.30 };

function getCart() {
  try {
    return JSON.parse(localStorage.getItem("zenith_cart")) || [];
  } catch (e) {
    return [];
  }
}

function saveCart(cart) {
  localStorage.setItem("zenith_cart", JSON.stringify(cart));
  const badge = document.querySelector(".cart-count");
  if (badge) badge.textContent = cart.reduce((n, i) => n + i.quantity, 0);
}

function money(x) {
  return "$" + x.toFixed(2);
}

function estimateTotals(cart, promoCode, creatorCode) {
  const subtotal = cart.reduce((s, i) => s + i.price * i.quantity, 0);
  // one code per order (Shopify rule); creator code only used if there is no promo
  const code = (promoCode || "").toUpperCase();
  const pct = PROMOS[code] || (creatorCode ? 0.30 : 0);
  const discount = Math.round(subtotal * pct * 100) / 100;
  const afterDiscount = subtotal - discount;
  return { subtotal, discount, afterDiscount, freeShipping: afterDiscount >= FREE_SHIPPING_MIN };
}

function showAddedModal(product) {
  const cart = getCart();
  const t = estimateTotals(cart, localStorage.getItem("zenith_promo"), localStorage.getItem("zenith_creator"));
  const modal = document.getElementById("added-modal");
  modal.querySelector(".modal-title").textContent = "✔ Added to cart — proceed to checkout";
  modal.querySelector(".item-name").textContent = product.name;
  modal.querySelector(".item-variant").textContent = product.variant || "";
  modal.querySelector(".item-price").textContent = money(product.price);
  modal.querySelector(".order-total").textContent = money(t.afterDiscount);
  modal.classList.add("open");
}

function closeModal() {
  document.getElementById("added-modal").classList.remove("open");
}

function addToCart(product, quantity = 1) {
  const cart = getCart();
  const line = cart.find((i) => i.id === product.id);
  if (line) line.quantity += quantity;
  else cart.push({ id: product.id, name: product.name, price: product.price, quantity });
  saveCart(cart);
  showAddedModal(product);

  // TEMP for BF22 test - send people straight to checkout. revert after Cyber Monday
  setTimeout(() => {
    window.location.href = "/checkout";
  }, 1500);
}

async function fetchQuote(zip) {
  const cart = getCart();
  const res = await fetch(API_BASE + "/cart/quote", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      items: cart.map((i) => ({ product_id: i.id, quantity: i.quantity })),
      zip: zip,
      promo_code: localStorage.getItem("zenith_promo"),
      creator_code: localStorage.getItem("zenith_creator"),
    }),
  });
  if (!res.ok) throw new Error("quote failed: " + res.status);
  return res.json();
}

function applyCodes() {
  const promo = document.getElementById("promo-code").value.trim();
  const creator = document.getElementById("creator-code").value.trim();
  if (promo) localStorage.setItem("zenith_promo", promo.toUpperCase());
  if (creator) localStorage.setItem("zenith_creator", creator.toUpperCase());
  const t = estimateTotals(getCart(), promo, creator);
  document.getElementById("cart-estimate").textContent =
    `Subtotal ${money(t.subtotal)} − ${money(t.discount)} = ${money(t.afterDiscount)}` +
    (t.freeShipping ? " · free shipping" : "");
}

document.addEventListener("DOMContentLoaded", () => {
  saveCart(getCart());
  document.querySelectorAll("[data-add-to-cart]").forEach((btn) =>
    btn.addEventListener("click", () => addToCart(JSON.parse(btn.dataset.product)))
  );
  const cont = document.getElementById("continue-shopping");
  if (cont) cont.addEventListener("click", closeModal);
  const apply = document.getElementById("apply-codes");
  if (apply) apply.addEventListener("click", applyCodes);
});
