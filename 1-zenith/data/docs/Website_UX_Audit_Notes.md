# zenithactive.com: UX audit notes

**Author:** Nadia Kowalski, freelance UX research
**For:** Megan Thompson (CMO), Jamie Sinclair (Creative Director); cc Brendan Ohs
**Date:** 18 September 2023
**Scope:** home, category pages, product pages, add-to-cart, checkout, post-purchase. Desktop (Chrome, Safari) and mobile (iPhone 13, Pixel 6).
**Method:** expert walkthrough on Fri 1 – Sun 3 Sep (flash weekend) and Tue 12 Sep; one real test order placed 1 Sep, refunded afterwards. No users tested this round: observations, not measurements.

---

## Priority 1: fix before the holiday season

**1. The add-to-cart modal sends people to checkout on its own.**
Adding any item opens a pink modal headed "✓ ADDED TO CART — PROCEED TO CHECKOUT" with the item, an Order Total, a large "CHECKOUT NOW" button and a small outlined "← Continue Shopping" link underneath. If you do nothing, the page moves to checkout after about a second and a half. On desktop I could sometimes hit Continue Shopping if my cursor was already near it. On mobile I never managed it: by the time my thumb is there, checkout is loading. The only way back from checkout is the browser back button.
The design assumes every visitor arrives for one thing. Anyone building an outfit gets interrupted after the first item.
*Recommendation:* remove the auto-advance. Keep the confirmation, make "Continue shopping" and "Checkout" equal-weight buttons, or use a slide-out mini-cart that stays until dismissed.

**2. The homepage is a discount page.**
Above the fold there is no product, photography or brand story. There's a pink strip ("FLASH SALE: 30% OFF SITEWIDE — USE CODE ZENITH30 AT CHECKOUT — ENDS MIDNIGHT!"), a hero that is just "30% OFF / Everything. No Exclusions.", a "SHOP THE SALE" button and an "Offer Ends In" countdown. The first section below is "TRENDING NOW — 30% OFF EVERYTHING", where every tile carries a red "30% OFF" badge.
Two specific problems. First, the countdown reset at midnight on Friday and again on Saturday: "ends midnight" three nights in a row. A returning visitor learns the deadline isn't real. Second, the tiles already show the reduced price (Velocity Training Shorts $55.00 struck through, $38.50), while the strip says to enter the code at checkout. It's unclear whether the code is already included or comes on top.
*Recommendation:* lead with product and brand (the Terra line photographs well). Keep promotions in one bounded slot. One deadline per sale, not one per day.

**3. The "stack it" creator banner.**
Below the product grid sits a full-width block: a big "FITFAM30" tag next to "GOT A CREATOR CODE? STACK IT WITH OUR SITEWIDE SALE! Our Creator Affiliate partners are sharing exclusive bundles and extra discounts… New codes drop every week." The trust strip under the hero adds "USE CODE FITFAM30 FOR INFLUENCER EXCLUSIVE DEALS". It's also visible behind the add-to-cart modal, at the exact moment someone decides to buy.
On my test order I entered ZENITH30 in the promo field and FITFAM30 in the separate creator-code field. Checkout accepted both and showed them as two discount lines. So the banner does what it says.
*Recommendation:* confirm with marketing and legal that combining is the intended offer for every creator and every sale. A public promise like this is hard to walk back.

## Priority 2

**4. No way to check an order without e-mail.**
There's no "Track my order" link in the header, footer or account area. The account page lists past orders, but without status or tracking. To know where a parcel is, a customer depends entirely on our e-mails or on support.
On my test order, the order confirmation arrived within a minute. I didn't see a shipping notification before the parcel turned up on 7 Sep (I checked spam and promotions). Could be a one-off on my side; worth someone confirming which post-purchase e-mails are supposed to go out.
*Recommendation:* add an order-status page (order number + e-mail or ZIP), and link to it from every e-mail and from the footer.

**5. Almost no cross-sell.**
The cart modal shows the item and the total, nothing else. No "goes well with", no bundles, and no free-shipping nudge even though "FREE SHIPPING ON ORDERS $75+" is in the trust strip. Example: an Alpine Zip Hoodie lands in the modal at $59.50, short of the free-shipping line, and nobody tells the customer. Product pages have no "complete the look" either, though obvious pairs exist (Velocity Socks 3-Pack with anything).
*Recommendation:* a line like "You're $15.50 away from free shipping" in the cart, and two or three paired products on product pages and in the mini-cart once it stops redirecting.

**6. Two return policies.**
The trust strip says "60-DAY RETURNS ON CREATOR PROMO ORDERS"; the FAQ says 30 days.

## Priority 3 (quick polish)

- Grey text on the pink hero fails contrast on mobile.
- Search has no typo tolerance ("hoody" returns nothing).
- Eco Collection pages have one-line descriptions.

## Suggested next step

Moderated user tests (3–5 people) on the add-to-cart flow with a two-item task, to see how real shoppers handle finding 1. I can run them remotely.

— Nadia
