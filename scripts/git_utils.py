import subprocess


def git_compare_versions():
    return subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )



def git_commit(message: str):

    subprocess.run(
        ["git", "add", "."],
        check=True
    )

    commit_result = subprocess.run(
        ["git", "commit", "-m", message],
        capture_output=True,
        text=True,
        check=True
    )

    push_result = subprocess.run(
        ["git", "push"],
        capture_output=True,
        text=True,
        check=True
    )

    return {
        "commit": commit_result,
        "push": push_result
    }