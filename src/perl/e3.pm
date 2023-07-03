package e3;


use strict;
use warnings;
use lib 'utils';
use common;
use LWP::UserAgent ();
use JSON;
use Data::Dumper;


sub fetch {
    
    my ($url) = @_;
    my $ua = LWP::UserAgent->new;
    
    my $res = $ua -> get($url);

    my $json = $res -> decoded_content;

    my $decoded = decode_json($json);

    return $decoded;
};


sub fetch_users{

    return fetch("http://packages.educativa.com/samples/usuarios.json") -> {usuarios};
};


sub fetch_courses{

    return fetch("http://packages.educativa.com/samples/cursos.json") -> {cursos};
};


sub main {

    common::clear();

    print "USUARIOS: \n";
    print Dumper(fetch_users());

    print "CURSOS: \n";
    print Dumper(fetch_courses());
};


if($0 eq __FILE__){
    
    main();
};


1;