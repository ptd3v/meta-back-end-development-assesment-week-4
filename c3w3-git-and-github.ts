# Git is a version control system designed to help users keep track of changes to files within their projects.     
# Git is used through the CLI (command line interface) and GitHub is a cloud platform.

GitBash - Windows
#Terminal - MAC

ls - la #( -la = List all command)
# The ls -al command is a combination of ls -l (use a long listing format) and ls -a (do not ignore entries starting with .)
# In Linux, all hidden folders start with a .

Git Workflow: 
Working Directory - Modified > (Git Add) > Staging Area > (git commit) > Commited Files/ Folders > (git push) > Remote Repository
After: Remote Repository > (git fetch) > Commited Files
After: Remote Repository > (git checkout) > Working Directory

// The correct workflow is from the working directory to the staging area, then to committed files, remote repository and lastly to your colleague.

Data Structures are a way of organising data that fits the objective.

Data Structure: Lists
[1,2,3] when adding a [4], it is moved to a whole new part of memory. E.g 1,2,3,hello.
By adding the 4, it will overwrite hello. So it is moved to a new block of open memory.
A program adding new items to lists will be very slow in memory.

Data Sturcture: Linked Lists
To avoid the issue above. New items are given a new location in memory, without moving the whole list.
Memory index location: 0 | 1 | 2 | 3 | 4        156 | 497 | 989
Value:                 1   2   3   4   5         6     7     8
By adding [6, 7, 8] to a linked list, it keeps the list intact and just gives a location in memory.
For example, number '6', when adding (appending) to a list, would point to memory index '156'.
