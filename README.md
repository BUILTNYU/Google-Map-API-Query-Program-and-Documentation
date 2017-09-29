# Google-Map-API-Query-Program-and-Documentation
This is a program for getting google map API information

# Documentation for	the	program	“GoogleMapQuery.py”:

# Xuebo	Lai

This	python	program,	created	by	Xuebo	Lai,	aims	to	provide	easy	and	quick	access	to	Google	
Maps	Distance	Matrix	API(GMDM API).	Fundamentally,	it	requests	data	from	Google	MAP	API	
according	to	users’ requirements.	It	would	ask	uses	to	input	certain	parameters	and	locations	
and	then	return	results generated	by	GMDM	API	based	on	user’s	inputs.	This	python	can	only	
run	with	internet	connected and	all	required	libraries	installed.	It’s	recommended	to	run	in	the	
environment of	python3.6.	To	add	more	parameters	or	further	customize	the	program,	please	
contact	with	the	developer.

## Python	Libraries:

For	the	program	to	run,	you	need	to	have	the	following python libraries	installed	in	your	
computer:
urllib
codecs
time
signal
To	install	those	libraries,	you	can	use	“pip	install	<library’s	name>”.
More	information	about	how	to	install	additional	python	program	can	be	found	in	the	following	
URL:
https://packaging.python.org/tutorials/installing-packages/
Please	notice	that	missing	one	or	more	libraries	might	lead	to	crush	of	the	program.

## Program	Instruction:

# Input:

After	the	program	is initialized,	it	would	pop	out	some	prompt	for	you to	enter	information.	
Follow	the	prompt	to	provide	all	necessary	information. You	need	to	provide	exact	answer	as	
requested	by	prompts. The	standard	format for	each answer	is	provided	at	the	end	of	the	
prompts.	Questions	are	listed	below:

## Q1,	For origins/destinations	addresses (required):	Please	indicate	whether	

## you	would	like	to	use	file	that	contains	all	location's	name	or	manually	enter	

## address(file/manual)

## Program	Expected	Answer(PEA):	manual/file

Explanation:	For	origins/destinations addresses,	you	have	to	choose	whether you	want	to	
manually	enter	all	the	addresses in	the	program	or	have	all	the	addresses stored	in	a	file	and	
then	let	the	program	to	read	the	file.


### Q2,	For	origins	(required):	Please	indicate	whether	you	would	like	to	use	

### coordinates	or	address(cor/address)

## PEA:	cor/address

Explanation:	Here	you	need	to	tell	the	program	whether	you	want	to	use	the	coordinate	system
or	addresses	as	input. If	you	choose	to	use	coordinates,	please	notice	that:	Google	uses	WGS	84	
Web	Mercator	as	its	coordinate	system.

## Q3,	situation	one,	If	you	choose	to	enter	addresses manually:

For	manually	entering the	addresses	(for	both	coordinates	and	literal	addresses),	you	need	to	
provide	the	addresses	in	the	following	format (without	the	quotation	marks):

## PEA:

Coordinates	Example: “47.6,75.3|48.5, 89.7”
Addresses	Example:	“257	gold	street	ny|2	gold	street	ny”

Explanation:
Please	notice	that	you	need	to	separate	each	of	the	address	by	“|” and	try	to	avoid	to	use	any	
other	punctuations within	the	address.	(Present	of	other	punctuations	might	lead	to	format	
error	later	in	the program.)
In	coordinates’ example,	47.6,75.3	is	a	set	of	coordinate	and	48.6,89.7	is	another	set	of	
coordinate.
In	addresses’ example, “257	gold	street	ny” is	one	address,	“2	gold	street	ny” is	another.

## Q3,	situation	two,	If	you	choose	to	enter	addresses	into	the	program	

## through	file:

For	using	file	to	pass	addresses/coordinates,	you	would	need	to	provide	the	path	of	the	files,	
either	absolute	or	relative.	

## PEA:

Please	refer	the	pictures	below:
For	addresses,	you	need	to	provide	one	address	at	a	line (figure	1), the	format	of	the	file	can	
any	types.	(txt,	csv...).	Example	file,	test.csv, can	be	found	in	this	directory.


For	coordinates,	it’s	pretty	much	the	same	except	that	you	put	one	coordinate a	line, the	
format	of	the	file	can	any	types.	(txt,	csv...)

## Q4,	What	kind	of	units	would	you	like	to	use?	(imperial/metric)

## PEA: imperial/metric

Explanation:	the	google	maps	distance	matrix	api	can	return	distance	in	two	system	of	units.	If	
you	choose	imperial,	it	would	return distance	in	units	of	miles	and	feet.	If	you	choose	metric,	it	
would	return	distance	in	kilometers	and	meters.	

```
Figure 	1 :
Addresses	format	example
```
```
Figure 	2 :
Coordinates format	example
```

## Q5,	Please	enter	your	departure	time	in	second	since	1970	(unix	time)	

## or	you	can	enter	'now'	to	indicate	you	want	real	time	information	(An	

## integer/now)

## PEA:	An	integer(the	future	time	in	second	since	1970,1,1)/now(real	

## time	data)

Explanation: you	can	choose	to	obtain	a	future	prediction	result	or	real	time	data,	but	do	note	
that	the	time	can’t	be	in	the	past.

## Q6,	Please	enter	the	traffic	mode	that	you	would	like	to	use	to	get	from	

## origins	to	destination(driving/walking/bicycling/transit)

## PEA: driving/walking/bicycling/transit

Explanation:
The	API	let	you	to	choose	your	desired travel	mode	from	origins	to	destination,	you	can	from	
four	different	ways	(driving/walking/riding	a	bike/	public	transit).	Note	that	each	choice	will	
lead	to	significantly different	result.	(Unless	you	are	in	Manhattan)

## Q7, Please	enter	your	google	map	api	key	to	continue:

## PEA:	a	Google	Map	API	key

Explanation:
Google	Map	API	keys	are	required	to	run	the	program.	Each	google	map	api	key	can	process	at	
least	few	thousand	queries. I	managed	to	obtain	four	keys.	They	should be	sufficient	for	most	of	
the	situations. If	not,	please	proceed	to	
https://developers.google.com/maps/documentation/javascript/get-api-key for	more	keys,	or	
contact	Xuebo	Lai	at	xl1638@nyu.edu for	more.
(when	entering	these	keys,	do	not	include	the	word	“key” or	“=” sign,	do	not	leave	any	space	
before	or	after	the	key.)
key	=	AIzaSyCrmf67meDZnuLbM3AfbZPznIWRxB-MmYE
key	=	AIzaSyDyZhD_n3gX8tMOOj4_Mk6kZ1eJ8MURgv
key	=	AIzaSyDV-aAQfBxSi4Emh0j6UWaqf-tbBrqhSIs
key	=	AIzaSyD4jRc75REFvITM-gXKHjFcqEp70oOiygM

## Q8, Do	you	want	to	randomly	pick	up	n	address	from	origins	and	

## destinations	to	generate	matrix?(yes/no)

## PEA:	yes/no


Explanation:
You	can	choose	whether	to	randomly	pick	up	n	addresses	from	origins and	destinations	to	
generate	an	OD	matrix.	If	you	choose	yes,	later	you	need	to	enter	how	many	addresses	you	
would	like	to	choose; if	no, the	program	will	generate	an	OD	matrix	of	all	origins	to	
destinations.

## Q8, Please	name	the	output	file

## PEA:	an	name/path	of	the	output	file.	

Explanation:
The	result	will	then	be	output	to	the	output	file	specified.

# Output:

Explanation:
Here’s	an	example of	the	output	file.	The	origins	are	listed	sequentially from	the	top	in	the	
leftmost column.	The	Destination	addresses	are	listed	sequentially from	left	to	right	in	the	first	
roll.	The	number	is	the	time	in	second	from	origin	(left) to	destination	(top).

## Functions:

It’s	recommended	to	leave	the	functions	alone	so	that	you	wouldn’t	mess	up	with	the	whole	
program.	

Documentations	of	the	all	functions:
Read_file:
Input:	The	program	takes	in	an	absolute/relative	path	of	a	file	and	the	mode(reading(r),	
writing(w),	appending(a))
Output:	A	reference	to	the	input	file.
Function:	read	in	a	file.

Handler:
Input:	signal
Function:	sometimes	if	the	python	program	runs	for	too	long,	the system	might	interrupt	it.	
This	function is	created	to	ignore	the	system	interruption.

processAddress:
input:	a	bunch	of	addresses
output:	the	cleaned	usable	addresses.


This	function	is	used	to	clean	up	the	addresses	so	that	they	can	be	used	by	the	google	map	API.

google_map_distance_matrix_api:
input:	parameters	relevant	to	the	request	of	google	map	api
output:	a sorted json	dictionary	that	contains	all	the	data	from	google maps	api
This	function is	created	for	formatting	input	for	google	map	api	and	parse	the	output	from	the	
api	to	a	dictionary.

OutputFile:
Input: output	file’s	name,	information	about	google	map	api’s	request
Output:	an	file that	contains	sorted	output	from	google maps	api
This	function	calls	on	previous	functions	to	make	a	request	to	google	map	api,	obtain	the	
output,	parse	the	output	to	a	file.

Main:
The	main	function in	this	program	is	mainly	used	for	I/O. It	coordinates	with	all	the	functions	to	
generate	desired	output.


