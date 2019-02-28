#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 3, Part 1

sub main {

	my $file_name = $ARGV[0];
	open(INPUT, $file_name) or die "Cannot open $file_name";
	my @feature_counter = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
	my @line_words;
	my $feature_num;
	while (my $input_line = <INPUT>) {
		chomp $input_line;
		@line_words = split(' ', $input_line);
		$feature_num = substr $line_words[-1], -1;
		$feature_counter[$feature_num] += scalar @line_words;
	}
	close(INPUT);

	for (@feature_counter) {
		print $_ . "\n";
	}
	
}

main();