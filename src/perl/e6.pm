package e5;


use strict;
use warnings;
use lib "utils";
use lib ".";
use common;
use db; 
use e5;
use Getopt::Long;


sub show_help {
  print("usage: e6.py [-h] [-m | -i | -e] [-u USER] [-c COURSE]

options:
  -h, --help            Muestra este mensaje
  -m, --mostrar         Mostrar lista de inscripciones
  -i, --inscribir       Inscribir
  -e, --eliminar        Eliminar
  -u USER, --usuario USER
                        Usuario a inscribir/eliminar de una inscripción
  -c COURSE, --curso COURSE
                        Curso donde inscribir/eliminar la inscripción del usuario");  
};


sub parser_values_are_valid {

    my ($show_enrollments,$create_enrollment,$delete_enrollment,$user,$course) = @_;

    my $no_given_operation = !$show_enrollments && !$create_enrollment && !$delete_enrollment; 

    if($no_given_operation){
        print "Error: debes ingresar al menos una operación (-m,-i,-e)";
        return 0;
    };

    my $user_or_course_not_defined = !$user || !$course;

    if(!$show_enrollments && $user_or_course_not_defined) {
        print "Error: si ingresa las opciones -i,--inscribir o -e,--eliminar, debe especificar el usuario (-u,--usuario) y el curso (-c,--curso)";
        return 0;
    };

    return 1;
};


sub get_user {
    
    my @params = ($_[0]);
    return db::fetch_one("SELECT * FROM usuarios u WHERE u.id_usuario = ?",\@params);
};


sub get_course {
    
    my @params = ($_[0]);
    return db::fetch_one("SELECT * FROM cursos c WHERE c.id_curso = ?",\@params);
};


sub user_and_course_values_are_valid {

    my ($user,$course) = @_;
    
    if(!$user){
        print "EL USUARIO INGRESADO NO EXISTE";
        return 0;
    };

    if(!$course){
        print "EL CURSO INGRESADO NO EXISTE";
        return 0;
    };

    return 1;
};


sub existing_enrollment {

    my ($student_id,$student_name,$student_surname) = @{$_[0]};
    my ($course_id,$course_name) = @{$_[1]};

    my @params = ($student_id,$course_id);

    my $enrollment = db::fetch_one("SELECT * FROM usuarios_cursos WHERE id_alumno = ? AND id_curso = ?", \@params);

    if(!$enrollment){return 0};

    print "YA EXISTE UNA INSCRIPCIÓN DEL USUARIO $student_name $student_surname (ID: $student_id) AL CURSO $course_name (ID: $course_id)";
    return 1;
};


sub create_enrollment {
    my ($student_id,$student_name,$student_surname) = @{$_[0]};
    my ($course_id,$course_name) = @{$_[1]};

    my @params = ($course_id,$student_id);

    db::execute("INSERT INTO usuarios_cursos VALUES (?,?)",\@params);
    print "SE HA INSCRIPTO AL USUARIO $student_name $student_surname (ID: $student_id) AL CURSO $course_name (ID: $course_id)";
};


sub delete_enrollment {
    my ($student_id,$student_name,$student_surname) = @{$_[0]};
    my ($course_id,$course_name) = @{$_[1]};

    my @params = ($course_id,$student_id);

    db::execute("DELETE FROM usuarios_cursos WHERE id_curso = ? AND id_alumno = ?",\@params);
    print "SE HA ELIMINADO LA INSCRIPCIÓN DEL USUARIO $student_name $student_surname (ID: $student_id) AL CURSO $course_name (ID: $course_id)";
};


sub main{

    common::clear();

    my $show_enrollments = 0;
    my $create_enrollment = 0;
    my $delete_enrollment = 0;
    my $user_value;
    my $course_value;

    GetOptions(
        'mostrar|m' => \$show_enrollments,
        'inscribir|i' => \$create_enrollment,
        'eliminar|e' => \$delete_enrollment,
        'usuario|u=i' => \$user_value,
        'curso|c=i' => \$course_value,
    ) or die show_help();

    parser_values_are_valid($show_enrollments,$create_enrollment,$delete_enrollment,$user_value,$course_value) || die;

    if($show_enrollments){
        
        e5::show_enrollments();
    }
    else{

        my $user = get_user($user_value);
        my $course = get_course($course_value);

        if(!user_and_course_values_are_valid($user,$course)){return};

        if($create_enrollment && !existing_enrollment($user,$course)){create_enrollment($user,$course)}
        
        elsif($delete_enrollment){delete_enrollment($user,$course)};

    };
};


if($0 eq __FILE__){
    
    main();
};


1;