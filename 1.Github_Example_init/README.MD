# Intilizating the project and comitiing 
```sh
1.created a directory called  1.Github_Example_init/ under DTCC_GITHUB_CODE 
mkdir DTCC_GITHUB_CODE/1.Github_Example_init
a.git init 
b.vi README.md
added changes in Readme.md
c.git add README.md or git add . 
d.git status [will tellwhat is updated]
git commit -a -m "added readme.md files"
```  

```sh
2.To set username and email 
git config --global user.name "shanphd"
git config --global user.email klgowrishankarphd@gmail.com
git config --list 
``` 

```sh
3.git log will show all logs 
``` 
```sh
4.git push willpush the files
```   

```sh
5. git branch will give branch
```

```sh

6.gh auth login -> willogin 
gh repo list  -> will repo the list
``` 

```sh
7.ssh keys 

ssh-keygen -t ed25519 

DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->ssh -T git@github.com
Hi shanphd! You've successfully authenticated, but GitHub does not provide shell access.
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->eval "$(ssh-agent -s)"
Agent pid 2163843
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->ssh-add home/gowrishankarphd/.ssh/id_ed25519.pub
home/gowrishankarphd/.ssh/id_ed25519.pub: No such file or directory
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->cd home/gowrishankarphd/.ssh/id_ed25519.pub
bash: cd: home/gowrishankarphd/.ssh/id_ed25519.pub: No such file or directory
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->cd home/gowrishankarphd/.ssh/
bash: cd: home/gowrishankarphd/.ssh/: No such file or directory
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->ssh-add /home/gowrishankarphd/.ssh/id_ed25519.pub
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/home/gowrishankarphd/.ssh/id_ed25519.pub' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->
DataScientist:/run/media/gowrishankarphd/Gowri Shankar/3.Learning/21.Github/1.DTCC_Githubcode->git clone git@github.com:shanphd/DTCC_Snowflake_ML_Code.git
Cloning into 'DTCC_Snowflake_ML_Code'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), 13.82 KiB | 70.00 KiB/s, done.
``` 

```sh

9.Github tags
``` 




