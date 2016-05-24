-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 24, 2016 at 04:05 PM
-- Server version: 10.0.17-MariaDB
-- PHP Version: 5.5.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crawler`
--

-- --------------------------------------------------------

--
-- Table structure for table `LoginSession`
--

CREATE TABLE `LoginSession` (
  `username` varchar(30) NOT NULL,
  `link_id` int(20) NOT NULL,
  `link_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `RegisteredUser`
--

CREATE TABLE `RegisteredUser` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `email_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Result`
--

CREATE TABLE `Result` (
  `keyword_no` bigint(255) NOT NULL,
  `links` text NOT NULL,
  `keyword` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ukey`
--

CREATE TABLE `ukey` (
  `link_id` bigint(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `keywords` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Url`
--

CREATE TABLE `Url` (
  `url_name` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `name` varchar(50) NOT NULL,
  `email_id` varchar(20) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `dob` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='User Details';

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `uname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `emailid` text NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `name` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `User_details`
--

CREATE TABLE `User_details` (
  `email_id` varchar(20) NOT NULL,
  `dob` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `VerifiedURL`
--

CREATE TABLE `VerifiedURL` (
  `link_id` varchar(30) NOT NULL,
  `domain_name` varchar(30) NOT NULL,
  `webpage` varchar(30) NOT NULL,
  `protocol` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `verifyURL`
--

CREATE TABLE `verifyURL` (
  `status_code` int(11) NOT NULL,
  `link_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `LoginSession`
--
ALTER TABLE `LoginSession`
  ADD PRIMARY KEY (`link_id`),
  ADD UNIQUE KEY `username_2` (`username`,`link_name`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `RegisteredUser`
--
ALTER TABLE `RegisteredUser`
  ADD PRIMARY KEY (`username`,`email_id`),
  ADD KEY `email_id` (`email_id`);

--
-- Indexes for table `Result`
--
ALTER TABLE `Result`
  ADD PRIMARY KEY (`keyword_no`);

--
-- Indexes for table `ukey`
--
ALTER TABLE `ukey`
  ADD PRIMARY KEY (`link_id`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`email_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uname`);

--
-- Indexes for table `User_details`
--
ALTER TABLE `User_details`
  ADD KEY `email_id` (`email_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `LoginSession`
--
ALTER TABLE `LoginSession`
  MODIFY `link_id` int(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Result`
--
ALTER TABLE `Result`
  MODIFY `keyword_no` bigint(255) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `ukey`
--
ALTER TABLE `ukey`
  MODIFY `link_id` bigint(255) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `User_details`
--
ALTER TABLE `User_details`
  ADD CONSTRAINT `emailidfk` FOREIGN KEY (`email_id`) REFERENCES `RegisteredUser` (`email_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
