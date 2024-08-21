import os
import yaml

# Define the base directory for your Hugo content
BASE_DIR = "content"

# Define the structure of your course
COURSE_STRUCTURE = {
    "modules": [
        "introduction-to-python",
        "variables-and-data-types",
        "control-flow",
        "functions",
        "working-with-files",
        "error-handling",
        "modules-and-packages",
        "object-oriented-programming",
        "python-data-structures",
        "intro-to-python-libraries",
        "python-best-practices",
        "final-project"
    ]
}

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    """Create a file with optional content."""
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created file: {path}")

def create_index_file(path, title, description):
    """Create an _index.md file with YAML front matter."""
    content = f"""---
title: "{title}"
description: "{description}"
---

# {title}

Add your content here.
"""
    create_file(path, content)

def setup_course_structure():
    """Set up the entire course structure."""
    # Create base content directory
    create_directory(BASE_DIR)

    # Create main _index.md
    main_index_path = os.path.join(BASE_DIR, "_index.md")
    if not os.path.exists(main_index_path):
        create_index_file(main_index_path, "Welcome to PythonPrimer.com", "Your journey to mastering Python starts here!")

    # Create modules directory
    modules_dir = os.path.join(BASE_DIR, "modules")
    create_directory(modules_dir)

    # Create module subdirectories and _index.md files
    for module in COURSE_STRUCTURE["modules"]:
        module_dir = os.path.join(modules_dir, module)
        create_directory(module_dir)
        index_path = os.path.join(module_dir, "_index.md")
        if not os.path.exists(index_path):
            title = module.replace("-", " ").title()
            create_index_file(index_path, title, f"Learn about {title} in Python")

def main():
    setup_course_structure()
    print("Course structure setup complete!")

if __name__ == "__main__":
    main()