import os

def print_tree(start_path='.', prefix=''):
    entries = sorted(os.listdir(start_path))
    entries = [e for e in entries if not e.startswith('.')]  # Skip hidden files
    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        connector = '└── ' if index == len(entries) - 1 else '├── '
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = '    ' if index == len(entries) - 1 else '│   '
            print_tree(path, prefix + extension)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Cek struktur project.')
    parser.add_argument(
        'path',
        metavar='PATH',
        type=str,
        nargs='?',
        default='.',
        help='Path ke folder project (default: current directory)'
    )
    args = parser.parse_args()
    print(f"Struktur project di: {os.path.abspath(args.path)}\n")
    print_tree(args.path)
