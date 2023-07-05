package common;


use strict;
use warnings;
use File::Spec;


sub clear {
    
    $^O eq "MSWin32" ? system "cls" : system "clear"; 
};


sub get_env_values {

    my $root_path = File::Spec -> rel2abs("../..");
    my $env_path = File::Spec -> catfile($root_path,".env");
    
    open(my $env_file, "<", $env_path) || die "ERROR ABRIENDO .ENV: $!";

    my $env_values = ();
    
    while(my $line = <$env_file>){
        
        my $key;
        my $value;
        
        if($line =~ /^\s*([^=\s]+)/){$key = $1};
        if($line =~ /=\s*(.*)/){$value = $1};
        
        $env_values -> {$key} = $value;
    };

    return $env_values;
};


1;
