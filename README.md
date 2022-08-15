# lshx
*nix ls command reimplementation

## Environment
Project was developed in Python 3.9.

Project uses `poetry` python package manager. For ease of use, a corresponding `requirements.txt file is provided

### Install dependencies (poetry)
Run the following commands (assuming bash shell). For aliasing a command using other shells, please refer to respective 
shell documentation. 
```
poetry install
```

### Create a shell alias for **lshx** command
```
alias lshx='poetry run python lshx.py'
```

## Usage

Use `lshx --help` to get usage information

To display content of current directory, use `lshx`

To manually select targets (files/directories/etc.) to display, use `lshx file1.txt file2.txt file3.jpg`

## Development

There additional development tools available from `make` utility:
1. `make test` - runs test suite using pytest runner
2. `make coverage` - runs test suite and reports on test overage
3. `make lint` - runs type checks and linters