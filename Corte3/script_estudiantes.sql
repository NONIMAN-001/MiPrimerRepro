-- Script para crear la base de datos ----> bdestudiantes		              
-- KEVIN ANGARITA, JUAN BOHORQUEZ             
-- \i c:/Taller/script_estudiantes.sql

-------------------------------------------------------------------------
-- 01.- BLOQUE CREAR BD_ESTUDIANTES
SELECT 'Paso 00: Bloque Crear bdestudiantes.....'  AS paso, pg_sleep(5);
SELECT '.........................................'  AS paso, pg_sleep(0);
----------

\! cls
\c postgres

SELECT 'Paso 01.1: Iniciando el Script .....'  AS paso, pg_sleep(01);
SELECT 'Paso 01.2: Listado de las BDs .....'  AS paso, pg_sleep(02);
\l

-- 0 Eliminando la base de datos si existe
--
SELECT 'Paso 01.3: Eliminar  bdestudiantes si Existe .....'  AS paso, pg_sleep(02);
DROP DATABASE IF EXISTS bdestudiantes;

-- Listado de las bases de datos
\l
\! cls

SELECT 'Paso 01.4: Crear bdestudiantes; .....'  AS paso, pg_sleep(05);
CREATE DATABASE  bdestudiantes  with ENCODING='UTF8';


SELECT 'Paso 01.5: Conectandose a bdestudiantes .....'  AS paso, pg_sleep(05);
\c bdestudiantes
-------------------------------------------------------------------------
-- 02.- BLOQUE DE CREACIÓN DE TABLAS
SELECT 'Paso 02: Bloque Crear TABLAS .....'  AS paso, pg_sleep(05);
SELECT '.........................................'  AS paso, pg_sleep(0);
-------------------------------------------------------------------------

-- TMESTADOS
SELECT 'Paso 02.01: TMESTADOS ....................'  AS paso, pg_sleep(02);
CREATE  TABLE  tmestados(
	pkcods	 INTEGER	  not null      primary key  ,
	destados varchar(12)    not null) ;

--insertar TMESTADOS

INSERT    INTO   tmestados  (pkcods,destados)  VALUES  (0,  'ELIMINADO'); 
INSERT    INTO   tmestados  (pkcods,destados)  VALUES  (1,  'ACTIVO'); 

-------------------------------------------------------------------------

-- TMESTUDIANTES
SELECT 'Paso 02.02: TMESTUDIANTES ................'  AS paso, pg_sleep(03);

CREATE TABLE tmestudiantes(
    pkid_estudiante INTEGER NOT NULL PRIMARY KEY,
    nombre_estudiante varchar(50) not null,
    apellido_estudiante varchar(50) not null,
    edad_estudiante integer not null,
    fkcodsta integer not null,
    FOREIGN KEY (fkcodsta) references tmestados(pkcods) on update cascade on delete restrict
);

-- Insertar datos en TMESTUDIANTES
INSERT INTO tmestudiantes (pkid_estudiante, nombre_estudiante, apellido_estudiante, edad_estudiante, fkcodsta) VALUES
(1, 'Juan', 'Perez', 20, 1),
(2, 'Maria', 'Gomez', 22, 1);

-------------------------------------------------------------------------

-- TDREGISTROS
SELECT 'Paso 02.03: TDREGISTROS ..................'  AS paso, pg_sleep(03);
CREATE TABLE tdregistros(
    pkid_registro integer not null primary key,
    fkid_estudiante integer not null,
    fecha_registro date not null,
    fkcods_registro integer not null,
    FOREIGN KEY (fkcods_registro) references tmestados(pkcods) on update cascade on delete restrict,
    FOREIGN KEY (fkid_estudiante) references tmestudiantes(pkid_estudiante) on update cascade on delete restrict
);

-- Insertar datos en TDREGISTROS
INSERT INTO tdregistros (pkid_registro, fkid_estudiante, fecha_registro, fkcods_registro) VALUES
(1, 1, '2025-01-01', 1), 
(2, 2, '2025-01-02', 1);  

--- CONSULTAS DE VERIFICACIÓN DE DATOS INSERTADOS
-------------------------------------------------------------------------
SELECT * FROM  tmestados; 
SELECT * FROM tmestudiantes;
SELECT * FROM tdregistros;
-------------------------------------------------------------------------