--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cfg; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cfg (
    sno integer NOT NULL,
    template_id integer NOT NULL,
    template_name character varying(35),
    saved_name character varying(40),
    created_on date DEFAULT CURRENT_DATE NOT NULL,
    created_by character varying(50),
    cfg_json json NOT NULL
);


ALTER TABLE public.cfg OWNER TO postgres;

--
-- Name: cfg_sno_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cfg_sno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cfg_sno_seq OWNER TO postgres;

--
-- Name: cfg_sno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cfg_sno_seq OWNED BY public.cfg.sno;


--
-- Name: cfg_template; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cfg_template (
    template_id integer NOT NULL,
    template_name character varying(35),
    created_on date DEFAULT CURRENT_DATE NOT NULL,
    created_by character varying(50),
    template json NOT NULL
);


ALTER TABLE public.cfg_template OWNER TO postgres;

--
-- Name: cfg_template_template_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cfg_template_template_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cfg_template_template_id_seq OWNER TO postgres;

--
-- Name: cfg_template_template_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cfg_template_template_id_seq OWNED BY public.cfg_template.template_id;


--
-- Name: cfg sno; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cfg ALTER COLUMN sno SET DEFAULT nextval('public.cfg_sno_seq'::regclass);


--
-- Name: cfg_template template_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cfg_template ALTER COLUMN template_id SET DEFAULT nextval('public.cfg_template_template_id_seq'::regclass);


--
-- Data for Name: cfg; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cfg (sno, template_id, template_name, saved_name, created_on, created_by, cfg_json) FROM stdin;
\.


--
-- Data for Name: cfg_template; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cfg_template (template_id, template_name, created_on, created_by, template) FROM stdin;
\.


--
-- Name: cfg_sno_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cfg_sno_seq', 1, false);


--
-- Name: cfg_template_template_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cfg_template_template_id_seq', 1, false);


--
-- Name: cfg cfg_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cfg
    ADD CONSTRAINT cfg_pkey PRIMARY KEY (sno);


--
-- Name: cfg_template cfg_template_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cfg_template
    ADD CONSTRAINT cfg_template_pkey PRIMARY KEY (template_id);


--
-- PostgreSQL database dump complete
--

