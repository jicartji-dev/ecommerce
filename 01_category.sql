
--
-- Data for Name: cartjiapp_category; Type: TABLE DATA; Schema: public; Owner: neondb_owner
--

INSERT INTO public.cartjiapp_category (id, name, slug, image) VALUES (4, 'Accessories', 'accessories', 'image/upload/v1767970962/f51r6nslebvgyr348ypy.png');
INSERT INTO public.cartjiapp_category (id, name, slug, image) VALUES (1, 'Men', 'men', 'image/upload/v1767971388/qebeatcnihjihtyoaiia.png');
INSERT INTO public.cartjiapp_category (id, name, slug, image) VALUES (2, 'Women', 'women', 'image/upload/v1767971410/okswy2syznrgl0qwixid.png');
INSERT INTO public.cartjiapp_category (id, name, slug, image) VALUES (5, 'Seasonal Wear', 'seasonal-wear', 'image/upload/v1767971446/kjxfuoi2pjflgwhsk20h.png');



--
-- Data for Name: cartjiapp_subcategory; Type: TABLE DATA; Schema: public; Owner: neondb_owner
--

INSERT INTO public.cartjiapp_subcategory (id, name, slug, category_id) VALUES (1, 'Winter Wear (Sweaters, Jackets)', 'winter-wear-sweaters-jackets', 5);
INSERT INTO public.cartjiapp_subcategory (id, name, slug, category_id) VALUES (2, 'Shirts', 'shirts', 1);
INSERT INTO public.cartjiapp_subcategory (id, name, slug, category_id) VALUES (3, 'T Shirts', 't-shirts', 1);


--
-- Data for Name: cartjiapp_color; Type: TABLE DATA; Schema: public; Owner: neondb_owner
--

INSERT INTO public.cartjiapp_color (id, name, code) VALUES (1, 'Airforce Blue', '#5D6F82');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (2, 'Brown', '#5A3A2E');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (3, 'Black', '#000000');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (4, 'White', '#FFFFFF');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (5, 'Red', '#B11226');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (6, 'Pista Green', '#93C7A2');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (7, 'Beige', '#D6C5A8');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (8, 'Grey', '#B0B0B0');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (9, 'Olive Green', '#556B2F');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (10, 'Navy Blue', '#0B1D34');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (11, 'Mint Green', '#A7CFC2');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (12, 'Classic Blue', '#7FA4C1');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (13, 'Forest Green', '#2F4F3E');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (14, 'Ivory Cream', '#F2E6D8');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (15, 'Deep Maroon', '#7A1F2B');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (16, 'Camel Brown', '#C2A47A');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (17, 'Mehendi Green', '#3F4F3C');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (18, 'Coffee Brown', '#4A2C1D');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (19, 'Sky Blue', '#B7D9F2');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (20, 'Wine Maroon', '#7B1E2B');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (21, 'Mustard Yellow', '#E1B12C');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (22, 'Royal Blue', '#2F4E8B');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (23, 'Light Green', '#9BCF9B');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (24, 'Charcoal Grey', '#5F666B');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (25, 'Bottle Green', '#0F3D2E');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (26, 'Ice Blue', '#DCE6F1');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (27, 'Cream Beige', '#F5E6CC');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (28, 'Wine Red', '#7A1F2B');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (29, 'Classic Red', '#C1121F');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (30, 'Ash Grey', '#B2B2B2');
INSERT INTO public.cartjiapp_color (id, name, code) VALUES (31, 'Camel', '#C9A26A');




--
-- Data for Name: cartjiapp_size; Type: TABLE DATA; Schema: public; Owner: neondb_owner
--

INSERT INTO public.cartjiapp_size (id, name) VALUES (5, 'XXL');
INSERT INTO public.cartjiapp_size (id, name) VALUES (7, '3XL');
INSERT INTO public.cartjiapp_size (id, name) VALUES (8, '4XL');
INSERT INTO public.cartjiapp_size (id, name) VALUES (9, '5XL');
INSERT INTO public.cartjiapp_size (id, name) VALUES (10, 'L');
INSERT INTO public.cartjiapp_size (id, name) VALUES (6, 'XL');
INSERT INTO public.cartjiapp_size (id, name) VALUES (4, 'M');
INSERT INTO public.cartjiapp_size (id, name) VALUES (1, 'S');
INSERT INTO public.cartjiapp_size (id, name) VALUES (2, 'XS');

--
-- Name: cartjiapp_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neondb_owner
--

SELECT pg_catalog.setval('public.cartjiapp_category_id_seq', 5, true);


--
-- Name: cartjiapp_subcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neondb_owner
--

SELECT pg_catalog.setval('public.cartjiapp_subcategory_id_seq', 3, true);



--
-- Name: cartjiapp_color_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neondb_owner
--

SELECT pg_catalog.setval('public.cartjiapp_color_id_seq', 31, true);

--
-- Name: cartjiapp_color_id_seq; Type: SEQUENCE SET; Schema: public; Owner: neondb_owner
--

SELECT pg_catalog.setval('public.cartjiapp_color_id_seq', 31, true);

