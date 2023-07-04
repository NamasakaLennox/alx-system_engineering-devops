#!/usr/bin/env ruby
puts ARGV[0].scan(/^[A-Z].*from:(\+?\w*)?.*to:(\+?\w*)?.*flags:(-?\d:-?\d:-?\d:-?\d:-?\d)?.*/).join(',')
