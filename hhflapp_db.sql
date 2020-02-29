-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 29, 2020 at 10:52 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hhflapp_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add user', 3, 'add_user'),
(10, 'Can change user', 3, 'change_user'),
(11, 'Can delete user', 3, 'delete_user'),
(12, 'Can view user', 3, 'view_user'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$180000$31QuUciWD4Sw$VBh3aa2DX+YvciNY6N7a4GSZmVAkVHZzNj0tjSd8vjA=', '2020-02-29 08:23:44.552337', 1, 'admin', '', '', '', 1, 1, '2020-01-10 11:27:54.846304'),
(3, 'pbkdf2_sha256$180000$MggxY327EKb0$kNz8N0Vj6Hx5ucC64jyqnRNcnUSpyNGYiLpRRWDBUaU=', NULL, 0, 'Dhananjay', '', '', '', 0, 1, '2020-01-10 11:37:51.560274'),
(4, 'pbkdf2_sha256$180000$JqvLP0NIy9wz$ikJHJ3WGlULsEIofCRADqHl2KJaXCtMdmYwVUyl04u0=', NULL, 0, 'neeraj', '', '', '', 0, 1, '2020-01-10 11:38:13.918329'),
(5, 'pbkdf2_sha256$180000$vs2GBkLFzGtC$rlp8xneNQt36KwKy3nASGTij3fz+rvoFP2zZhky9fc0=', NULL, 0, 'chetan', '', '', '', 1, 1, '2020-01-10 11:47:46.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0az03ecekryw2q5elogekkulgcy1anpz', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-09 11:40:06.258703'),
('2pg4j95v3jlmzesxrr4r6f1i9p64g7x1', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-02-03 07:43:30.776977'),
('312gedqrmmwwsmkt59f6a8rzb7z0bzi6', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-02-05 12:00:57.642122'),
('39h1k2cm6vz7r72yu5riqu4uyluvf6w1', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-06 12:46:35.805677'),
('3b057t859xyxzrrqtlaa45n6ki40tjgc', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-06 13:48:01.396473'),
('6tegf1nratrg5ju18dnpx7q9odu8bzdf', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-11 07:32:10.141606'),
('74xv37v2ay4ex5481m2my5baec5986iq', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-13 09:15:16.872634'),
('7cw0h0e17euqkoy9zxa88kvuk33glu1c', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-01-29 09:11:16.869498'),
('922fsbdimb77my35iittjip9ua8hue2v', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-11 10:20:41.085838'),
('dino4i5vx6zxzlmzjh1ntr0brrgxcqu5', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-06 09:55:31.472374'),
('hk2igfuekdphja8iu703207cfs7ucwvg', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-09 12:03:57.875156'),
('hwe565r1sr8zs3pakcgqga5a7gldgzgp', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-02-19 11:22:25.773221'),
('it9ievtfqy1edqgwppi11dkepaxxebh4', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-06 11:37:45.600543'),
('jv7dkcsrs2p416ndsfhef2qnn96wgjgz', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-02-05 11:37:33.737852'),
('m7x2mxl0hp1sjbi3994oi132c6fv9w3i', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-01-24 11:28:04.834938'),
('o6m2cahscdt41hsejhpavg5bfk5a9deq', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-11 07:22:50.601760'),
('peg75io113kshgrp9udczw7w3u72mw93', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-10 14:35:54.103582'),
('rb5dfcq4t2ax8yny2bhko7a0r6sxr3l7', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-01-29 06:18:04.572930'),
('teecu3emwc6l5776qtct7k2hum0gdwpf', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-09 05:48:30.787454'),
('tk8vuvuzi6ieq656i1oavy7u1y2b4jnl', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-10 10:44:01.008761'),
('y3miiwtigad0vwf2dz4bv2zrgqfzft2c', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-06 10:31:26.318633'),
('yivbd3kra0ytshc9y176814bea2roqph', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-06 14:47:00.234005'),
('z33jhcipoifoxemf7m46yxlue7mbw3vj', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-03-14 08:23:44.562400'),
('zel29841dv1sdvv0hejf6l1o98hc5z87', 'NTBiNmVmMjY4ZTFjYmIxNjIyODEyOTU4NjAyNjVjMzY5Nzc2MzdmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjVmMWRhNGRlNzkxODJmZTU0Mzg3M2YxY2M3NjMxNDA2ODMwOGIwIn0=', '2020-02-03 06:03:36.095515');

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_app_tracker`
--

CREATE TABLE `hhfl_app_tracker` (
  `id` int(11) NOT NULL,
  `case_id` int(11) NOT NULL,
  `created_on` varchar(20) NOT NULL,
  `app_status` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hhfl_app_tracker`
--

INSERT INTO `hhfl_app_tracker` (`id`, `case_id`, `created_on`, `app_status`) VALUES
(1, 1, '31-12-1985', 1),
(2, 2, '31-12-1985', 1);

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_bank_statements`
--

CREATE TABLE `hhfl_bank_statements` (
  `id` int(11) NOT NULL,
  `doc_dtl_id` int(11) NOT NULL,
  `bank_id` int(11) NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  `is_verified` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hhfl_bank_statements`
--

INSERT INTO `hhfl_bank_statements` (`id`, `doc_dtl_id`, `bank_id`, `bank_name`, `is_verified`) VALUES
(1, 1, 1, 'Bank Of India', 0),
(2, 1, 2, 'State Bank Of India', 0);

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_bank_statements_dtl`
--

CREATE TABLE `hhfl_bank_statements_dtl` (
  `id` int(11) NOT NULL,
  `bank_stat_id` int(11) NOT NULL,
  `Date` date NOT NULL DEFAULT current_timestamp(),
  `Description` varchar(100) NOT NULL,
  `cheque_no` int(10) NOT NULL,
  `credit` varchar(255) NOT NULL,
  `debit` varchar(255) NOT NULL,
  `balance` float NOT NULL,
  `value_date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hhfl_bank_statements_dtl`
--

INSERT INTO `hhfl_bank_statements_dtl` (`id`, `bank_stat_id`, `Date`, `Description`, `cheque_no`, `credit`, `debit`, `balance`, `value_date`) VALUES
(1, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(2, 1, '2020-02-21', 'Bank Statement EMI 2', 123456789, '1000', '2000', 30000, '2020-02-21'),
(3, 2, '2020-02-21', 'Bank Statement EMI 2', 123456789, '1000', '2000', 50000, '2020-02-21'),
(4, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(5, 1, '2020-02-21', 'dhananjay', 123456789, '5000', '1000', 0, '2020-02-21'),
(6, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(7, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(8, 1, '2020-02-21', 'dsdsBank Statement EMI 2', 123456789, '1000', '2000', 30000, '2020-02-21'),
(9, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(10, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(11, 1, '2020-02-21', 'dhananjay', 123456789, '5000', '1000', 0, '2020-02-21'),
(12, 1, '2020-02-21', 'dsdsBank Statement EMI 2', 123456789, '1000', '2000', 30000, '2020-02-21'),
(13, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(14, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(15, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(16, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(17, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(18, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(19, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(20, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(21, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(22, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(23, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(24, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(25, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(26, 1, '2020-02-21', 'fghfghfgh', 123456789, '5000', '1000', 0, '2020-02-21'),
(27, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(28, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(29, 1, '2020-02-21', 'Bank Statement EMI 2', 123456789, '1000', '2000', 30000, '2020-02-21'),
(30, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21'),
(31, 1, '2020-02-21', 'Bank Statement EMIghg', 123456789, '5000', '1000', 0, '2020-02-21'),
(32, 1, '2020-02-21', 'Bank Statement EMI', 123456789, '5000', '1000', 0, '2020-02-21');

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_customer_dtl`
--

CREATE TABLE `hhfl_customer_dtl` (
  `id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  `cust_detail_no` varchar(50) NOT NULL,
  `applicant_type` varchar(20) NOT NULL,
  `cust_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hhfl_customer_dtl`
--

INSERT INTO `hhfl_customer_dtl` (`id`, `app_id`, `cust_detail_no`, `applicant_type`, `cust_name`) VALUES
(1, 1, '1111', 'Applicant', 'Dhananjay'),
(2, 1, '2222', 'Co-Applicant', 'Kuldeep');

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_dataentry`
--

CREATE TABLE `hhfl_dataentry` (
  `id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  `filed_1` varchar(20) NOT NULL,
  `filed_2` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_document_dtl`
--

CREATE TABLE `hhfl_document_dtl` (
  `id` int(11) NOT NULL,
  `doc_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hhfl_document_dtl`
--

INSERT INTO `hhfl_document_dtl` (`id`, `doc_id`, `cust_id`, `filepath`) VALUES
(1, 1, 1, 'D:/Doc');

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_document_mst`
--

CREATE TABLE `hhfl_document_mst` (
  `id` int(11) NOT NULL,
  `doc_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hhfl_document_mst`
--

INSERT INTO `hhfl_document_mst` (`id`, `doc_name`) VALUES
(1, 'Cibil');

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_exception_dtl`
--

CREATE TABLE `hhfl_exception_dtl` (
  `id` int(11) NOT NULL,
  `process_dtl_id` int(11) NOT NULL,
  `exception_dtl` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_process_dtl`
--

CREATE TABLE `hhfl_process_dtl` (
  `id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  `process_id` int(11) NOT NULL,
  `status` varchar(1) NOT NULL,
  `start_time` varchar(20) NOT NULL,
  `end_time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_process_mst`
--

CREATE TABLE `hhfl_process_mst` (
  `id` int(11) NOT NULL,
  `process_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `hhfl_status_mst`
--

CREATE TABLE `hhfl_status_mst` (
  `id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hhfl_status_mst`
--

INSERT INTO `hhfl_status_mst` (`id`, `status`) VALUES
(1, '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `hhfl_app_tracker`
--
ALTER TABLE `hhfl_app_tracker`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hhfl_app_tracker_fk0` (`app_status`);

--
-- Indexes for table `hhfl_bank_statements`
--
ALTER TABLE `hhfl_bank_statements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hhfl_bank_statements_fk0` (`doc_dtl_id`);

--
-- Indexes for table `hhfl_bank_statements_dtl`
--
ALTER TABLE `hhfl_bank_statements_dtl`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hhfl_bank_statements_dtl_fk0` (`bank_stat_id`);

--
-- Indexes for table `hhfl_customer_dtl`
--
ALTER TABLE `hhfl_customer_dtl`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hhfl_customer_dtl_fk0` (`app_id`);

--
-- Indexes for table `hhfl_dataentry`
--
ALTER TABLE `hhfl_dataentry`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hhfl_dataentry_fk0` (`app_id`);

--
-- Indexes for table `hhfl_document_dtl`
--
ALTER TABLE `hhfl_document_dtl`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hhfl_document_dtl_fk0` (`doc_id`),
  ADD KEY `hhfl_document_dtl_fk1` (`cust_id`);

--
-- Indexes for table `hhfl_document_mst`
--
ALTER TABLE `hhfl_document_mst`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hhfl_exception_dtl`
--
ALTER TABLE `hhfl_exception_dtl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hhfl_process_dtl`
--
ALTER TABLE `hhfl_process_dtl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hhfl_process_mst`
--
ALTER TABLE `hhfl_process_mst`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hhfl_status_mst`
--
ALTER TABLE `hhfl_status_mst`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hhfl_app_tracker`
--
ALTER TABLE `hhfl_app_tracker`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hhfl_bank_statements`
--
ALTER TABLE `hhfl_bank_statements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hhfl_bank_statements_dtl`
--
ALTER TABLE `hhfl_bank_statements_dtl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `hhfl_customer_dtl`
--
ALTER TABLE `hhfl_customer_dtl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hhfl_dataentry`
--
ALTER TABLE `hhfl_dataentry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hhfl_document_dtl`
--
ALTER TABLE `hhfl_document_dtl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `hhfl_document_mst`
--
ALTER TABLE `hhfl_document_mst`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `hhfl_exception_dtl`
--
ALTER TABLE `hhfl_exception_dtl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hhfl_process_dtl`
--
ALTER TABLE `hhfl_process_dtl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hhfl_process_mst`
--
ALTER TABLE `hhfl_process_mst`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hhfl_status_mst`
--
ALTER TABLE `hhfl_status_mst`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `hhfl_app_tracker`
--
ALTER TABLE `hhfl_app_tracker`
  ADD CONSTRAINT `hhfl_app_tracker_fk0` FOREIGN KEY (`app_status`) REFERENCES `hhfl_status_mst` (`id`);

--
-- Constraints for table `hhfl_bank_statements`
--
ALTER TABLE `hhfl_bank_statements`
  ADD CONSTRAINT `hhfl_bank_statements_fk0` FOREIGN KEY (`doc_dtl_id`) REFERENCES `hhfl_document_dtl` (`id`);

--
-- Constraints for table `hhfl_bank_statements_dtl`
--
ALTER TABLE `hhfl_bank_statements_dtl`
  ADD CONSTRAINT `hhfl_bank_statements_dtl_fk0` FOREIGN KEY (`bank_stat_id`) REFERENCES `hhfl_bank_statements` (`id`);

--
-- Constraints for table `hhfl_customer_dtl`
--
ALTER TABLE `hhfl_customer_dtl`
  ADD CONSTRAINT `hhfl_customer_dtl_fk0` FOREIGN KEY (`app_id`) REFERENCES `hhfl_app_tracker` (`id`);

--
-- Constraints for table `hhfl_dataentry`
--
ALTER TABLE `hhfl_dataentry`
  ADD CONSTRAINT `hhfl_dataentry_fk0` FOREIGN KEY (`app_id`) REFERENCES `hhfl_app_tracker` (`id`);

--
-- Constraints for table `hhfl_document_dtl`
--
ALTER TABLE `hhfl_document_dtl`
  ADD CONSTRAINT `hhfl_document_dtl_fk0` FOREIGN KEY (`doc_id`) REFERENCES `hhfl_document_mst` (`id`),
  ADD CONSTRAINT `hhfl_document_dtl_fk1` FOREIGN KEY (`cust_id`) REFERENCES `hhfl_customer_dtl` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
