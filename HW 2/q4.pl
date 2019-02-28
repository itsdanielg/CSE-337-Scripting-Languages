#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 4

use Cwd qw(abs_path);

sub main {

	my $directory = "features";
    unless(-e $directory or mkdir $directory) {
    	die "Unable to create $directory\n";
    }

    print qq(Files have been created!\n);
	for (my $i = 0; $i < 10; $i++) {
		my $new_file_name = $directory . "/$i-" . $ARGV[0];
		open(OUTPUT, '>', $new_file_name) or die "Cannot open $new_file_name";
		close(OUTPUT);
		print abs_path($directory . "/$i-" . $ARGV[0]), "\n";
	}
    
	my $file_name = $ARGV[0];
	open(INPUT, $file_name) or die "Cannot open $file_name";
	my @line_words;
	my $feature_num;
	while (my $input_line = <INPUT>) {
		chomp $input_line;
		@line_words = split(' ', $input_line);
		$feature_num = substr $line_words[-1], -1;
		my $new_file_name = $directory . "/$feature_num-" . $ARGV[0];
		open(OUTPUT, '>>', $new_file_name) or die "Cannot open $new_file_name";
		print OUTPUT $input_line . "\n";
		close(OUTPUT);
	}
	close(INPUT);

}

main();