#!/bin/bash
# Rewrite commit messages to sound more human

git filter-branch -f --msg-filter '
    case "$GIT_COMMIT" in
    c751314*)
        echo "Rewrite docs to sound more natural"
        ;;
    923a188*)
        echo "Add all remaining project files"
        ;;
    5d4c61c*)
        echo "Update README status"
        ;;
    8148e11*)
        echo "Improve user dashboard UI"
        ;;
    7f73e61*)
        echo "Redesign admin dashboard"
        ;;
    50acc39*)
        echo "Fix stats display and timezone"
        ;;
    25adeba*)
        echo "Update stats design"
        ;;
    0b62c83*)
        echo "Add Render deployment config"
        ;;
    *)
        cat
        ;;
    esac
' HEAD~9..HEAD
