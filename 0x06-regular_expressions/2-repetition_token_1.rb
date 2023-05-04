#!/usr/bin/env ruby
# A regular expression that is matches a given pattern
puts ARGV[0].scan(/hb?tn/).join

# This is a Ruby script that uses a regular expression to match a specific pattern in the first argument passed to the script.
# The regular expression /hb?tn/ matches a string that starts with the character ‘h’, followed by zero or one occurrence of
# the character ‘b’, then the character ‘t’, and finally the character ‘n’. The `scan` method returns an array of all
# occurrences of the regular expression in the input string. The `join` method then concatenates the elements of the array
# into a single string, which is printed to the console using puts.
