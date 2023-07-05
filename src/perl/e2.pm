package e2;


use strict;
use warnings;
use lib 'utils';
use common;


sub format_names {

    my @formatted_names = ();

    foreach my $name (@_){
        my @splitted_full_name = split(" ",$name);
        my $surname = @splitted_full_name[-1];
        pop @splitted_full_name;
        my $name = join(" ", @splitted_full_name);
        push(@formatted_names, ("$surname, $name"))  
    };

    return @formatted_names;
};


sub generate_hash {

    my $ordered_names_len = scalar(@_);
    my %ordered_names = ();

    for(my $i = 1; $i < $ordered_names_len + 1; $i = $i + 1){
        $ordered_names{$i} = @_[$i-1];
    };

    return %ordered_names;
};


sub sort_array {

    my @names = @_;
    
    @names = format_names @names;
    
    @names = sort @names;

    my %names_hash = generate_hash @names;

    return %names_hash;
};


sub main {

    common::clear();
    
    my @lista_nombres = ("Jacinta Flores", "Juan Carlos Feletti", "Pedro Lugones", "Ana Maria Galindez");
    
    print sort_array(@lista_nombres);
};


if($0 eq __FILE__){
    
    main();
};


1;