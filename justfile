# Preview always runs from the main checkout: Quarto renders no pages when the
# project sits under a dot-directory such as .claude/worktrees/.
port := "4871"

preview:
    cd "$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")" && quarto preview --no-browser --port {{port}}
