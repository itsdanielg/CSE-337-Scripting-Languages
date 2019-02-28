#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 1, Part 2

sub main {

	#Change file name to different csv file
	my $file_name = 'collections.csv'; 
	open(INPUT, $file_name) or die "Cannot open $file_name";
	my $file_line = <INPUT>;	# Skip header line

	my ($id, $name, $country, $year);
	
	my $old_id;
	my $new_id;
	my $old_year;
	my $new_year;

	$file_line = <INPUT>; # First line to initialize everthing
	chomp($file_line);
	($id, $name, $country, $year) = split(',', $file_line);
	$old_id = $new_id = $id;
	$old_year = $new_year = $year;

	while ($file_line = <INPUT>) {
		chomp($file_line);
        ($id, $name, $country, $year) = split(',', $file_line);
        if ($year < $old_year) {
        	$old_id = $id;
        	$old_year = $year;
        }
        elsif ($year > $new_year) {
        	$new_id = $id;
        	$new_year = $year;
        }
	}

	print "$old_id\n";
	print "$new_id\n";
	
	close(INPUT);
	
}

main();