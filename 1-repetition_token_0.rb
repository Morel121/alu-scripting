#!/usr/bin/env ruby
# The regex /hbt{2,5}n/ matches hb followed by 2 to 5 t's and then n
puts ARGV[0].scan(/hbt{2,5}n/).join
