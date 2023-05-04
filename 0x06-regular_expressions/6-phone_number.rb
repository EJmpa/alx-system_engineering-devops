#!/usr/bin/env ruby
# A regular expression that is matches 10 digit phone number
puts ARGV[0].scan(/^\d{10,10}$/).join

# This is a Ruby script that uses a regular expression to match a 10-digit phone number
# in the first argument passed to the script. The regular expression "/^\d{10,10}$/"
# matches a string that starts and ends with exactly 10 digits (represented by \d)
