-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 07, 2023 lúc 11:50 AM
-- Phiên bản máy phục vụ: 10.4.27-MariaDB
-- Phiên bản PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlnv`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `checkin`
--

CREATE TABLE `checkin` (
  `staffId` varchar(10) NOT NULL,
  `checkInTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `checkout`
--

CREATE TABLE `checkout` (
  `staffId` varchar(10) NOT NULL,
  `checkOutTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `staff`
--

CREATE TABLE `staff` (
  `id` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `birthday` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `checkin`
--
ALTER TABLE `checkin`
  ADD PRIMARY KEY (`checkInTime`),
  ADD KEY `staffId` (`staffId`);

--
-- Chỉ mục cho bảng `checkout`
--
ALTER TABLE `checkout`
  ADD PRIMARY KEY (`checkOutTime`),
  ADD KEY `staffId` (`staffId`);

--
-- Chỉ mục cho bảng `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `checkin`
--
ALTER TABLE `checkin`
  ADD CONSTRAINT `check_ibfk_in` FOREIGN KEY (`staffId`) REFERENCES `staff` (`id`);
COMMIT;

--
-- Các ràng buộc cho bảng `checkout`
--
ALTER TABLE `checkout`
  ADD CONSTRAINT `check_ibfk_out` FOREIGN KEY (`staffId`) REFERENCES `staff` (`id`);
COMMIT;

--
-- Insert dữ liệu 
--

INSERT INTO `staff` (`id`,`name`,`birthday`) VALUES
('0417','Nguyễn Ngọc Sơn','2003-05-16'),
('0426','Nguyễn Ngọc Sang','2003-08-21'),
('0433','Nguyễn Thành Đạt','2003-05-20');


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
