#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 2, Part 1

sub main {

	#Change file names to different files
	my $file_dir = "Q2sample/t1/";
	my $input_file_name = "q2.in";
	my $output_file_name = "q2p1.out";
	
	my $str1 = <STDIN>;
	my $str2 = <STDIN>;
	chomp $str1;
	chomp $str2;

	open(INPUT, $file_dir . $input_file_name) or die "Cannot open $input_file_name";
	my @input_lines = <INPUT>;
	my @output_lines;
	for (@input_lines) {
		$_ =~ s/\b$str1\b/$str2/g;
		push(@output_lines, $_);
	}
	close(INPUT);

	open(INPUT, '>', $file_dir . $output_file_name) or die "Cannot output $output_file_name";
	print INPUT @output_lines;
	close(INPUT);
	
}

main();