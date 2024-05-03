import argparse

parser = argparse.ArgumentParser(
    description="""Creates a tmux script that can be used to write files
    to embedded devices that do not have file transfer utilities. This is
    done using a tmux script that automates typing a series of 'echo' 
    commands to echo the bytes of a file to a location on the embedded 
    device.""",
    epilog="""To run the tmux script, press Ctrl-B followed by a ':' to
    tell tmux you are going to enter a command. Type the command 'source-file
    /full/path/to/tmux_script'
    """,
)
parser.add_argument(
    '-i', '--input',
    required=True,
    type=str,
    help="The input file that will be written to the embedded device."
)
parser.add_argument(
    '-r', '--remote-dest',
    required=True,
    type=str,
    help="""The location to which the tmux script will write the file.""",
)
parser.add_argument(
    '-c', '--chunk-size',
    required=True,
    type=int,
    help="""The number of bytes send with each echo command.""",
)
parser.add_argument(
    '-o', '--output',
    required=False,
    default="tmux_script",
    type=str,
    help="""Optional; dicates the name of the file output from this program."""
)

args = parser.parse_args()

with open(args.input, "rb") as infile:
    with open(args.output, "w") as outfile:
        data = infile.read(args.chunk_size)
        while (data):
            echo_bytes = ""
            for octet in data:
                echo_bytes += f"\\x{octet:02x}"
            shell_cmd = f"echo -ne \"{echo_bytes}\" >> {args.remote_dest}"
            tmux_cmd = f"send-keys '{shell_cmd}'\nsend-keys Enter\n"
            outfile.write(tmux_cmd)
            data = infile.read(args.chunk_size)
