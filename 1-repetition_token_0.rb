#!/usr/bin/env ruby
# The regex /hbt{2,5}n/ matches:
# hb      : exactly the characters "hb"
# t{2,5}  : the letter "t" repeated between 2 and 5 times
# n       : exactly the character "n"
puts ARGV[0].scan(/hbt{2,5}n/).join
