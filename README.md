# Ransomware
A ransomware python script

> Original Author: Maor Sabag


The default password of the file is 'maor', you can change it in line 9 to whatever you'd like.
Be advised don't run it on your main PC!

# Dependencies

```
pip3 install -r requirements.txt
```


# Usage

On the **victim machine**, run this script. you'll see the files in the directory getting locked in a zip file
name "locked_file.zip", than changing the name to "locked_files.zip.aes".
Then an easygui window will pop telling you to enter the password inorder to decrypt the file.

```
python3 ransomware.py
```
