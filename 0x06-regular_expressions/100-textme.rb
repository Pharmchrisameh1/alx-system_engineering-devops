#!/usr/bin/env ruby
print ARGV[0].scan(/(?<=from:)(?<=from:)\+?\w*/).join
print ","
print ARGV[0].scan(/(?<=to:)\+?\w*/).join
print ","
print ARGV[0].scan(/(?<=flags:)(?:-?\d:?)*/).join
