import os

def main():
    who = os.environ["INPUT_MYINPUT"]

    my_output = f"Hello {who}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()