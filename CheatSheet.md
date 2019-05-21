# CheatSheet

## Table of content
  - [Sublime Text](##SublimeText)
  - [Markdown](##Markdown)
  - [Git](##Git)
  - [Unity](##Unity)

## Sublime Text
  - Add cursor on the upper/lower line :
       Windows: `alt gr + up/down arrow`
       Linux: `ctrl + alt + up/down arrow`
  - Add cursor at several places :
      Window: `mouse wheel clic` or `ctrl + left click`
      Linux: `ctrl + left click`
	- Go into multi-cursor mode on all occurrences of the selected text `Alt+F3` 
	- Select entire line (on every cursor line) `Control+L`

## Markdown 

[Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Git

[Git aliases](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) :
 ```
 $ git config --global alias.co checkout
 $ git config --global alias.br branch
 $ git config --global alias.ci commit
 $ git config --global alias.st status
 ```
    
[Branching model](http://nvie.com/posts/a-successful-git-branching-model/)

## Unity

Enable point cloud shaders
`cd "C:\Program Files\Unity5\Editor\" ;  .\Unity.exe -force-opengl`

**Format class attributes in inspector**
 - Display and assign a private field in inspector `[SerializeField]` 
 - Make an attribute `required [RequireComponent]`
 - Group by header `[Header("Hi there!")]`
 - Add a 10 pixels of spacing in inspector `[Space(10)]`
 - Set range for the attribute `[Range(5,9)]`
 
 Enumeration `enum Days {Sat, Sun, Mon, Tue, Wed, Thu, Fri};`

