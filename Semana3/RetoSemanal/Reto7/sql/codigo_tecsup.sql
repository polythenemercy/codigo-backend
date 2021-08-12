-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 13, 2021 at 01:23 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 5.6.39

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codigo_tecsup`
--

-- --------------------------------------------------------

--
-- Table structure for table `datainfo`
--

CREATE TABLE `datainfo` (
  `IdReg` int(11) NOT NULL,
  `DataValue` varchar(250) CHARACTER SET latin1 NOT NULL,
  `DateRegister` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datainfo`
--

INSERT INTO `datainfo` (`IdReg`, `DataValue`, `DateRegister`) VALUES
(1, 'Dato almacenado #1', '2021-08-12 22:07:29'),
(2, 'Intento de grabado #1', '2021-08-12 23:12:34');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `datainfo`
--
ALTER TABLE `datainfo`
  ADD PRIMARY KEY (`IdReg`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `datainfo`
--
ALTER TABLE `datainfo`
  MODIFY `IdReg` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
