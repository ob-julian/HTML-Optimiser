import fnmatch
import os

def read_gitignore_patterns(root_path):
    """Read .gitignore patterns from the given root path."""
    gitignore_path = os.path.join(root_path, '.gitignore')
    patterns = ['.git', '.gitignore']
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    patterns.append(stripped_line)
    return patterns

def create_ignore_function(root_path, folder_name):
    """Create an ignore function for shutil.copytree based on .gitignore and folder name."""
    patterns = read_gitignore_patterns(root_path)
    patterns.append(folder_name)

    def ignore_function(directory, filenames):
        ignored_names = []
        for filename in filenames:
            for pattern in patterns:
                if fnmatch.fnmatch(filename, pattern):
                    ignored_names.append(filename)
                    break
        return ignored_names

    return ignore_function
