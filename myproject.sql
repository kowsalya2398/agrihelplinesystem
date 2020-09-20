-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 10, 2020 at 07:54 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `adm_log_details`
--

CREATE TABLE `adm_log_details` (
  `id` int(30) NOT NULL,
  `user_id` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adm_log_details`
--

INSERT INTO `adm_log_details` (`id`, `user_id`, `password`) VALUES
(1, 'monika', 'moni');

-- --------------------------------------------------------

--
-- Table structure for table `agrireg_details`
--

CREATE TABLE `agrireg_details` (
  `id` int(30) NOT NULL,
  `Agrioffid` varchar(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `DOB` int(30) NOT NULL,
  `Gender` varchar(30) NOT NULL,
  `Qualification` varchar(30) NOT NULL,
  `Workexperience` varchar(30) NOT NULL,
  `Worklocation` varchar(30) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `District` varchar(30) NOT NULL,
  `State` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Contactno` bigint(30) NOT NULL,
  `Createpassword` varchar(30) NOT NULL,
  `Confirmpassword` varchar(30) NOT NULL,
  `Photoupload` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `agrireg_details`
--

INSERT INTO `agrireg_details` (`id`, `Agrioffid`, `Name`, `DOB`, `Gender`, `Qualification`, `Workexperience`, `Worklocation`, `Address`, `District`, `State`, `Email`, `Contactno`, `Createpassword`, `Confirmpassword`, `Photoupload`) VALUES
(86, 'agrioff0086', 'vignesh', 0, 'male', 'B.E', '3 years', 'chennai', 'kk nagar', 'chennai', 'tamilnadu', 'monika15699@gmail.com', 9898989898, 'moni', 'moni', '');

-- --------------------------------------------------------

--
-- Table structure for table `farmer_reg_details`
--

CREATE TABLE `farmer_reg_details` (
  `id` int(30) NOT NULL,
  `Farmerid` varchar(30) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `DOB` varchar(30) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `Qualification` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `District` varchar(30) NOT NULL,
  `State` varchar(30) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Contactno` bigint(30) NOT NULL,
  `Createpassword` varchar(30) NOT NULL,
  `Confirmpassword` varchar(30) NOT NULL,
  `Photoupload` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `farmer_reg_details`
--

INSERT INTO `farmer_reg_details` (`id`, `Farmerid`, `Name`, `DOB`, `Gender`, `Qualification`, `Address`, `District`, `State`, `Email`, `Contactno`, `Createpassword`, `Confirmpassword`, `Photoupload`) VALUES
(6, 'farmer0001', 'aakash', '2020-02-11', 'male', 'Any Degree', 'ascac', 'Madurai', 'tn', 'monika15699@gmail.com', 9658869699, 'moni', 'moni', 'nfeek.JPG');

-- --------------------------------------------------------

--
-- Table structure for table `genuser_reg_details`
--

CREATE TABLE `genuser_reg_details` (
  `id` int(30) NOT NULL,
  `Genuserid` varchar(30) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `DOB` varchar(30) NOT NULL,
  `Gender` varchar(30) NOT NULL,
  `Companyname` varchar(30) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `District` varchar(30) NOT NULL,
  `State` varchar(30) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Contactno` bigint(30) NOT NULL,
  `Createpassword` varchar(30) NOT NULL,
  `Confirmpassword` varchar(30) NOT NULL,
  `Photoupload` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `genuser_reg_details`
--

INSERT INTO `genuser_reg_details` (`id`, `Genuserid`, `Name`, `DOB`, `Gender`, `Companyname`, `Address`, `District`, `State`, `Email`, `Contactno`, `Createpassword`, `Confirmpassword`, `Photoupload`) VALUES
(1, 'genuser0001', 'vignesh', '2020-02-14', 'male', 'ss tech', '4/6,ram nagar,sivakasi', 'Chennai', 'tamilnadu', 'monika15699@gmail.com', 9658869699, 'moni', 'moni', 'nfeek.JPG');

-- --------------------------------------------------------

--
-- Table structure for table `student_reg_details`
--

CREATE TABLE `student_reg_details` (
  `id` int(30) NOT NULL,
  `Studentid` varchar(30) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `DOB` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `Qualification` varchar(50) NOT NULL,
  `College` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `District` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Contactno` bigint(50) NOT NULL,
  `Createpassword` varchar(50) NOT NULL,
  `Confirmpassword` varchar(50) NOT NULL,
  `Photoupload` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_reg_details`
--

INSERT INTO `student_reg_details` (`id`, `Studentid`, `Name`, `DOB`, `Gender`, `Qualification`, `College`, `Address`, `District`, `State`, `Email`, `Contactno`, `Createpassword`, `Confirmpassword`, `Photoupload`) VALUES
(5, 'student0005', 'kavin', '2020-02-20', 'male', 'B.Sc(Agri)', 'abc', 'qqw123', 'Coimbatore', 'tn', 'monika15699@gmail.com', 9658869699, '123', '123', 'nfeek.JPG');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adm_log_details`
--
ALTER TABLE `adm_log_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agrireg_details`
--
ALTER TABLE `agrireg_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `farmer_reg_details`
--
ALTER TABLE `farmer_reg_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `genuser_reg_details`
--
ALTER TABLE `genuser_reg_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_reg_details`
--
ALTER TABLE `student_reg_details`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adm_log_details`
--
ALTER TABLE `adm_log_details`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `agrireg_details`
--
ALTER TABLE `agrireg_details`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT for table `farmer_reg_details`
--
ALTER TABLE `farmer_reg_details`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `genuser_reg_details`
--
ALTER TABLE `genuser_reg_details`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `student_reg_details`
--
ALTER TABLE `student_reg_details`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
