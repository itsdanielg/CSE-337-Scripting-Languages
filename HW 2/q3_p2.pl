#!/usr/bin/perl
use strict;
use warnings;

# Daniel Garcia
# SBU ID: 111157499
# Homework 2

# Question 3, Part 2

sub main {

	my %revenue_hash = (
		jan => 4840,
		feb => 4340,
		mar => 3900,
		apr => 4330,
		may => 3090,
		jun => 3660,
		jul => 3520,
		aug => 3280,
		sep => 4130,
		oct => 3690,
		nov => 4260,
		dec => 4800
	);
	my @months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 
		'aug', 'sep', 'oct', 'nov', 'dec');
	my $initial_month;
	my $final_month;
	print qq(Months can be selected using the three initials letters.\n);
	print qq(Enter the initial month: );
	while (1) {
		$initial_month = lc(<STDIN>);
		chomp($initial_month);
		if (exists $revenue_hash{$initial_month}) {
			last;
		}
		else {
			print qq(Please enter only the three initials letters of a valid month.\n);
			print qq(Re-enter the initial month: );
		}
	} 
	my ($initial_index) = grep { $months[$_] eq $initial_month } (0 .. @months-1);
	my $final_index;
	print qq(Enter the final month: );
	while (1) {
		$final_month = lc(<STDIN>);
		chomp($final_month);
		if (exists $revenue_hash{$final_month}) {
			($final_index) = grep { $months[$_] eq $final_month } (0 .. @months-1);
			if ($final_index >= $initial_index) {
				last;
			}
			else {
				print qq(Please enter only the three initials letters of a valid month.\n);
				print qq(Re-enter the final month: );
			}
		}
		else {
			print qq(Please enter only the three initials letters of a valid month.\n);
			print qq(Re-enter the final month: );
		}
	}

	my $cumulative_revenue = 0;
	for (my $i = $initial_index; $i <= $final_index; $i++) {
		$cumulative_revenue += $revenue_hash{$months[$i]};
	}
	print qq(The cumulative revenue is: $cumulative_revenue);
	
}

main();