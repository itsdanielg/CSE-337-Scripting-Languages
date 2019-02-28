#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 2, Part 2

sub main {

	#Change file names to different files
	my $file_dir = "Q2sample/t1/";
	my $input_file_name = "q2.in";
	my $output_file_name = "q2p2.out";

	my $input_num = <STDIN>;
	chomp $input_num;

	open(INPUT, $file_dir . $input_file_name) or die "Cannot open $input_file_name";
	my @input_lines = <INPUT>;
	my @output_lines;
	my @removed_lines;
	for (@input_lines) {
		if (scalar(() = $_ =~ /\S+/g) == $input_num) {
			push(@removed_lines, $_);
		}
		else {
			push(@output_lines, $_);
		}
	}
	if (!@removed_lines) {
		undef(@output_lines);
		push(@output_lines, "Oooh Nooo!\n");
	}
	close(INPUT);

	open(INPUT, '>', $file_dir . $output_file_name) or die "Cannot output $output_file_name";
	print INPUT @output_lines;
	close(INPUT);
	
}

main();