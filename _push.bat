global /i del *.pyc

git push https://github.com/goulu/Goulib.git
git push https://goulu@bitbucket.org/goulu/goulib.git
git push ssh://drgoulu@git.code.sf.net/p/goulib/code
git commit googlecode master

svn commit --username=drgoulu svn+ssh://drgoulu@svn.code.sf.net/p/goulib/code-0/trunk