#!/usr/bin/env ruby
# A regular expression that is matches only capital letters
puts ARGV[0].scan(/[A-Z]/).join

# This is a Ruby script that uses a regular expression to match all uppercase letters 
# in the first argument passed to the script. The regular expression "/[A-Z]/" matches any character in the range ‘A’ to ‘Z’.
