
# HTML Optimiser

A Python package for optimizing HTML, JS, CSS, and JSON files in a directory.

To achieve this, the project copies the selected folder to a new "compressed" folder inside the selected directory and applies optimizations to supported file types.

It automatically detects `.gitignore` files and skips ignored files during copying.

Currently supported file types:
- `.html`
- `.js`
- `.css`
- `.json`

## Usage

Run `main.py` to launch the folder selection and optimization process.

## Structure

- `html_optimiser/` — main package code
- `main.py` — entry point
- `setup.py` — package setup
- `README.md` — documentation


## Extending optimisation_def.py for New File Types


### How to Add Support for a New File Extension

1. **Open** `html_optimiser/optimisation_def.py`.

2. **Create a new function** for your file type (e.g., `optimize_xml`).
   - The function should take a file path as its only argument.
   - It should read and write the file itself, allowing you to handle encoding as needed.
   - The function should overwrite the file it is given (the file is already copied before optimisation).

3. **Register your function** in the `optimisation_map` dictionary, mapping the new file extension to your function.

4. **Document your function** with a clear docstring describing its purpose and usage.

**Example:**

```python
def optimize_xml(file_path):
	"""
	Optimize an XML file by removing unnecessary whitespace.
	Args:
		file_path (str): Path to the XML file to optimize.
	"""
	# Add your XML optimisation logic here
```

Feel free to open issues or submit pull requests for new file type support!

