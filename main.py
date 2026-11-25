import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(SRC, "rb") as f:
        data = f.read()
    with open(DST, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
