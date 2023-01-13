{"command":"/wake"}

# Phone-Hub

## Info:

This project allows the user to control his PC's in a local network through any platform/app that allows sending messages to that phone.
provided that there exists a spare android phone that is connected to the same local network and the PC's are running the provided http server script.

## pre-requisites:

- A spare android phone that is always connected to the same network that will always be left on and in the same place.
- Basic knowledge in macrodroid.
- [macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=en&gl=US) ,[macrodroid helper](https://www.macrodroidforum.com/index.php?threads/macrodroid-helper-apk.1/), [ntfy](https://ntfy.sh/), [HTTP Shortcuts](https://http-shortcuts.rmy.ch/) and [WOL](https://play.google.com/store/apps/details?id=co.uk.mrwebb.wakeonlan&hl=en&gl=US) installed.
- PC with static local ip, WOL enabled, python and notify-py installed.

## Setup (Windows):

1. Add your PC to WOL app.
2. Subscribe to a ntfy topic with a unique/hard to guess topic name and enable instant delivery.
3. Make sure battery optimaization is turned off for macrodroid and macrodroid helper.
4. Import [control_macro](https://github.com/MainUseless/Phone-Controlled-Shutdown/blob/main/Remote_Control.macro) to macrodroid.
5. Configure the first if condition to match notification name (can be removed if you don't want it).
6. Replace empty action in (/wake) if-else with configured WOL action that matches target PC .
7. Open the imported macro ,edit each http action with the static local ip of the target pc and with the propper json body.
8. Open run, type shell:startup, add [control.pyw](https://github.com/MainUseless/Phone-Controlled-Shutdown/blob/main/control.pyw) or a shortcut of it in startup folder.
9. On Main phone, open HTTP Shortcuts app:

   * Add all the desired actions that will be triggered using the link thats provided from ntfy and Post as a method.
   * Request body set to text with the command as its value.
   * Tone Trigger & Execution settings to your liking.
10. (Optional) Install ntfy on main phone , subscribe to a topic and let macrodroid send a confirmation message that it did activate.
11. Make sure to allow python through your firewall.

    - if you get An attempt was made to access a socket in a way forbidden by its access permissions error.
    - Open cmd as admin and run:

    ```
    net stop hns
    net start hns
    ```

## Supported actions:

- WOL : (/wake {target name})
  - json payload : *
- Shutdown : (/kill {target name})
  - json payload : { "command":"/kill" }
- Hibernate : (/sleep {target name})
  - json payload : { "command":"/sleep" }
- target name is user generated and isn't correlated anything, Just used to differentiate them.
