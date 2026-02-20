

## what does the program do: 
when executed, the program takes a filepath as an argument and outputs the sha256 hash of a given file. This is useful so that if you suspect that there may be malicious activity or malware in a given file, you can output its hash and check it against popular databases such as VirusTotal. 

## How to run and necessary dependancies:
1) you just need python installed, no other dependancies. 
2) python3 block2.py
3) it will prompt you for a filepath, you can offer an absolute path or relative to current directory, and it will
output the sha256 digest of that file. 

## Limitations:
This tool is for educational use only. 
this tool doesn't normalize filepaths so you must be considerate of how you articulate your filepath. 

## Ethical considerations and responsible use: 
Someone could absolutely modify this in some sense for unethical purposes. for example, someone could take the output and transform the sha digest of a given file, and in doing so, conceal any malicious properties the file might have. In that sense, it could give users a false sense of security. That is why it is important that we as programmers endeavor to build trust and positive relationships with our users, so that they can know we are doing what we say we are doing (and not outputting the wrong hash) and we can trust other programmers when we inevitably rely on other programmers for dependancies. 