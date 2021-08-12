from typing import cast

from decouple import config


def main():
    username = config("ACCOUNT", cast=str)
    password = config("PASSWORD", cast=str)
    debug = config("DEBUG", cast=bool)
    print(f"username={username}")
    print(f"password={password}")
    print(f"debug={debug}")


if __name__ == "__main__":
    main()

