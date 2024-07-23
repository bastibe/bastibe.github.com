set "filename=%1"
set "filename=%filename:\=/%"
emacs -batch -script .vscode/init.el -eval "(org-static-blog-publish-file \"%filename%\")"