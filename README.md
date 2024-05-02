# Echo Sender
Sometimes you want to write files/programs to an embedded device that does not have any file transfer utilities; these programs allow you to write files using the 'echo' command. It will work as long as the embedded device supports the '-n' and '-e' options in echo.

I originally wrote `echo_sender.py` to solve this problem, but after I learned about tmux scripting I decided I liked using tmux scripts more. To use `echo_sender.py`, see the example below. To use `tmux_echo_sender.py`, run `python3 tmux_echo_sender.py -h`.

# echo_sender.py example
In this example, `/dev/ttyUSB0` is a device used to interface with a UART shell on a router. Here `echo_sender.py` is shown being using to send the file `foo` containing "hello world" to the router.
![how to use](https://github.com/tristan-white/echo_sender/blob/main/howToUse.gif)
