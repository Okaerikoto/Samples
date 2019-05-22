## Freenect

**source** : https://openkinect.org/wiki/Main_Page

**Open third kinect** : ` $ freenect-glview 2`

**Open all 4 kinects** :` $ for i in 0 1 2 3; do ( freenect-glview $i &); done`

**record** : `$ sudo fakenect-record record_name`
→ saves the acceleration, depth, and rgb data as individual files with names in the form `"TYPE-CURRENTIME-TIMESTAMP"` where TYPE is either (a)ccel, (d)epth, or (r)gb, TIMESTAMP corresponds to the timestamp associated with the observation (or in the case of accel, the last timestamp seen), and CURRENTTIME corresponds to a floating point version of the time in seconds.	

**Record device 0** : `fakenect-record -d 0 ../../record/m1_0`

**With log**: `fakenect-record -d 0 ../../record/m1_0 > ../../record/device0.log`

**Problem**: 
can not open cam → add `sudo`

## Freenect2

**launch video** : `$ ./Documents/freenect2/libfreenect2/build/bin/Protonect`

## GIT

**Pb lors du clonage** : unable to access 'https://github.com/OpenKinect/libfreenect2.git/'
→ rajouter `$ socksify` devant pour detecter le proxy automatiquement :
`socksify git clone https://github.com/OpenKinect/libfreenect2.git`
Se generalise a tout acces web a partir de la ligne de commande en cas de non reaction si le reseau utilise un proxy ( = gros firewall qui redirige la connection)

## Liens symbolics sur Linux (exemple avec matlab)

**Source** : http://enddl22.net/wordpress/2013/07/page/2

In order to **manually create the symbolic link**, browse to the `/usr/local/bin/` folder and run the following command:
```ln -s $MATLAB/bin/matlab matlab```
where `$MATLAB` is the MATLAB installation directory.

To create a launcher for a Desktop environment, you can do so with the following steps:
1. Right click on the Desktop and select "Create Launcher"
2. Under the name field, type in MATLAB or MATLAB R2009a, etc.
3. If you have the symbolic link created, under the command field, enter:
`matlab -desktop`
Otherwise you will need to give the full path to the matlab script located in `$MATLAB/bin` (where `$MATLAB` represents the installation folder for MATLAB) followed by the `-desktop` flag. For example:
```/usr/local/matlab_r2009a/bin/matlab -desktop```
4. Press OK to create the launcher.

## Analyse of the usb ports

- liste the usb device : `$ lsusb`
- show usb device hierarchie as a tree : `$ lsusb -t`
- n'afficher que les lignes contenant “57” :  `lsusb | grep 57`

## Terminal shortcut

- `Shift+Ctrl+t`	new tab	
- `Shift+Ctrl+w`	close tab	
- `Shift+Ctrl+n`	new window	
- `Ctrl+{PgUp,PgDown}`	change tabs	
- `Shift+Insert`	paste from selection buffer, or if that's empty the clipboard	
- `Ctrl+Insert`	copy selection to clipboard	
- `Shift+Ctrl+v`	paste from clipboard	
- `Ctrl+Click`	Open URL under mouse cursor

## GIT
- Alias : https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases
- Subtree :
`git remote add libfreenect2 https://github.com/OpenKinect/libfreenect2.git`
`git subtree add --prefix libfreenect2 libfreenect2-record master –squash`

- Go to a pt of history:
`reflog`
`git reset --hard HEAD@{8}`

- Undo a commit and redo
```
$ git commit -m "Something terribly misguided"              (1)
$ git reset --soft HEAD~                                    (2)
<< edit files as necessary >>                               (3)
$ git add ...                                               (4)
$ git commit -c ORIG_HEAD                                   (5)
```
1.	This is what you want to undo
2.	This is most often done when you remembered what you just committed is incomplete, or you misspelled your commit message1, or both. Leaves working tree as it was before git commit.
3.	Make corrections to working tree files.
4.	git add whatever changes you want to include in your new commit.
5.	Commit the changes, reusing the old commit message. reset copied the old head to .git/ORIG_HEAD; commit with -c ORIG_HEAD will open an editor, which initially contains the log message from the old commit and allows you to edit it. If you do not need to edit the message, you could use the -C option instead.

- Amending the most recent commit message
`git commit --amend`
Will open your editor, allowing you to change the commit message of the most recent commit. Additionally, you can set the commit message directly in the command line with:
`git commit --amend -m "New commit message"`
…however, this can make multi-line commit messages or small corrections more cumbersome to enter.
Make sure you don't have any working copy changes staged before doing this or they will get committed too. (Unstaged changes will not get committed.)

## Sublime Text
Add symbolic link : `$ cd /usr/local/bin$ `
		       `$ sudo ln -s ~/Documents/Sublime\ Text\ 2/sublime_text sublime_text`
Panneau de recherche dans les fichiers : `(Ctrl+Shift+F)`

## Permission
Source :(http://www.thegeekstuff.com/2010/06/chmod-command-examples/)

Following are the symbolic representation of three different roles:
- u is for user,
- g is for group,
- and o is for others.
Following are the symbolic representation of three different permissions:
- r is for read permission,
- w is for write permission,
- x is for execute permission.

Following are few examples on how to use the symbolic representation on chmod.
1. Add single permission to a file/directory
Changing permission to a single set. + symbol means adding permission. For example, do the following to give execute permission for the user irrespective of anything else:
`$ chmod u+x filename`
2. Add multiple permission to a file/directory
Use comma to separate the multiple permission sets as shown below.
`$ chmod u+r,g+x filename`
3. Remove permission from a file/directory
Following example removes read and write permission for the user.
`$ chmod u-rx filename`
4. Change permission for all roles on a file/directory
Following example assigns execute privilege to user, group and others (basically anybody can execute this file).
`$ chmod a+x filename`
5. Make permission for a file same as another file (using reference)
If you want to change a file permission same as another file, use the reference option as shown below. In this example, file2’s permission will be set exactly same as file1’s permission.
`$ chmod --reference=file1 file2`
6. Apply the permission to all the files under a directory recursively
Use option -R to change the permission recursively as shown below.
`$ chmod -R 755 directory-name/`
7. Change execute permission only on the directories (files are not affected)
On a particular directory if you have multiple sub-directories and files, the following command will assign execute permission only to all the sub-directories in the current directory (not the files in the current directory).
`$ chmod u+X *`
Note: If the files has execute permission already for either the group or others, the above command will assign the execute permission to the user

## Script shell
- Se donner les droits: `chmod +x cript.sh`
- Executer: `./script.sh`
- Parser des arguments : `osr600doc.sco.com/en/SHL_automate/_Passing_to_shell_script.htmlsh`
- Variables:
```
NAME="Zara Ali
echo $NAME
```
Attention : pas d'espaces autour de =
- Operations: exemples
```
echo $((7+4))
echo $(($i/2))
```

- Enchainement des commandes
1. les caractères d’enchainement
Il existe sous Linux trois caractères qui permettent l’enchainement des commandes, il s’agit de `;`, `||` et `&&` . Chacun de ces trois caractères ont un type d’exécution différents au niveau de l’enchainement des commandes.
2. Le point virgule
Enchaîner les commandes sans se soucier de la réussite ou de l’échec de chacune.
```kdir /home/~/dossier1/; cd /home/~/dossier1/ ; touch file1```
4. Le `&&`
Exécute une commande que si les commandes précédentes ont réussies.
```cd /home/~/dossier1 && touch file1```
Ici, si la commande « cd /home/~/dossier1 » ne s’exécute pas correctement (que le dossier n’existe pas), la commande « touch file1 » qui créer un fichier vide ne s’exécutera pas non plus et par conséquent ne déclenchera pas de message d’erreur.
Linux enregistre un paramètre à chaque exécution de commande (comme un flag) qui peut être récupéré dans un script (par exemple). Ce paramètre se met à « 0 » si la commande s’est executée correctement et à « 2 » (dans la plupart des cas) quand la commande à échouée.
Pour déterminer si une commande a bien réussie, Linux analyse ce paramètre et, dans le cas d’un « 0 » avec un enchainement de commande « && », il exécute la commande suivante. Si le paramètre en question est « 2« , c’est que la commande précédente ne s’est pas correctement déroulée et il met donc fin à l’exécution des prochaines commandes.
5. Le `||`
Dans d’autres cas, il peut être intéressant d’exécuter une commande uniquement si la commande précédente ne se déroule pas correctement au lieu de mettre fin à toute la ligne de commande. Cela est possible avec les caractères « || ».
Par exemple si l’on souhaite, comme auparavant, voir si un dossier existe et si c’est le cas y créer un fichier. On peut également vouloir créer le dossier si il n’est pas encore présent :
cd /home/~/dossier1 || mkdir / /home/~/dossier1 && touch file1
C’est un exemple simple mais on peut imaginer des choses beaucoup plus complexes. Ici, si le retour du paramètre de vérification de l’exécution de la commande n’est pas « 0 » (= la commande « cd /home/~/dossier1 » à échouée), on créera le fichier avec la commande « mkdir« . Dans un second temps suite à cela on créera le fichier « file1« .

- Boucles
https://fr.wikibooks.org/wiki/Programmation_Bash/Boucles

- Condition
```
if condition ; then
    commands
fi
```
Second form:
```
if condition ; then
    commands
else
    commands
fi
```

- Third form
```
if condition ; then
    commands
elif condition ; then
    commands
fi
```
 - ouvrir un terminal, y entrer une commande et le laisser ouvert:
`xterm -e "commande; $SHELL" &`

##Comparaison kinect :http://zugara.com/how-does-the-kinect-2-compare-to-the-kinect-1


## Proxy

Pb de librairie sur matlab:
entrer dans la console pour lancer matlab:
$export LD_LIBRARY_PATH=/usr/local/lib/opencv2.1:$LD_LIBRARY_PATH 
$matlab


## Chercher une librairie : aptitude search boost (exple avc boost)

## ouvrire gestionaire d'imprimante : system-config-printer

