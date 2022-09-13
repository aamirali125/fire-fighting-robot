def progress_bar(progress, total):
    percent = 100 * (progress / total)
    bar = u"\u2588" * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print()