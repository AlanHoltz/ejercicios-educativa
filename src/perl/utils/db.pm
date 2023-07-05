package db;


use strict;
use warnings;
use lib ".";
use DBI;
use common;


sub get_db_connection {

    my $env_values = common::get_env_values();
    my $db_user = $env_values -> {DB_USER};
    my $db_password = $env_values -> {DB_PASSWORD};
    
    my $db_conn = DBI->connect("DBI:mysql:edu_challenge_db",$db_user,$db_password, {
    PrintError => 0, 
    RaiseError => 1
});
    
    $db_conn || die "Error: $!";
        
    return $db_conn;
};


sub fetch_one {
    my ($query,$params) = @_;
    my $db_conn = get_db_connection();
    my $stmt = $db_conn -> prepare($query);
    $stmt -> execute(@{$params});

    my $row = $stmt -> fetchrow_arrayref;

    $stmt -> finish();
    $db_conn -> disconnect();

    return $row;
};


sub execute {
    my ($query,$params) = @_;
    my $db_conn = get_db_connection();
    my $stmt = $db_conn -> prepare($query);

    $stmt -> execute(@{$params});
    
    $stmt -> finish();
    $db_conn -> disconnect();
};


1;