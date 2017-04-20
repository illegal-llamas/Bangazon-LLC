# Illegal Llamas Pull Request Template

## Status
Is this PR ready to be looked at by other group members? 

## Description
A description of what this PR does

### Related Tickets 
***
List all related tickets that are addressed by this pull request

[A link to a ticket](link.com)

[A link to a ticket](link.com)

### Impacted Areas of the Application
***
Files that this PR modifies or affects in some way. 
```
    Fileexample.py
    fileexample.db
    fileexample.sql
```

### Deploy Notes
***
Anything that a user needs to know in order to deploy/properly test this branch. Provide step by step instructions that address any db migrations, packages needed, ect. Be as specific as possible in your instructions

For example: 
```
    git pull 
    git fetch --all
    git checkout example_branch_name
    python manage.py makemigration
    python manage.py migrate
    python manage.py runserver
```