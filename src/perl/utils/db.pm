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


1;