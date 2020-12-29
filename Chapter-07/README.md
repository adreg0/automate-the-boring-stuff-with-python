1) re.compile()
2) .
3) returns Match result
4) By using group() or group (0)
5) Group 0 returns the entire match, Group 1 covers the first parenthesis and Group 2 covers the second paranthesis.
6) By using backslash as a prefix (\.)
7) If it is divided into groups, list of tuples of strings is formed if not list of strings will be returned.
8) | is called a pipe. It is used to match one of the expressions. 
9) Used to specify non greedy matching.
10) + matches one or more, * is matches zero or more.
11) {3} matches three instances. {3,5} matches in the interval three and five.
12) \d matches a digit, \w matches a word, \s matches a space
13) \D matches match a character except digit, \W matches a character except word, \S matches except space.
14) .* - Greedy match, .*? - non greedy match.
15) [a-z0-9]
16) re.IGNORE makes a regular expression case-insensitive.
17) . matches everything except new line. re.DOTALL matches everything includeing new line.
18) .
19) can add comments and spaces by using re.VERBOSE as the second argument to re.compile()
