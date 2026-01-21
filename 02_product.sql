--
-- Data for Name: cartjiapp_product; Type: TABLE DATA; Schema: public; Owner: neondb_owner
--

INSERT INTO public.cartjiapp_product (id, name, slug, original_price, discount_price, description, views, is_active, created_at, category_id, subcategory_id) VALUES (1, 'Tom & Jerry Printed Hoodie', 'tom-jerry-printed-hoodie', 1799.00, 699.00, 'Trendy oversized hoodie featuring a playful Tom & Jerry back graphic. Designed for warmth, comfort, and street-style appeal.



FEATURES:

- Premium heavy GSM fabric

- 3-thread 480 GSM fleece

- Bold and vibrant digital prints

- Comfortable oversized fit



SIZES AVAILABLE:

XXS, XS, S, M, L, XL, XXL, 3XL, 4XL, 5XL



NOTE:

3XL???5XL sizes cost ???80 extra.



SHIPPING:

Free shipping



Stay warm, stylish, and comfortable this winter.', 2, true, '2026-01-03 12:26:36.08168+00', 5, 1);
--
-- Name: cartjiapp_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neondb_owner
--

SELECT pg_catalog.setval('public.cartjiapp_product_id_seq', 1, true);

