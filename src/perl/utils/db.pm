package db;


use strict;
use warnings;
use DBI;


sub get_db_connection {
    
    my $db_conn = DBI->connect("DBI:mysql:edu_challenge_db",'edu_challenge_user','3duc4');
    
    $db_conn || die "Error: $!";
        
    return $db_conn;
};


1;