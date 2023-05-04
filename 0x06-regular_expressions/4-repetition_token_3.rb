#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regular expression matching method
puts ARGV[0].scan(/hbt*n/).join

# This is a Ruby script that uses a regular expression to match a specific pattern in the first
# argument passed to the script. The regular expression "/hbt*n/" matches a string that starts with the character ‘h’,
# followed by the character ‘b’, then zero or more occurrences of the character ‘t’, and finally the character ‘n’. 
# The `scan` method returns an array of all occurrences of the regular expression in the input string. 
# The `join` method then concatenates the elements of the array into a single string, which is printed to the console using puts.
