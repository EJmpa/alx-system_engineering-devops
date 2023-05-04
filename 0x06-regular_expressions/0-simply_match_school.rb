#!/usr/bin/env ruby
# coding: utf-8
# Ruby script that accepts one argument and pass it to a regular expression matching method
puts ARGV[0].scan(/School/).join

# This is a Ruby script that uses a regular expression to match the word ‘School’ in the first
# argument passed to the script. The `scan` method returns an array of all occurrences of the regular
# expression in the input string. The `join` method then concatenates the elements of the array into
# a single string, which is printed to the console using `puts`.
