# Git and Github: Why and How

## First: Why

Git is a software service that allows for collaboration, open source development and contribution, and version control. It is more or less commonplace in the programming world and indeed very useful for any programming projects one might have.

Specifically we can use git to work collaboratively on a project without necessarily interfering with each other's work, store code in a safe and easy to access place, and various other things.

## How To:

### Preliminary Things

Git works on the command line, so to use git you should ideally know the basics of working in the command line. It's not too difficult, and if you need help you can always Google around. That goes for using git too. If you really don't want to use the command line you don't have to; there are various interfaces that allow you to use git without it. Two examples are Github desktop (developed by Github itself), and Git Kraken (that my friends use). 

First you will need to install git on your computer. Just search for git and install it with the recommended settings. 

### Into the Meat of Git

Now I'm going to explain how to use git on the command line. 

First, navigate the command line to an empty folder. This folder will be your 'repository' of all the code and possibly resources that the project will use. 

Now save some file to this directory. For example, one called `task5.py` (or whatever your task is). You don't need to write any code yet. Now that you've done this, type the following into the command line:

`git init`

This tells the computer that we want this folder to be our git repository. Now what we need to do is link this local (meaning on your hard drive) repository to the repository on the Github servers. We will do this with the following command:

`git remote add origin https://github.com/KadinTucker/Basket-Ball.git`

There are a lot of words in this command. But basically what we are doing is we are telling the computer that this git repository should be a local version of the git repository located at that URL link. This is the Github page, and it is our `origin`.

Now we will use the most important command there is in git:

`git status`

You should get a message that you have an untracked file, called `task5.py`. If you have any other files they will show up there too, but ideally this folder should be reserved for just things that belong in the programming project. 

Before we can start tracking this file, though (we will discuss what that means in a second), we need to make sure that this local repository is synced up with the `origin`, the Github repository online. To do this we will `pull` from the origin, downloading all files from the online repository. We will do this with the following command:

`git pull origin master`

This tells the computer to `pull` all files from the `origin` on the `master` branch. Since we will not need to do anything with branches, you can always use the `master` keyword in the command. 

Now you'll see that you have more files in your directory. This is the result of the pull. You can now edit any of these files as you like, but for now let's look at the file you created earlier. Type `git status` again, and you can see that this file is still labeled as 'untracked'. This means that the computer doesn't consider this file as part of the repository. Let's change that using the following command:

`git add <filename>`

This tells the computer that we want that file to be a part of the repository. Note also that we will use this command if we have made any changes to an existing file.

For now this is all we're going to add to the repository. What we will do now is create something called a `commit`. A `commit` is a batch of changes to the project that acts as a sort of marking point to the code. Now let's use the following command:

`git commit -m"<message>"`

This tells the computer to batch together all of the files that we added using `git add` and turn them into a `commit`. With a `commit` we also want to put a message that is a very short description of what the `commit` contains. For example, a good `commit` message for this situation is: `"Added task 5"`. This gives us the command:

`git commit -m"Added task 5"`

Lastly we need to send our local repository changes to the online Github repository by doing a `push`. This is basically the opposite of a pull; it sends any new commits you have locally to the online repository. Use then the following command:

`git push origin master`

Now you might need to input your username and password to your Github account. This is to assure that you have permission to directly modify the code in the repository. 

And then you're done! You can check the online Github repository and see your changes. 

If you're still confused on how to do this, you can always do some Googling around to find answers to your questions.

# Quick amendment: using file modules in Python

When we use git we generally can't both be working on one file at the same time. What we'll do is use a modular file system. Fortunately this is really easy to do with Python. 

We've used the `import` command before with libraries like `numpy` and `matplotlib`, but now we will make our own libraries. Let's say that we have two files, `library.py` and `main.py`, and that we want `main.py` to use some functions or variables or class definitions that exist in `library.py`. Let's say that there exists a function `foo()` in `library.py`. Then, as long as `main.py` and `library.py` are in the same directory, we can put the following in `main.py`:

```python
# main.py
import library

library.foo()
```

This runs the `foo()` function from `library.py`. 

We can also use `from library import *` and `import library as <name>` as one would with other libraries. 

You can have your imported file be named anything you want.

Again if you have questions try googling them and you'll likely find the answers you want. 

### One last thing: the main() function

Lastly I will note that in general it is good practice to have your python files have no isolated code. That is, all code in your file should be in functions or in class definitions. You can also defined constants in your code. If there is a script you want to run specifically in that file, what you can do is create a `main()` function. There's nothing special about the name `main()` in python, it is just a standard name. In this function you can program your script as you want it. Then, at the very end of the file, you can put the following code:

```python
if __name__ == '__main__':
    main()
```

What this does is it checks if the file is being run directly or being imported as a module. Now, if you are importing this file from somewhere else the `main()` function won't run. 