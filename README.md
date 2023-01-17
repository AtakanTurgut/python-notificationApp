## Make notification app using python.
For make a notification app, Plyer module must be installed first.
- Download the latest [Python installer](https://www.python.org/downloads/) for your OS.
I used [this website](https://www.alphr.com/pip-is-not-recognized-as-an-internal-or-external-command/#:~:text=Reinstall%20Python%20to%20Fix%20'Pip,components%20to%20fix%20the%20problem.) for help, you can have a look if you want.
-  Users who want to use pip for installing the Plyer module on Windows in the command prompt have to use the command:
```
pip install plyer
```
The notification message will disappear after 10 seconds. ' timeout = 10  #seconds '
The notification message will be repeated after 15 seconds. ' time.sleep(15) #seconds '

![](/notificationBox.png)