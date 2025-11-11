-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 05:47 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `id` int(11) NOT NULL,
  `ten_danhmuc` varchar(100) NOT NULL,
  `mo_ta` text DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`id`, `ten_danhmuc`, `mo_ta`, `trang_thai`) VALUES
(1, 'Hot Sale', 'Tổng hợp các sản phẩm đang được giảm giá mạnh và khuyến mãi đặc biệt.', 1),
(3, 'Thực phẩm chức năng', 'Cung cấp các sản phẩm hỗ trợ sức khỏe, bổ sung vitamin và khoáng chất.', 1),
(4, 'Thiết bị, dụng cụ y tế', 'Bao gồm nhiệt kế, máy đo huyết áp, khẩu trang, bông băng y tế và các dụng cụ chăm sóc sức khỏe.', 1),
(5, 'Dược mỹ phẩm', 'Các sản phẩm làm đẹp có nguồn gốc dược phẩm, an toàn cho da và được khuyên dùng bởi chuyên gia da liễu.', 1),
(6, 'Chăm sóc cá nhân', 'Sản phẩm chăm sóc răng miệng, da, tóc và vệ sinh cá nhân hằng ngày.', 1),
(7, 'Chăm sóc trẻ em', 'Sản phẩm dành riêng cho trẻ nhỏ như sữa tắm, dầu gội, kem dưỡng, và thực phẩm bổ sung.', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `id` int(11) NOT NULL,
  `ten_sanpham` varchar(255) NOT NULL,
  `gia_goc` decimal(10,2) NOT NULL,
  `gia_giam` decimal(10,2) DEFAULT NULL,
  `phan_tram_giam` tinyint(4) DEFAULT NULL,
  `so_suat` int(11) DEFAULT 0,
  `da_ban` int(11) DEFAULT 0,
  `hinh_anh` varchar(255) DEFAULT NULL,
  `id_danhmuc` int(11) DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`id`, `ten_sanpham`, `gia_goc`, `gia_giam`, `phan_tram_giam`, `so_suat`, `da_ban`, `hinh_anh`, `id_danhmuc`, `trang_thai`) VALUES
(1, 'Nước tẩy trang Bioderma Sensibio', 535000.00, 398750.00, 25, 20, 16, 'bioderma.jpg', 1, 1),
(2, 'Tăm chỉ nha khoa Okamura 734503', 22000.00, 18000.00, 18, 20, 20, 'okamura.jpg', 6, 1),
(3, 'Nước súc miệng Listerine Cool Mint', 169000.00, 81000.00, 52, 20, 16, 'listerine.jpg', 6, 1),
(4, 'Nước Yến Collagen Green Bird Nutrinest', 30000.00, 22500.00, 25, 60, 60, 'greenbird.jpg', 3, 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_danhmuc` (`id_danhmuc`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`id_danhmuc`) REFERENCES `danhmuc` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
