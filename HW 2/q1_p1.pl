#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 1, Part 1

sub main {

	#Change file name to different csv file
	my $file_name = 'collections.csv'; 
	open(INPUT, $file_name) or die "Cannot open $file_name";
	my $file_line = <INPUT>;	# Skip header line
	
	my $country_name = <STDIN>;
	chomp $country_name;

	my $country_counter = 0;
	my $expl_str = "";
	while ($file_line = <INPUT>) {
		chomp($file_line);
        my ($id, $name, $country, $year) = split(',', $file_line);
        if ("$country" eq "$country_name") {
        	$expl_str .= $file_line . "\n";
        	$country_counter++;
        }
	}
	print "$country_counter\n";

	close(INPUT);
	
}

main();