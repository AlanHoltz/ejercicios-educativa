package e4;


use strict;
use warnings;
use lib "utils";
use common;
use db; 


sub main{

    common::clear();
    
    my @tables = (
    "CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_usuario)
    )",

    "CREATE TABLE IF NOT EXISTS cursos(
    id_curso INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,   
    cupo INT UNSIGNED NOT NULL,
    id_docente INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_curso)
    )",

    "CREATE TABLE IF NOT EXISTS usuarios_cursos(
    id_curso INT UNSIGNED NOT NULL,
    id_alumno INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_curso,id_alumno),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
    FOREIGN KEY (id_alumno) REFERENCES usuarios(id_usuario)
    )"
    );

    my $db_conn = db::get_db_connection();

    foreach my $query (@tables){
        $db_conn -> do($query);
    };

    $db_conn -> disconnect();

    print "LAS TABLAS usuarios, cursos y usuarios_cursos HAN SIDO CREADAS CORRECTAMENTE"; 
};


if($0 eq __FILE__){
    
    main();
};


1;