import argparse
from dictionary_api import fetch_word
from utils import display_word, export_word

def main():
    parser = argparse.ArgumentParser(description="Dictionary CLI Tool")
    parser.add_argument("--word", type=str, required=True, help="Word to look up")
    parser.add_argument("--export", type=str, help="Export JSON file")
    args = parser.parse_args()

    data = fetch_word(args.word)
    display_word(data)

    if args.export and data:
        export_word(data, args.export)
        print(f"✅ Exported to {args.export}")

if __name__ == "__main__":
    main()
