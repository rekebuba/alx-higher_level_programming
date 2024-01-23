import importlib
import sys

def check_documentation(module_name):
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Error: Could not import module '{module_name}'.")
        return

    # Module documentation
    print("Module Documentation:")
    print(module.__doc__)

    # Iterate through the attributes of the module
    for name, obj in module.__dict__.items():
        # Class documentation
        if isinstance(obj, type):
            print(f"\nClass Documentation ({name}):")
            print(obj.__doc__)

        # Function or method documentation
        elif callable(obj):
            print(f"\nFunction/Method Documentation ({name}):")
            print(obj.__doc__)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_docs.py <module_name>")
    else:
        module_name = sys.argv[1]
        check_documentation(module_name)
