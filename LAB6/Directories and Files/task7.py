def copy_file(src, dest):
    open(dest, "w", encoding="utf-8").write(open(src, "r", encoding="utf-8").read())

copy_file("source.txt", "destination.txt")
