# Tiffany's Coding Cheat Sheet

## Markdown
- Using Markdown Preview Enhanced extension on VS Code, view the formatted markdown using `ctrl+k + v`

## Github
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
### Lambda Functions
TBD but I want to write something about it

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
- To install PostgreSQL 14:
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
- https://www.postgresql.org/docs/18/sql-copy.html
- `COPY table FROM filepath WITH DELIMITER AS ',' CSV HEADER;`
- copy the file to /tmp/ folder so that PostgreSQL server has access
