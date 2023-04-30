# Lenovo Battery conservation mode on kde Plasma
So I was looking for KDE Plasma widget to control Conservation mode something like gnome extenstion [IdeaPad](https://extensions.gnome.org/extension/2992/ideapad/) but didn't find any so i made this on Qt6 and I was to lazy to learn how to make KDE Plasma widget hope someone find this and make it widget for KDE Plasma (or i will do it)

Don't worry about your different lenovo model with this, it searches for filenames containing "VPC" in the ideapad_acpi directory and uses the first one found (if any) as the new mode_file. If no files containing "VPC" are found, an error message is printed and the function returns.
# How to run  

```
pip install -r requirements.txt

python main.py
```
Tested on Manjaro KDE Plasma
