package e1;


use strict;
use warnings;
use lib 'utils';
use common;


sub main {

    common::clear();
    
    my $string =
    'Jacinta_Flores$Juan_Carlos_Feletti$Pedro_Lugones$Ana_Maria_Galindez$Juana_Bermudez$Rafael_Ernesto_Brahms
$Beatriz_Valente$Ulma_Fabiana_Goya$Martina_Nicolesi$Betania_Miraflores$Fermin_Olivetti$Ana_Luz_Narosky$Gr
aciana_Arruabarrena$Joel_Perez$Valentina_Feller$Hector_Tadeo_Siemens$Natalia_Martinevsky$Ernesto_Nicolini
$Pia_Paez$Fermin_Obdulio_Camilo_Galindez$Delfina_Beirut$Walter_Mantinoli$Celina_Celia_Samid$Ulises_Malo$J
uana_Varela$Melquiades_Jose_Li$Radamel_Servini$Filemon_Salsatti$Celeste_Faim$Valerio_Martin_Rosseti$Jerem
ias_Farabutti$Veronica_Nefertiti$Ana_Delia_Pereyra$Hermenilda_Carla_Rutini$Valerio_Tunuyan$Silvia_Solano$
Beatriz_Bevacqua$Manuel_Martinez$Berto_Carlos_Kigali$Juan_Manuel_Miraflores$Nicolas_Kligorsky$Maria_Laura
_Berotti';

    $string =~ s/\s+//g;

    $string =~ s/_/ /g;
    
    $string =~ s/\$/ - /g;
    
    my @students = split(" - ", $string);

    foreach my $student (@students){
        print "$student\n\n";
    };
};


if($0 eq __FILE__){
    
    main();
};


1;



