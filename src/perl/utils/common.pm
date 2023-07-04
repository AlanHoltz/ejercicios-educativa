package common;


use strict;
use warnings;


sub clear {
    
    $^O eq "MSWin32" ? system "cls" : system "clear"; 
};


1;
