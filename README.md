# Rar password helper
Use this tool if you lost your rar password but know some keywords you may have used when choosing that pwd.

## Setup
You need to have unrar installed on your linux machine.
Create a file, e.g., words.txt, and put the first line containing how many combinations of words you want for each password. Every other line should be a single word to be used for password combinations.

```bash
python3 pass_gen.py < words.txt > dict.txt
# Edit the first line of dict.txt so it contains the .rar file you want to crack. Then, execute:
python3 pass_test.py < dict.txt
```
And pray.

