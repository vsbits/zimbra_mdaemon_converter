import secrets
import os


ENV_FILE = ".env"


def main():
    if os.path.exists(ENV_FILE):
        print(f"Arquivo '{ENV_FILE}' já existe!")
        exit(1)
    
    key = secrets.token_bytes(16)

    with open(ENV_FILE, "x") as fh:
        fh.write(f"SECRET_KEY = {key}")
    print(f"Arquivo {ENV_FILE} gerado com sucesso!")


if __name__ == "__main__":
    main()