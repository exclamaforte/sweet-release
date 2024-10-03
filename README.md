# sweet-release
A script to reduce the friction of manually processing release notes for PyTorch.

## What it does
First, it opens the issue up in the browser and asks you to categorize it. Then, it processes the commit message and opens the final version in your editor of choice for manual edits. Finally, it saves the information to the output file in markdown format.

It will overwrite your output file with the current state after every input line is processed, so make sure to save it if you quit and resume a session.

## Usage
```shell
$ python process.py <input file> <output file> --editor <code editor name>
```

Add categories to the `classes` variable in `process.py` file.

Tip: If you open the file in github, you can see the "rendered" version of the output file without needing to install markdown.
