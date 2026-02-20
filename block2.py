import hashlib

def sha256_of_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    try:
        print("SHA-256:", sha256_of_file(path))
    except FileNotFoundError:
        print("File not found.")