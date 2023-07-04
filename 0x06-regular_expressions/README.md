# 0x06. Regular expression
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## 0-simply_match_school.rb
The regular expression must match School
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 1-repetition_token_0.rb, 2-repetition_token_1.rb, 3-repetition_token_2.rb
Find the regular expression that will match the above cases

## 4-repetition_token_3.rb
Find the regular expression that will match the above cases
Your regex should not contain square brackets

## 5-beginning_and_end.rb
The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between

## 6-phone_number.rb
This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

Requirement:
The regular expression must match a 10 digit phone number

## 7-OMG_WHY_ARE_YOU_SHOUTING.rb
The regular expression must be only matching: capital letters
