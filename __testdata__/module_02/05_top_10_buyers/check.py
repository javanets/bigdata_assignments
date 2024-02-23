import os
import sys


def try_get_line(stream):
    try:
        return next(stream), True
    except StopIteration:
        return None, False


def main():
    answer_file = os.path.join(sys.argv[1], "output")
    output_file = "solution_output"

    with open(answer_file, "r") as answer:
        with open(output_file, "r") as output:
            striped_answer = map(lambda x: x.strip(), answer)
            striped_output = map(lambda x: x.strip(), output)
            has_answer, has_output = False, False
            while True:
                answer_line, has_answer = try_get_line(striped_answer)
                output_line, has_output = try_get_line(striped_output)
                if not has_answer or not has_output:
                    break
                if answer_line != output_line:
                    print(f"Expected   : {answer_line}", file=sys.stderr)
                    print(f"Your output: {output_line}", file=sys.stderr)
                    exit(1)
            while has_answer:
                answer_line, has_answer = try_get_line(striped_answer)
                if answer_line:
                    print(f"Expected : {answer_line}", file=sys.stderr)
                    print(f"Your output ended prematurely.", file=sys.stderr)
                    exit(1)
            while has_output:
                output_line, has_output = try_get_line(striped_output)
                if output_line:
                    print(f"Expected no more output lines.", file=sys.stderr)
                    print(f"Your output: {output_line}", file=sys.stderr)
                    exit(1)



if __name__ == "__main__":
    main()