I started this as a hobby project to run commands or actions by commanding ;) .. 
I am finding it useful and so sharing it for the public use. Of course like life it can always be made better and hence, 
if you want to contribute please mail me at: sandeepkkothari@gmail.com

## How to INSTALL
```
pip3 install -r requirements.txt
```
Also, install **espeak**

For MaC:
```
brew install espeak
```
For linux:
Use apt or yum 

Example for Ubuntu: 
```
apt-get install espeak 
```

## How to use?
1. Just launch the launcher in your terminal:
	``` 
	python3 launcher.py
	```
2. Say **rocket**
3. Wait for prompt (Yes, Sir)
4. Say your commands like: 
	"open browser"
	"search courses for kubernetes"
5. Repeat steps 2-4 for each of your commands
6. Say "goodbye" to exit **rocket**

You can configure your own commands in **commands.yml** file

It's a simple file where you can add your own commands and customize it for your needs.

Already few commands are added for MAC OS Users:

You can say commands like:

open browser
open calendar
open mail
close browser

To see the list of already added commands use:
```
python3 launcher.py -c
```

USAGE:
```
python3 launcher.py 

```
DEBUGGING MODE: 
```
python3 launcher.py -d 
```

