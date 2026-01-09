#!/bin/bash
# Script to fix commit messages - run this if needed
# Note: This requires force push after

git rebase -i HEAD~10
