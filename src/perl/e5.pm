package e5;


use strict;
use warnings;
use lib "utils";
use lib ".";
use common;
use db; 
use e3;
use Text::Table;


sub get_enrollments {
    
    my @enrollments = ();

    my @users = @{$_[0]};
    
    foreach my $user (@users){
        my $user_id = $user -> {id};
        my $user_courses = $user -> {id_curso};
        foreach my $course (@{$user_courses}){
            my $enrollment = ();
            $enrollment -> {course_id} = $course;
            $enrollment -> {user_id} = $user_id;
            push(@enrollments, $enrollment);
        };
    };

    return \@enrollments;
};

sub show_enrollments {
    my $db_conn = db::get_db_connection();

    my $stmt = $db_conn -> prepare('SELECT 
    uc.id_alumno,uc.id_curso,
    CONCAT(u.nombre," ",u.apellido) AS "nombre y apellido usuario",
    c.nombre 
    FROM usuarios_cursos uc
    INNER JOIN usuarios u ON u.id_usuario = uc.id_alumno
    INNER JOIN cursos c ON c.id_curso = uc.id_curso');

    my $table = Text::Table -> new("id_usuario","id_curso","nombre y apellido usuario", "nombre curso");

    $stmt -> execute();

    while(my $row = $stmt -> fetchrow_arrayref){
        $table -> add($row -> [0], $row -> [1], $row -> [2], $row -> [3]);
    };

    print $table->rule('-', '+');
    print $table->title();
    print $table->rule('-', '+');
    print $table->body();
    print $table->rule('-', '+');
    
    $stmt -> finish();
    $db_conn -> disconnect();
};


sub fill_table {
    
    my ($table_name,$columns,$data) = @_;

    my $db_conn = db::get_db_connection();
    my $columns_len = scalar(@{$columns});


    my $params = join(",",("?") x $columns_len);

    my $statement = $db_conn -> prepare("INSERT INTO $table_name VALUES ($params)");

    eval {
        foreach my $element (@{$data}){
            my @row = ();
            foreach my $column (@{$columns}){push(@row,($element -> {$column}))};
            $statement -> execute(@row);
        };
    };

    $db_conn -> disconnect();
};


sub main{

    common::clear();

    my $users = e3::fetch_users();
    my @users_columns = ("id","nombre","apellido");

    my $courses = e3::fetch_courses();
    my @courses_columns = ("id","nombre","cupo","id_docente");


    my $enrollments = get_enrollments($users);
    my @enrollments_columns = ("course_id", "user_id");

    fill_table("usuarios", \@users_columns ,$users);
    fill_table("cursos", \@courses_columns, $courses);
    fill_table("usuarios_cursos", \@enrollments_columns, $enrollments);

    show_enrollments();
};


if($0 eq __FILE__){
    
    main();
};


1;