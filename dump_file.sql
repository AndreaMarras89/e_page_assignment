--
-- PostgreSQL database dump
--

-- Dumped from database version 13.12 (Debian 13.12-1.pgdg120+1)
-- Dumped by pg_dump version 15.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: user
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO "user";

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Product; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public."Product" (
    "ID" uuid NOT NULL,
    "Name" character varying NOT NULL,
    "Price" double precision NOT NULL,
    "Description" text NOT NULL
);


ALTER TABLE public."Product" OWNER TO "user";

--
-- Name: User; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public."User" (
    "UID" uuid NOT NULL,
    "Username" character varying NOT NULL,
    "Pass" character varying NOT NULL
);


ALTER TABLE public."User" OWNER TO "user";

--
-- Name: User_Cart; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public."User_Cart" (
    "PID" uuid NOT NULL,
    "UID" uuid NOT NULL,
    "Quantity" integer
);


ALTER TABLE public."User_Cart" OWNER TO "user";

--
-- Name: prova; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.prova (
    "ID" uuid
);


ALTER TABLE public.prova OWNER TO "user";

--
-- Data for Name: Product; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public."Product" ("ID", "Name", "Price", "Description") FROM stdin;
9e94e4ac-4a33-4945-b4aa-cd10f84e6351	Scarf	23	Woolen scarf
ecae2085-3f9c-42bb-890c-92674803e4e0	T-Shirt	43	T-shirt with a cupcake
de5cf73e-eba2-478c-9a72-5b728ded2824	Jeans	29.99	Denim-Jeans
6f553f8f-a6c1-480b-8202-d8dda919b007	Shoes	25	Nike shoes
\.


--
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public."User" ("UID", "Username", "Pass") FROM stdin;
ad5ce927-4a17-4b74-9693-53a2b74f177c	Zer0	1234567890
28451cc3-4a86-426b-a83c-ccfc3dd7ee12	TheWanderer	rishfhe@
\.


--
-- Data for Name: User_Cart; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public."User_Cart" ("PID", "UID", "Quantity") FROM stdin;
9e94e4ac-4a33-4945-b4aa-cd10f84e6351	ad5ce927-4a17-4b74-9693-53a2b74f177c	1
de5cf73e-eba2-478c-9a72-5b728ded2824	28451cc3-4a86-426b-a83c-ccfc3dd7ee12	2
\.


--
-- Data for Name: prova; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.prova ("ID") FROM stdin;
\.


--
-- Name: Product Product_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_pkey" PRIMARY KEY ("ID");


--
-- Name: User_Cart User_Cart_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."User_Cart"
    ADD CONSTRAINT "User_Cart_pkey" PRIMARY KEY ("PID", "UID");


--
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY ("UID");


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: user
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

