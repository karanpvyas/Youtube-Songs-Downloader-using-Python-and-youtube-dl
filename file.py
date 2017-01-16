import os

linksFile = open('todo.txt', 'r+');
doneFile = open('done.txt', 'w+');
allLinksArr = linksFile.read().strip().split('\n')
doneLinksArr = doneFile.read().strip().split('\n')
#can push them in a map for O(1) checking below, but eh.


linksDone = doneFile.read().strip()

for link in allLinksArr:
    try:
        if(link not in doneLinksArr):
            os.system('youtube-dl -f 140 -o '+'"%'+'(title)s.'+'%'+'(ext)s" '+ link)
            print "\n---------------------------------------------\n"
            linksDone+='\n' + link
    except Exception as e:
        print e


doneFile.write(linksDone)

linksFile.close()
doneFile.close()
