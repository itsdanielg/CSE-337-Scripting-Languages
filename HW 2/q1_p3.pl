#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 1, Part 3

sub main {

	#Change file names to different csv files
	my $input_fn_one = 'collections.csv';
	my $input_fn_two = 'm1.csv';
	my $input_fn_three = 'm2.csv';
	my $output_fn = 'exhibition.csv';

	open(INPUT, $input_fn_one) or die "Cannot open $input_fn_one";
	my $file_line = <INPUT>;	# Skip header line
	my $header_line = $file_line;
	chomp $header_line;
	my @file_lines;
	my $num_lines = 0;
	while ($file_line = <INPUT>) {
		chomp($file_line);
        my @input_file_line = split(',', $file_line);
        push @file_lines, [@input_file_line];
        $num_lines++;
	}
	close(INPUT);
	
	open(INPUT, $input_fn_two) or die "Cannot open $input_fn_two";
	$file_line = <INPUT>;	# Skip header line
	while ($file_line = <INPUT>) {
		chomp($file_line);
        my @input_file_line = split(',', $file_line);
        push @file_lines, [@input_file_line];
        $num_lines++;
	}
	close(INPUT);
	
	open(INPUT, $input_fn_three) or die "Cannot open $input_fn_three";
	$file_line = <INPUT>;	# Skip header line
	while ($file_line = <INPUT>) {
		chomp($file_line);
        my @input_file_line = split(',', $file_line);
        push @file_lines, [@input_file_line];
        $num_lines++;
	}
	close(INPUT);

	for (my $i = 0; $i < $num_lines; $i++) {
		my $min_ind = $i;
		for (my $j = $i + 1; $j < $num_lines; $j++) {
			if ($file_lines[$j][0] < $file_lines[$min_ind][0]) {
				$min_ind = $j;
			}
		}
		my $temp_arr = $file_lines[$i];
		$file_lines[$i] = $file_lines[$min_ind];
		$file_lines[$min_ind] = $temp_arr;
	}

	open(INPUT, '>', $output_fn) or die "Cannot output $output_fn";
	print INPUT join(',', $header_line);
	for (my $i = 0; $i < $num_lines; $i++) {
		print INPUT "\n", join(',', @{$file_lines[$i]});
	}
	close(INPUT);
	
}

main();