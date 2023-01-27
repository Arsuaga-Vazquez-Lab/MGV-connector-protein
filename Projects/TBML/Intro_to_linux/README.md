# Intro to Unix

- display user manual of command:
	`man <command_name>` 
## Navigating the Directory:

- open a folder / directory:
	`cd <folder_name>`

- to move up one directory:
	`cd ..`
	
- navigate to root / home:
	`cd ~`
	`cd /`

- print path to your current working directory:
	`pwd`

- list files in current directory:
	`ls`
	- to list in long form:
		`ls -l`
	- to list all content:
		`ls -a`
## Files:

	- run a <filename> in the same folder where you're located:
		`.\ <filename>`
		
	- run a shell file:
		`sh <file.sh>`
		
	- run a python file:
		`python3 <file.py>`
		- for any other programming language, simply replace python3 and .py with the appropriate language
		
	- display a file:
		`cat <filename>`
		
	- run a file from a parent folder:
		`..\<filename>`
		
	- to see more about a file:
		`more <filename>`

	- to find a file
		`find <directory> -name <filename>`	
			- wildcard: `.`
			`find . -name <filename>`	
			- finds file called <filename> in current and sub-directories.
	
	- to find a directory:
		`find ./ -type d -name <directory>`
	
	- to move or rename a file:
		- move:
			`mv <filename> <new_directory>`
		- rename:
			`mv <filename> <new_name>`
	
	- copy a file:
		`cp <filename> <directory>`
		
	- create files:
		`touch <filename>`
	
	- create directory:
		`mkdir <directory>`
		
	- remove files / directories
		- remove directory:
			`rmdir <directory>`
		
			- to remove directory along with the files inside:
				`rmdir -r`
		
		- remove file:
			`rm -i <filename>`
			- i : will ask for confirmation before removing file
			
	- to find things in files:
		`grep 'word' <filename>'
		flags:
			-i : case insensitive
			-c : display the total number of times the word appears
	
	- To decompress .gz files, use:
			`gzip -d <filename.gz>`
			
		- Unzip and open gz file using:
			`gunzip <filename.gz>`
			
		- For .tar.gz/.tgz file try the tar command:
			`tar -xvf <filename.tar.gz>`
			
		- To unzip files:
			`unzip <filename.zip>`
	- sort file:
		`sort <filename>`	
		
	- Piping:
		|
		- output of one function into another
		ex: sort file.txt | uniq 
			- sort a file and print unique values
	
	- change file permissions:
		`chmod +rwx <filename>`
		- r = read
		- w = write
		- x = execute
		- u = users
		- g = group
		- o =  others,
		- use - to remove permission
		- can create different combinations of permissions
		- ex: `chmod g+w` : group has write permission
		
		
## Shortcuts:
	- Ctrl+L:
		clears screen
	- Ctrl+S:
		pauses command output
	- Ctrl+Q:
		resumes output
	- Ctrl+A / Home:
		moves cursor to start of line
	- Ctrl+E / End:
		moves cursor to end of line
	- Ctrl+Z:
		suspends program
	- Ctrl+C:
		interrupt program	
	- Tab:
		autocomplete