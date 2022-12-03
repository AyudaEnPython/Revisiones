-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2021 a las 14:57:40
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `automotoradb`
--
CREATE DATABASE IF NOT EXISTS `automotoradb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `automotoradb`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Vehículos`
--

CREATE TABLE `automovil` (
  `patente` varchar(12) NOT NULL,
  `marca` text(20) NOT NULL,
  `año` int(4) NOT NULL,
  `kilometraje` int(20) NOT NULL,
  `tipo_combustible` text (20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `automovil`
--

INSERT INTO `automovil` (`patente`, `marca`, `año`, `kilometraje`, `tipo_combustible`) VALUES
('AABB00', 'KIA', '2015', 80.000, 'Bencina'),
('BBCC11', 'FORD', '2018', 50.000, 'Petroleo'),
('CCDD22', 'CHEVROLET', '2021', 30.000, 'Petroleo'),
('DDEE33', 'BMW', '2022', 12.000, 'Bencina'),
('EEFF44', 'MAZDA', '2022', 10.000, 'Bencina'),
('FFGG55', 'NISSAN', '2017', 100.000, 'Petroleo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `automovil`
--
ALTER TABLE `automovil`
  ADD PRIMARY KEY (`patente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;