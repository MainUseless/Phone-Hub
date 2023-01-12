# Phone-Hub
## Info:
This project allows the user to control his PC's in a local network through any platform/app that allows sending messages to that phone. 
provided that there exists a spare android phone that is connected to the same local network and the PC's are running the provided TCP server script.


## pre-requisites:
- A spare android phone that is always connected to the same network that will always be left on and in the same place.
- [send/expect](https://play.google.com/store/apps/details?id=com.asif.plugin.sendexpect&hl=en&gl=US) ,[macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=en&gl=US) ,[macrodroid helper](https://www.macrodroidforum.com/index.php?threads/macrodroid-helper-apk.1/) and [WOL](https://play.google.com/store/apps/details?id=co.uk.mrwebb.wakeonlan&hl=en&gl=US) installed.
- A spare private Discord account that is signed in on the phone / or any other prefered way of sending a message to the phone.
- PC with static local ip, WOL enabled and python.

## Setup:
1. Import [control_macro](https://github.com/MainUseless/Phone-Controlled-Shutdown/blob/main/Remote_Control.macro) to macrodroid.
2. Make sure battery optimaization is turned off for macrodroid and macrodroid helper.
3. Add your PC to WOL app.
4. In send/expect app add profiles with the PC static local ip and port 12000 with one of the available messages to trigger an action on your PC.
5. Open the imported macro in macrodroid and match each profile from send/expect with a command that will be sent to your phone.
6. Add configure WOL action with your PC profile created in step 3.
7. Configure the first if condition to match your sender user name (can be removed if you don't want it).
8. Open run, type shell:startup, add [shut.pyw](https://github.com/MainUseless/Phone-Controlled-Shutdown/blob/main/shut.pyw) or a shortcut of it in startup folder.
9. Make sure to allow python through your firewall.
    - if you get An attempt was made to access a socket in a way forbidden by its access permissions error.
    - Open cmd as admin and run:
    ```
    net stop hns
    net start hns
    ```
  

## Supported actions:
- WOL : (/wake {pc name})
  - TCP message : *
- Shutdown : (/kill {pc name})
  - TCP message : shutdown
- Hibernate : (/sleep {pc name})
  - TCP message : hibernate
- pc name is user generated and isn't correlated to your actual PC name.
