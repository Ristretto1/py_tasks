PGDMP                      |            postgres    16.4 (Postgres.app)    16.4 (Postgres.app)      >           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            @           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            A           1262    5    postgres    DATABASE     t   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';
    DROP DATABASE postgres;
                postgres    false            B           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3649                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            C           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    16428    comments    TABLE     �   CREATE TABLE public.comments (
    id integer NOT NULL,
    text character varying NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);
    DROP TABLE public.comments;
       public         heap    postgres    false    4            �            1259    16427    comments_id_seq    SEQUENCE     �   ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    222    4            �            1259    16412    likes    TABLE     s   CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);
    DROP TABLE public.likes;
       public         heap    postgres    false    4            �            1259    16411    likes_id_seq    SEQUENCE     �   ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    220    4            �            1259    16399    posts    TABLE     �   CREATE TABLE public.posts (
    title character varying NOT NULL,
    description character varying NOT NULL,
    user_id integer NOT NULL,
    id integer NOT NULL
);
    DROP TABLE public.posts;
       public         heap    postgres    false    4            �            1259    16398    posts_id_seq    SEQUENCE     �   ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    4    218            �            1259    16391    users    TABLE     �   CREATE TABLE public.users (
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying NOT NULL,
    nationality character varying NOT NULL,
    id integer NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false    4            �            1259    16390    users_id_seq    SEQUENCE     �   ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    4    216            ;          0    16428    comments 
   TABLE DATA           >   COPY public.comments (id, text, user_id, post_id) FROM stdin;
    public          postgres    false    222   �!       9          0    16412    likes 
   TABLE DATA           5   COPY public.likes (id, user_id, post_id) FROM stdin;
    public          postgres    false    220   L"       7          0    16399    posts 
   TABLE DATA           @   COPY public.posts (title, description, user_id, id) FROM stdin;
    public          postgres    false    218   �"       5          0    16391    users 
   TABLE DATA           C   COPY public.users (name, age, gender, nationality, id) FROM stdin;
    public          postgres    false    216   3#       D           0    0    comments_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.comments_id_seq', 11, true);
          public          postgres    false    221            E           0    0    likes_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.likes_id_seq', 15, true);
          public          postgres    false    219            F           0    0    posts_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.posts_id_seq', 11, true);
          public          postgres    false    217            G           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 5, true);
          public          postgres    false    215            �           2606    16434    comments comments_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_pk;
       public            postgres    false    222            �           2606    16416    likes likes_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_pk;
       public            postgres    false    220            �           2606    16405    posts posts_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_pk;
       public            postgres    false    218            �           2606    16397    users users_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pk;
       public            postgres    false    216            �           2606    16435    comments comments_posts_fk    FK CONSTRAINT     y   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);
 D   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_posts_fk;
       public          postgres    false    218    3483    222            �           2606    16440    comments comments_users_fk    FK CONSTRAINT     y   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);
 D   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_users_fk;
       public          postgres    false    222    3481    216            �           2606    16422    likes likes_posts_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);
 >   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_posts_fk;
       public          postgres    false    3483    218    220            �           2606    16417    likes likes_users_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);
 >   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_users_fk;
       public          postgres    false    216    220    3481            �           2606    16406    posts posts_users_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);
 >   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_users_fk;
       public          postgres    false    218    216    3481            ;   d   x�m�9
�0���È?��]	b!�4����q��˾x?Nq�� ��ٚ�ܞ.dw�BG�����i4l������oiJ���ý�"�
���6#F       9   F   x�˱�0�����.	���s`��J�ef,*.ZS��7G���h�֍�x�����N
��y/����      7   �   x�U��
�0���c�Mt�H�|(�	���L��pnBK*y���M9ρ����&{\� MA� ^��#�}�B�(�b�;�p�JCÂl��ް"�������h��	Q�0t�%��
��7f��"oI      5   V   x���,����46��M�I�,*-.�L��4�r̫L	���Hq�%�d�Q5s�� �M14�p�$V�iE�y���\1z\\\ �4&�     