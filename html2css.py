#!/c/Users/vadim/AppData/Local/Programs/Python/Python35/python

import fileinput

pre = False

for line in fileinput.input():
	if line.find('<pre') > -1:
		pre = True
		first = True
		continue
	if line.find('</pre>') > -1:
		break
	if not pre:
		continue
	line = line.rstrip()
	# CSS Stats quirk: the very first line of each CSS file has extra spaces on the left
	if first:
		line = line.lstrip()
		first = not first
	while True:
		i = line.find('<span class="hljs')
		if i < 0:
			break
		line = line[:i] + line[line.index('>', i)+1:]
	print(line.replace('</span>', '').replace('&lt;','<').replace('&gt;','>'))
