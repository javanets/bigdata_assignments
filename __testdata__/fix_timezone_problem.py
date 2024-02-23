

if __name__ == "__main__":
    with open("user_activity_log.tsv", "w") as out:
        with open("user_activity_log_old.tsv", "r") as f:
            out.write(f.readline())
            for line in f:
                row = line.strip().split("\t")
                row = row if len(row) == 5 else row + [""]
                row[1] = row[1] + "+00:00"
                out.write("\t".join(row) + "\n")