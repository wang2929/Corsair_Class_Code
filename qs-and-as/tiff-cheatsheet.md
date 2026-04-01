# Tiffany's Coding Cheat Sheet
This is a compilation of notes I've taken over my time at Code Platoon. The notes are primarily for syntax and important CLI commands.

## Helpful shell commands
- `grep -nir <name> .` to find old project names mentioned and rename
    - `n` option to display line numbers
    - `i` option to ignore case
    - `r` option to search recursively (in subfolders)

## Some nice prompts for resume refining
Courtesy of [Calvin Joewono](https://www.linkedin.com/in/cjoewono/)
- Act as a senior recruiter. Analyze my resume against this job description. Give me a match score out of 100 and list the top 5 missing keywords i need.
- Act as a senior recruiter. I am going to provide my resume and a job description. Analyze my resume against this job description, give me a match score out of 100, and list the top 5 missing skills or keywords I need to include to pass an ATS scan.
- Rewrite my experience section to naturally include those keywords. Use the Google X-Y-Z formula: Accomplished [X] as measured by [Y], by doing [Z].
- Based on the missing keywords and the job description, rewrite my experience section to naturally include those keywords. Use the Google XYZ framework: Accomplished [X] as measured by [Y] by doing [Z]. Make sure the bullet points are high-impact and focus on results, not just tasks.
- Now acts as an Applicant Tracking System filter. Scan my new resume. Tell me which sections a bot would struggle to read.
- Act as an applicant tracking system filter. Scan my updated resume and tell me which sections a bot would struggle to read. Please also ensure the output is in a clean format, removing any complex elements that could lead to rejection.
- Act as the hiring manager for this specific role. Ask me the three hardest technical questions you would ask. Then give me the perfect response based on my background.


## Planning a project
This contains some steps to making an app from scratch.

### Elevator pitch template

> 
> For *[target customer]*
>
> who *[statement of need or opportunity]*
>
> the *[product name]*
>
> is a *[product category]*
>
> that *[key benefit, compelling reason to buy/use]*.
>
> Unlike *[primary competitive alternative]* 
>
> our product *[statement of primary differentiation]*.
>

### Scope
Vocab:
- Features: buckets of functionality that solves a problem or adds value
- User stories: break features to more detailed descriptions of the feature
- Acceptance criteria: how to know something is done

Goal - big idea, broadest "why" behind app; business outcome
- Feature 1 - big pieces of functionality
    - User story 1.1 - smaller, testable units of value associated with the feature
    - User story 1.2
- Feature 2
    - User story 2.1

Example: Dinner Party. Goal: Have fun!
- Plan the meal
    - Allergies
    - 3 course menu
- Materials
    - list of non-perishable items
    - seating, chairs
- Set up event
    - Clean venue
    - RSVPs

### Feature Prioritization
MoSCoW method (MSCW):
- Must have: needed for the project to succeed.
- Should have: high-priority bonuses - nice to have but workarounds exist for now
- Could have: wishlist; cool features but not essential now; future ideas
- Won't have: not now; use to prevent scope creep

## Markdown
Using Markdown Preview Enhanced extension on VS Code, view the formatted markdown using `ctrl+k + v`

## Github
Using Github notes here.
### Change default branch name
Change default branch setting: `git config --global init.defaultBranch main`
Rename branch: `git branch -m {name}`

### All about git
- `{ref}` - anything git can resolve into a commit. Possible refs: `branch_name, commit_id, rel_ref, tag_name`
- Create branch_name: `git branch branch_name {ref!optional}`
- Reassign branch_name to a commit_id (not allowed on current branch): `git branch -f branch_name {ref}`
- Change to a {ref}: `git checkout {ref}`
- Create and change to branch_name: `git checkout -b branch_name`
- Merge current branch with branch_name: `git merge branch_name`
- Rebasing copies and pastes a commit to clean up the commit tree: `git rebase {ref}`
  - Rebase copies and pastes from `{ref}` to the current commit
  - `-i` interactive flag to allow to drop and re-order commits along a branch
- Relative refs (rel_ref): move upwards one commit: ^, vs move upwards n commits: ~n
    - Use this to replace branch_name or commit_id with a commit relative to current
    - Can specify ^num if there's multiple parents (first parent is oldest parent, smallest hash)
    - Can string together ^ and ~ e.g. `main~2^3~2` goes back 2, 3rd parent, then back 2 again
- Use reset or revert to undo a commit
    - for local branches: `git reset {ref}`; vs for remote branches: `git revert {ref}`
- Copy a series of commits to below the current location: `git cherry-pick [list of {ref}s]`
- Tags for marking commits; anchor certain parts of the work process: `git tag tag_name {ref}`
    - You cannot add commits off of tagged commits
- How far {ref} currently is from closest anchor: `git describe {ref}`
    - Describe format: `tag - numCommits - g<hash> (hash of {ref})`

### All about git and cloud (Github)
- Use clone to make a local copy of a remote repository: `git clone <remote_git_repo>`
- Remote branches are for the state of the remote repo
    - Remote branches are on the local repository, not remote repository
    - Default main remote name is origin
- Fetch (git fetch) does two things: downloads commits in remote but not local and updates remote branch's commit location
    - Does NOT change any local files; only downloads info
    - Basically creates a branch with the remote changes
- Pull (git pull) does two things: fetches and merges
- Push (git push) uploads your local changes to remote repository
    - git.default defines default behavior
    - Otherwise git push remote_ref local_ref -> upload commits on local ref to remote ref
        - local_ref can be a range of commits source:destination
- Diverging work: local repo doesn't have commits in the remote repo
    - Can fetch, rebase origin, and then push
    - Can fetch, merge origin, and then push
    - Can use git pull --rebase for fetch and merge/rebase

### Github process
1. create repo in Github
2. git remote add origin git_url
3. git push -u origin main

To copy a repo from Github: git clone git_url
(then I just `delete .git rm -rf .git`)

## Docker
- Build an image: `docker build -t image-name .`
- Build a container for React: `docker run --rm -p 5173:5173 -v $(pwd):/app -v /app/node_modules --name <container-name> <image-name>`
  - rm flag to remove container after finishing
  - p flag for linking ports, connecting current network to Docker network
  - v flag for mounting, connecting current directory to Docker directory
  - name for the container name
  - my-vite-image is the name of the vite image
- build image first, then run container
- to build the image: `docker build -t image_name`
- to build containers (--rm for remove after, but don't have to do that): `docker run --rm container_name image_name`
- workflow for container management:
  1. Stop container
  2. Delete container
  3. Delete image
  - remember containers depend on images
- to view containers (-a for all containers): `docker ps -a`
- to remove containers (-f to force stop if container is running): `docker rm -f container_name`
- to see images: `docker images`
- to remove images: `docker rmi image_name`
- Can use a `run.sh` to build image and run container
  - remember to change permissions `chmod +x run.sh`
- Open bash terminal: `docker exec -it <container name or id> bash`
- Run as root: add -u user flag `docker exec -it -u root <container-name> bash`
### For me: Running while having ghcr.io issues
1. Build the image: `docker build --tag image_name /location/`
2. Use regular docker run `docker run --rm --name <container-name <image-name`
3. Either install packages as root or add RUN commands to Dockerfile
### Docker Compose
- 


## HTML and CSS
- Typical files include index.html (the structure), styles.css (the formatting and colors), and app.js (the javascript script to do stuff)
- Add stylesheet: `<link rel="stylesheet" href="styles.css">`
- Add script.js: `<script src="path/to/script.js" defer async></script>`
  - defer async is because scripts are linked to the top of the index.html page but run at the end
### shorthands in VS Code
- Can use ! + tab to make the html head
- elem > child.class * number, specify the format using selectors, can specify #id or .class, and multiply for repeat
- An HTML element can have multiple classes separated by spaces e.g. class="class1 class2", then can style by combining multiple CSS styles

## Python
- For dictionary, can use get method to get the value
    - dict.get(key, default), can assign a default value to return if doesn't exist
### Lambda Functions
TBD but I want to write something about it
### Django
- Virtual environment: `python -m venv <env_name>`
- Activate venv: `source <env_name>/bin/activate`
- Then to deactivate, use deactivate
- install django with pip, then run `django-admin` to check it worked
- new project: `django-admin startproject <name_proj>`
- create an app `python manage.py startapp <app_name>`
- add app to installed apps under settings.py
- update database to postgres
    - 'ENGINE': 'django.db.backends.postgresql'
    - 'NAME': 'db_name'
    - 'HOST': 'container-name'
    - 'PORT': '5432',
    - 'USER': 'user_made_in_env_vars'
    - 'PASSWORD': 'password_made_in_env_vars'
- install psycopg3 `pip install "psycopg[binary]"`
- get requirements.txt (for the container) `pip freeze > requirements.txt`
- Make a Dockerfile for django
    - use Python image (of course)
    - WORKDIR /app
    - COPY . . 
    - install requirements.txt
    - EXPOSE web port
    - CMD to run server
- update ALLOWED_HOSTS in settings.py to connect to container
- Make the Docker compose to link everything together
- In the Django terminal (container or local) run `python manage.py shell` to open shell
    - can import models from app.models to test methods
- To migrate, run `python manage.py makemigrations` then `python manage.py migrate`
#### Fixtures
- In the app directory, make a directory to hold fixtures
- To export data, run `python manage.py dumpdata {app}.{model} --indent 2 > {app}/fixtures/{data}.json`
    - app for the django app within the project folder
    - model for the table model getting exported
    - {data}.json folder can be named anything
- To import data to the table, run `python manage.py loaddata {data}.json`
    - {data}.json to match the export name above

## Javascript
- <b>if-else shorthand:</b> condition ? true-expression : false-expression
### DOM stuff
- getElementsByClassName() returns an HTMLCollection, not an array. To use array methods, cast to Array using Array.from()
### Arrow Functions
Arrow functions are good to use for one-liner functions. They're compact and quicker to write. General recommendation is to use arrow functions when possible. Do not use arrow functions for class methods, for functions that you want to reuse outside of the current function, and for functions that lose too much readability/clarity.

#### Example Syntax
##### No parameters:
```
function() {
    expression;
    expression;
    more expressions;
}
```
You can use these arrow functions:
```
() => expression;   // Short functions

() => {             
  expressions;      // Long functions
}
```
##### One parameter:
```
function(param) {
    expression;
    expression using param;
    more expressions;
}
```
You can use these arrow functions:
```
param => expression     // Short functions

(param) => expression   // Short functions

param => {
  statements            // Long functions
}
```
##### More than one parameter
```
function(param1, param2, param3) {
    expression using param1;
    expression using param1 and param2;
    expression using param 3;
}
```
You can use these arrow functions:
```
// Short functions
(param1, paramN) => expression 

// Long functions
(param1, paramN) => {
  statements
}
```
### Array Manipulation
#### Filter 
Filter is a method for array manipulation. It takes a function and keeps all elements that return true in the function. Below example filters out all elements less than 5.
```
function exampleFilter(arr) { 
    return arr.filter((elem) => elem > 5); 
}
console.log(exampleFilter([1, 3, 5, 7, 9, 11]));
// Prints [7, 9, 11]
```

## React
My React notes here. Starting with some misc notes.
- .jsx files are for react components, .js for Javascript utils
- Create new project using vite: `npm create vite /project/location`
- Install dependencies: `npm install`
- Run the app: `npm run dev`
### For containerization
- run.sh script builds the image then runs the container
    - `-p 5173:5173` links machine port 5173 to Docker port 5173
    - `-v $(pwd):/app & -v /app/node_modules` is mounting the directories to container
- package.json dev script should `--host` to allow remote connection
- Dockerfile should `RUN npm install` before `CMD npm run dev`
    - Dockerfile should also expose the mapped port 5173
- Maybe I can play around with ports later, but for now, I don't know enough about container networking.
### Using react-router-dom
Setup steps:
1. Create a pages folder for the routing pages .jsx files
2. Create a router.jsx file 
    - import pages
    - import createBrowserRouter() from react-router-dom
3. Set up createBrowserRouter() in router.jsx. Argument is a route object (list)
    - Takes a list of routing dictionaries
    - path: defines the root of the router
    - element: defines the element that renders on a match (in this case, App page)
    - children: subpages from the root page
4. In main.jsx, import the router and `import { RouterProvider } from 'react-router-dom'`
    - Set up a null element `<RouterProvider router={ router page }/>`
5. In App.jsx, `import { Outlet } from 'react-router-dom'`and set up the Outlet page

Things like the createBrowserRouter can change to a different type of router.


## PostgreSQL
### How to (maybe) install other versions
- Uninstall the wrong version of PostgreSQL (Ubuntu): `apt-get --purge remove postgresql-{number}`
- `psql -U {username} -d {db_name}` to run in psql as a specific user (useful in the container)
### To install PostgreSQL 14:
- `sudo apt update` to grab latest packages
- `sudo apt install wget -y` for wget (-y for yes)
- `wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -` to import the repository key
- `sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'` to find and install the PostgreSQL repository and packages
- `sudo apt update` to upgrade packages again
- `sudo apt install postgresql-14` to install PostgreSQL 14
- `sudo service postgresql@14 restart` to restart the service
- `sudo -u postgres psql` to access shell (you're done, yay!)
### Add your user to your database
- Log in as postgres `sudo -u postgres -i`
- Run `CREATE ROLE {username} superuser LOGIN;`
    - if user exists, then run `ALTER ROLE {username} WITH superuser LOGIN;`
- Good to `\q` and exit out of postgres shell, then log into the database as user
    - as username, `psql {database}`
### Copy from CSV
- [Reference link](https://www.postgresql.org/docs/18/sql-copy.html)
- `COPY table FROM filepath WITH DELIMITER AS ',' CSV HEADER;`
- copy the file to /tmp/ folder so that PostgreSQL server has access
### PSQL shell
- `createdb` and `dropdb` to add/remove databases
- `psql` useful options:
    - `-h` for host e.g. `-h localhost` for psql in a container
    - `-p` for port e.g. `-p 5433` if I bind the container to port 5433
    - `-d` for database name
    - `-U` for database user

## Dot Net Stuff
Not related to the class, but personal notes for me since I'm working on web API using ASP.NET.
- Why write interfaces? Interfaces act much like an abstract class or a normal parent class. Interface contains syntax of methods shared across different services. See [discussion on stackoverflow](https://stackoverflow.com/questions/6802573/interfaces-whats-the-point)
### Web API
- MVC vs Web API: MVC is a development framework for creating full stack web apps. Model for classes that hold data, view for the user UI, and controller for connecting the view and the model. Versus web API is only the model part. 
    - See [this stackoverflow answer](https://stackoverflow.com/a/65969849) on MVC in the context of React
- Minimal APIs vs Controller-based: Controller-based APIs are more structured vs Minimal APIs offer more freedom to structure an API
    - Structure means less room for errors
    - Freedom means faster to implement
- Definitely use controller-based for a full-stack MVC app - controller-based can return app parts like views, pages, and more
- On Minimal APIs, see [Tess Fernandez's article](https://www.tessferrandez.com/blog/2023/10/31/organizing-minimal-apis.html) on how to structure minimal APIs
### EF Core process
Entity Framework Core or EF Core is dotnet's way of linking code data to the database. You can start with code and then map to DB or start with the DB and map the code models to match. Model first is similar to Code first except you only define the models before creating the database, not the other parts of the backend.

Generally Code First is preferred since the heavy logic happens in code. The API has to be able to grab data efficiently first. Frontend can be flexible on displaying the API data, and database can be flexible in setup. A good understanding of both code and database is important when making an API.
#### Code first migration
1. Add classes for each table into a Models folder
    - Classes should define the table restrictions, either with Fluent API or Data Annotations
    - Fluent API wins over Data Annotations and Conventions
    - Fluent API to OnModelCreating in the DbContext, vs Data Annotations are marked in class files
    - See [.Net Code Chronicles](https://amarozka.dev/entity-framework-data-annotations/) for more setup instructions on how to set up.
2. Add a DBContext into the Data folder.
3. Add relevant packages. See [available database providers](https://learn.microsoft.com/en-us/ef/core/providers/)
4. In Package Manager console, command `Add-Migration "Initial Migration` to add an initial migration
    - can update the name for subsequent migrations
    - use `-o` or `--output-dir` to define the Migrations path e.g. `Data\Migrations`
5. Command `Update-Database` to see table defined as the models
#### Database first migration
1. Download relevant packages. See [available database providers](https://learn.microsoft.com/en-us/ef/core/providers/)
2. In the Package Manager console, type `Scaffold-DbContext {connectionString} {package name} -ContextDir Data -OutputDir Models`
    - Connection string e.g. `host=localhost;port=5432;username=test;password=test`
    - Package name can be for Pomelo, Npgsql, Microsoft's SQL, etc. e.g. Microsoft.EntityFrameworkCore.SqlServer
    - `-ContextDir` option for the database context directory
    - `-OutputDir` option for the folder where classes corresponding to tables should go
    - `-DataAnnotations` to include data annotations in the class
        - Fluent API is used by default in OnModelCreating
    - More details [here](https://learn.microsoft.com/en-us/ef/core/managing-schemas/scaffolding/)

#### EF Core and MySQL
- Pomelo is open source and preferred package for MySQL using EF Core
- As of February 2026, Pomelo hasn't been updated for .net 10
    - Use version 9 of EF Core plus Pomelo is compatible with .net 10
#### EF Core and PostgreSQL
- Npgsql is updated for .net10 and ready to go with most recent stuff
- Be sure to update the username and password in the testing connection string

## Backend (web API plus DB) container deployment
- Use two Docker containers: one for web server and one for DB
    - expose a port (5432 for PostgreSQL) for the web server and database to talk
    - Run web server on the port that should be exposed for the API
- Make one container first, then use `--link` option on the second container during `docker run`
- maybe run database detached `-d` option
### For the compose.yaml:
1. Make the Dockerfile for the web server
    - For Django, image is Python
    - set workdir to /app
    - copy files in current directory to container
    - install requirements.txt
    - expose port 8000 for web server
2. In compose.yaml, under services, set db to the database image
    - be sure to set env vars for the user (either in the yaml or in .env file)
    - map port 5432 to 5433 locally (postgreSQL runs locally on 5432)
    - define the container name with 'container-name'
    - name image with 'image' attribute
    - if web part depends_on the database and has a condition for service_healthy, add a health check
        - for postgres, `test: ["CMD-SHELL", "pg_isready -U {user} -d {database}"]` is a good command for it (be sure to replace user and database)
        - interval checks for the output
        - timeout determines when to stop checking for health
        - retries is how many times to try before giving up
    
3. In compose.yaml, under services, set web to build from Dockerfile
    - 'container-name' defined
    - command to run server
    - map port 8000 to 8000
    - volumes should mound current directory . to /app
    - depends_on adds a check to make sure web doesn't build before db
        - can add a status to the db based on `condition` either to check started, check completed, or by health check
        - healthcheck is a command to see if a service is healthy
    - can run multiple commands by a list `[sh, -c, 'python manage.py migrate && python manage.py runserver 0.0.0.0:8000']` (I had issues with a regular string)
    - to make a superuser, set environment variables to DJANGO_SU_USERNAME, DJANGO_SU_EMAIL, and DJANGO_SU_PASSWORD. Then the command is `python manage.py createsuperuser --no-input` with the no-input flag
4. `docker compose up` to run and `docker compose down` to remove containers
#### Other tips:
- Will add something about volumes for the DB to map the data to a local folder to hold the data

## Database Design
- First normal form is for a regular table
    - Some table items like customer ID and customer name, which are linked, still exist in the same table
- Second normal form is for a table where keys called primary determine vales in other columns
    - Customer table to seprate customer info from sales info
- Third normal form is when all transitively dependent values are removed
    - transitively dependent: when one value determines values in other columns e.g. customer id and customer name
    - values that depend on each other are in their own table
- Conceptual vs Internal vs External schema
    - Conceptual: model databases after real life
    - Internal: the structure of a database inside the computer
    - External: how other users and external apps use the data