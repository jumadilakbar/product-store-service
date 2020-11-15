-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 15, 2020 at 07:03 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bajigur`
--

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(100) NOT NULL,
  `permittion` varchar(100) NOT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `update_at` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`role_id`, `role_name`, `permittion`, `create_at`, `update_at`, `status`) VALUES
(1, 'karyawan', '1,2,3,4,5,6,7', '2019-11-19 07:45:18', '', 'aktif');

-- --------------------------------------------------------

--
-- Table structure for table `tb_asosiasi_product`
--

CREATE TABLE `tb_asosiasi_product` (
  `produk_id` int(1) DEFAULT NULL,
  `relate_product_id` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_asosiasi_product`
--

INSERT INTO `tb_asosiasi_product` (`produk_id`, `relate_product_id`) VALUES
(1, '2,3'),
(2, '1,2,6'),
(3, '2,1,5'),
(4, '10,8,4'),
(5, '6,10,7');

-- --------------------------------------------------------

--
-- Table structure for table `tb_color`
--

CREATE TABLE `tb_color` (
  `color_id` int(1) NOT NULL,
  `color_name` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_color`
--

INSERT INTO `tb_color` (`color_id`, `color_name`) VALUES
(1, 'biru dongker'),
(2, 'ping'),
(3, 'nila'),
(4, 'orange'),
(5, 'maroon');

-- --------------------------------------------------------

--
-- Table structure for table `tb_kategori`
--

CREATE TABLE `tb_kategori` (
  `kategori_id` int(11) NOT NULL,
  `kategori_name` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_kategori`
--

INSERT INTO `tb_kategori` (`kategori_id`, `kategori_name`) VALUES
(1, 'Kaos'),
(2, 'Kemeja'),
(3, 'Celana'),
(4, 'Tas'),
(5, 'Jaket'),
(6, 'Asesoris');

-- --------------------------------------------------------

--
-- Table structure for table `tb_product_list`
--

CREATE TABLE `tb_product_list` (
  `product_id` int(11) NOT NULL,
  `product_name` text DEFAULT NULL,
  `price` int(6) DEFAULT NULL,
  `stock` int(2) DEFAULT NULL,
  `rating` decimal(2,1) DEFAULT NULL,
  `id_kategori` int(1) DEFAULT NULL,
  `id_color` varchar(50) DEFAULT NULL,
  `create_at` varchar(10) DEFAULT NULL,
  `update_at` varchar(10) DEFAULT NULL,
  `create_by` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_product_list`
--

INSERT INTO `tb_product_list` (`product_id`, `product_name`, `price`, `stock`, `rating`, `id_kategori`, `id_color`, `create_at`, `update_at`, `create_by`) VALUES
(1, 'Baju A', 100000, 12, '4.5', 1, '1,2,4,5', '', '', ''),
(2, 'Tshirt B', 122000, 11, '4.0', 1, '2,3,5', '', '', ''),
(3, 'Celana Jeans A', 200000, 11, '5.0', 3, '3,6', '', '', ''),
(4, 'Kaos kaki Belang', 40000, 23, '5.0', 1, '4,1', '', '', ''),
(5, 'Gelang Oke', 12000, 42, '3.0', 6, '1,5,6', '', '', ''),
(6, 'Tas ekece', 176000, 10, '2.0', 4, '2,6', '', '', ''),
(7, 'Baju kemeja tamvan', 110100, 3, '4.0', 2, '3,4,6', '', '', ''),
(8, 'Baju polo Mesra', 96000, 6, '4.3', 1, '6', '', '', ''),
(9, 'Tas greget', 200000, 10, '5.0', 4, '1,2', '', '', ''),
(10, 'Jaket Mantan', 230000, 12, '4.9', 5, '2,4', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `tb_recomendasi_similarity`
--

CREATE TABLE `tb_recomendasi_similarity` (
  `product_id` int(2) DEFAULT NULL,
  `similar_product_id` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_recomendasi_similarity`
--

INSERT INTO `tb_recomendasi_similarity` (`product_id`, `similar_product_id`) VALUES
(1, '3,2'),
(2, '1,2'),
(3, '4,5'),
(4, '3,5'),
(5, '3,4'),
(6, '7,8'),
(7, '6,8'),
(8, '6,7'),
(9, '10,8'),
(10, '9,7');

-- --------------------------------------------------------

--
-- Table structure for table `tb_rekomendation_history`
--

CREATE TABLE `tb_rekomendation_history` (
  `user_id` int(4) DEFAULT NULL,
  `product_id` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_rekomendation_history`
--

INSERT INTO `tb_rekomendation_history` (`user_id`, `product_id`) VALUES
(1, 1),
(1, 2),
(1, 4),
(1225, 7),
(1225, 8),
(1225, 9);

-- --------------------------------------------------------

--
-- Table structure for table `tb_rekomendation_order`
--

CREATE TABLE `tb_rekomendation_order` (
  `user_id` int(4) DEFAULT NULL,
  `product_id` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_rekomendation_order`
--

INSERT INTO `tb_rekomendation_order` (`user_id`, `product_id`) VALUES
(1, 1),
(1, 2),
(1, 4),
(1, 5),
(1, 7),
(1, 10),
(1225, 1),
(1225, 4),
(1225, 5),
(1225, 6),
(1225, 7),
(1225, 8),
(1225, 9),
(1225, 2),
(1225, 3);

-- --------------------------------------------------------

--
-- Table structure for table `tb_tranding_product`
--

CREATE TABLE `tb_tranding_product` (
  `id_prduct` int(2) DEFAULT NULL,
  `skor_tranding` varchar(3) DEFAULT NULL,
  `start_time` varchar(10) DEFAULT NULL,
  `end_time` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_tranding_product`
--

INSERT INTO `tb_tranding_product` (`id_prduct`, `skor_tranding`, `start_time`, `end_time`) VALUES
(1, '0,5', '10-10-2020', '11-10-2020'),
(2, '0,3', '10-11-2020', '11-11-2020'),
(3, '0,2', '10-12-2020', '11-12-2020'),
(10, '0,1', '10-13-2020', '11-13-2020');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(100) NOT NULL,
  `role_id` text NOT NULL,
  `username` varchar(50) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `email` text NOT NULL,
  `password` varchar(100) NOT NULL,
  `birthday` varchar(20) NOT NULL,
  `address` text NOT NULL,
  `website` text NOT NULL,
  `status` varchar(20) NOT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `update_at` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `role_id`, `username`, `fullname`, `email`, `password`, `birthday`, `address`, `website`, `status`, `create_at`, `update_at`) VALUES
(1, '1', 'adil', 'muhamad jumadil akbar', 'muhamadjumadilakbar@gmail.com', 'rahasia', '15/11/1996', 'yogyakarta', 'http://codekita.com', '1', '2020-11-15 16:08:09', ''),
(1225, '1', 'user1', 'user1', 'user1@test@com', '12345678', '15/11/1996', 'location test', '-', '1', '2020-11-15 16:08:13', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `tb_color`
--
ALTER TABLE `tb_color`
  ADD PRIMARY KEY (`color_id`);

--
-- Indexes for table `tb_kategori`
--
ALTER TABLE `tb_kategori`
  ADD PRIMARY KEY (`kategori_id`);

--
-- Indexes for table `tb_product_list`
--
ALTER TABLE `tb_product_list`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_color`
--
ALTER TABLE `tb_color`
  MODIFY `color_id` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_kategori`
--
ALTER TABLE `tb_kategori`
  MODIFY `kategori_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tb_product_list`
--
ALTER TABLE `tb_product_list`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1226;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
