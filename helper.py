    os.system("lg2 add .")
    print(f"[{TAG}] command: lg2 commit")
    os.system("lg2 commit -m 'autosaved by script'")
    print(f"[{TAG}] command: lg2 push")
    os.system("lg2 push")

def lg2_status():
    print(f"[{TAG}] command: lg2 status -s")
    output = subprocess.check_output("lg2 status -s")
    if not output:
        return CLEAN
    else:
        return DIRTY

def is_dirty():
    return lg2_status() == DIRTY

def pull():
    if not is_dirty():
        lg2_pull()

def push():
    if is_dirty():
        lg2_push()
