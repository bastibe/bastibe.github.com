; -*- coding: utf-8 -*-

(prefer-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(set-language-environment "UTF-8")

;; auto-install packages

(require 'package)
(setq package-archive-exclude-alist '(("melpa")))
(dolist (source '(("elpa" . "http://tromey.com/elpa/")
                  ("gnu" . "http://elpa.gnu.org/packages/")
                  ("nongnu" . "https://elpa.nongnu.org/nongnu/")
                  ("melpa-stable" . "https://stable.melpa.org/packages/")))
  (add-to-list 'package-archives source t))
(package-initialize)

(setq package-archive-priorities
      '(("nongnu" . 10)
        ("melpa-stable" . 9)
        ("gnu" . 8)
        ("elpa" . 7)))

(when (not package-archive-contents)
  (package-refresh-contents))

(defvar my-packages '(org-static-blog)
  "A list of packages to ensure are installed at launch.")

(dolist (p my-packages)
  (when (not (package-installed-p p))
    (package-install p)))

(deftheme typo
  "Theme emulating reading on an E Ink device.")

(let* ((fg "#111111")
       (bg "#fafaf9")
       (bg-light "#ddddd8")
       (fg-medium "#404040")
       (fg-light "#606060")
       (bg-lighter "#f4f4f0")
       (bg-white "#fcfcf8")
       (bg-highlight "#FFF1AA")
       (bg-highlight-2 "LightCyan")
       (bg-highlight-3 "LightGreen")
       (bg-overlay "grey90")
       (my-default-family "PragmataPro")
       ;; strings are the most difficult face to get right, as they
       ;; are deeply integrated into the code and often contain
       ;; code-like structures. I give them a face with a distincly
       ;; different x-height that makes them easy to spot:
       (my-string-family "Agave")
       ;; types are annotations to the code itself, so I use a
       ;; slightly lighter, slightly less conspicuous variant of the
       ;; main faces:
       (my-type-family "Iosevka Comfy")
       ;; Comments should be easily discernible from code. I use an
       ;; italic slant and slabs to make them stand out:
       (my-comment-family "Iosevka Slab")
       ;; Docs usually come in longer paragraphs, and don't need to
       ;; stand out as much. I use an upright slant with a
       ;; lighter-weight family:
       (my-docs-family "Victor Mono")
       (my-docs-height 0.95)
       (headline-1 `(:foreground ,fg :weight semi-bold :height 1.4 :family "InputSerifCompressed"))
       (headline-2 `(:foreground ,fg :weight semi-bold :height 1.4 :family "InputSerifCompressed"))
       (headline-3 `(:foreground ,fg :weight semi-bold :height 1.2 :family "Iosevka Slab"))
       (headline-4 `(:foreground ,fg :weight semi-bold :height 1.1)))

  ;; other compatible fonts: InputMonoCompressed, Iosevka
  ;; Compatible fonts: Monoid HalfTight 0.85, Victor Mono 0.95,
  ;; Lekton 1.1, Ubuntu Mono 1.05, Agave, Iosevka, PragmataPro,
  ;; Monofur

  (custom-theme-set-faces
   'typo

   ;; generic stuff
   `(default ((t (:background ,bg :foreground ,fg :family ,my-default-family))))
   `(fixed-pitch ((t (:family ,my-default-family))))
   `(button ((t (:foreground ,fg :underline t))))
   `(cursor ((t (:background ,fg :foreground "white smoke"))))
   `(custom-variable-tag ((t (:foreground ,fg :weight bold))))
   `(default-italic ((t (:italic t))))
   `(font-lock-builtin-face ((t (:foreground ,fg-medium)))) ; nicht sichtbar
   `(font-lock-comment-delimiter-face ((t (:foreground ,fg-medium :slant oblique :weight light :family ,my-comment-family))))
   `(font-lock-comment-face ((t (:foreground ,fg-medium :slant oblique :weight light :family ,my-comment-family))))
   `(font-lock-doc-face ((t (:foreground ,fg :family ,my-docs-family :height ,my-docs-height))))
   `(font-lock-constant-face ((t (:foreground ,fg))))
   ;; function names and keywords provide the code's /structure/, so I
   ;; make them stand out in bold:
   `(font-lock-function-name-face ((t (:foreground ,fg :underline t :weight bold))))
   `(font-lock-keyword-face ((t (:foreground ,fg :weight bold))))
   `(font-lock-preprocessor-face ((t (:foreground ,fg :family ,my-comment-family))))
   `(font-lock-reference-face ((t (:foreground ,fg))))
   `(font-lock-string-face ((t (:foreground ,fg-light :family ,my-string-family :weight light))))
   `(font-lock-type-face ((t (:foreground ,fg :underline t :family ,my-type-family))))
   `(font-lock-variable-name-face ((t (:foreground ,fg-medium :underline nil))))
   `(font-lock-warning-face ((t (:foreground ,fg :weight bold))))
   `(fringe ((t (:background ,bg :foreground ,fg))))
   `(gnus-header-content ((t (:foreground ,fg))))
   `(gnus-header-from ((t (:foreground ,fg))))
   `(gnus-header-name ((t (:foreground ,fg))))
   `(gnus-header-subject ((t (:foreground ,fg))))
   `(highlight ((t (:background ,bg-highlight))))
   `(ido-first-match ((t (:foreground ,fg :weight bold))))
   `(ido-vertical-first-match ((t (:foreground ,fg :weight bold))))
   `(ido-only-match ((t (:foreground ,fg))))
   `(ido-subdir ((t (:foreground ,fg))))
   `(isearch ((t (:foreground ,fg :box (:line-width -1)))))
   `(isearch-lazy-highlight-face ((t (:foreground ,fg :box (:line-width -1)))))
   `(link ((t (:foreground ,fg))))
   `(minibuffer-prompt ((t (:foreground ,fg-medium :weight bold))))
   `(mode-line ((t (:background ,bg :foreground ,fg :height 1.0))))
   `(mode-line-buffer ((t (:foreground ,fg :weight bold))))
   `(mode-line-inactive ((t (:background ,bg :foreground ,fg :height 1.0))))
   `(mode-line-minor-mode ((t (:weight ultra-light))))
   `(modeline ((t (:background ,bg :foreground ,fg :height 1.0))))
   `(fill-column-indicator ((t (:foreground "gainsboro"))))
   ;; `(hl-line ((t :inherit highlight :extend t))

   ;; latex
   `(font-latex-bold-face ((t (:foreground ,fg))))
   `(font-latex-italic-face ((t (:foreground ,fg :slant italic))))
   `(font-latex-match-reference-keywords ((t (:foreground ,fg))))
   `(font-latex-match-variable-keywords ((t (:foreground ,fg))))
   `(font-latex-string-face ((t (:foreground "#a9a9a9"))))
   `(font-latex-sectioning-5-face ((t (:foreground ,fg :weight bold))))
   `(font-latex-math-face ((t (:foreground ,fg))))
   `(font-latex-warning-face ((t (:foreground ,fg :weight bold))))
   `(font-latex-sedate-face ((t (:foreground ,fg :weight bold))))
   `(font-latex-sectioning-1-face ((t ,headline-1)))
   `(font-latex-sectioning-2-face ((t ,headline-2)))
   `(font-latex-sectioning-3-face ((t ,headline-3)))
   `(font-latex-sectioning-4-face ((t ,headline-4)))
   `(font-latex-sectioning-5-face ((t ,headline-4)))

   ;; org
   `(org-agenda-date ((t (:foreground ,fg :height 1.2))))
   `(org-agenda-date-today ((t (:foreground ,fg :weight bold :height 1.4))))
   `(org-agenda-date-weekend ((t (:foreground ,fg :weight normal))))
   `(org-agenda-structure ((t (:foreground ,fg :weight bold))))
   `(org-block ((t (:background ,bg-white :foreground ,fg))))
   `(org-block-background ((t (:background ,bg-white))))
   `(org-block-begin-line ((t (:foreground ,fg, :background ,bg-lighter :family ,my-string-family))))
   `(org-block-end-line ((t (:foreground ,fg :background ,bg-lighter :family ,my-string-family))))
   `(org-meta-line ((t (:foreground ,fg :background ,bg-lighter :family ,my-string-family))))
   `(org-code ((t (:foreground ,fg-medium :background ,bg-white :family ,my-string-family))))
   `(org-date ((t (:foreground ,fg) :underline)))
   `(org-hide ((t (:foreground ,bg))))
   `(org-document-title ((t ,headline-1)))
   `(org-document-info ((t (:foreground ,fg))))
   `(org-document-info-keyword ((t (:foreground ,fg-light :family ,my-string-family))))
   `(org-level-1 ((t ,headline-2)))
   `(org-level-2 ((t ,headline-3)))
   `(org-level-3 ((t ,headline-4)))
   `(org-level-4 ((t ,headline-4)))
   `(org-level-5 ((t ,headline-4)))
   `(org-level-6 ((t ,headline-4)))
   `(org-link ((t (:foreground ,fg :underline t))))
   `(org-quote ((t (:foreground ,fg :slant italic :inherit org-block))))
   `(org-scheduled ((t (:foreground ,fg))))
   `(org-sexp-date ((t (:foreground ,fg))))
   `(org-special-keyword ((t (:foreground ,fg))))
   `(org-todo ((t (:foreground ,fg-light :family ,my-string-family))))
   `(org-done ((t (:foreground ,fg-light :family ,my-string-family :strike-through t))))
   `(org-verse ((t (:inherit org-block :slant italic))))
   `(org-table ((t (:foreground ,fg))))
   `(org-formula ((t (:foreground ,fg-light))))

   `(region ((t (:background "#eeeee8" :foreground ,fg))))
   `(slime-repl-inputed-output-face ((t (:foreground ,fg))))
   `(whitespace-line ((t (:background ,bg-highlight-2))))
   `(whitespace-space ((t (:background ,bg :family ,my-comment-family))))
   `(whitespace-newline ((t (:background ,bg :family ,my-comment-family))))
   `(whitespace-empty ((t (:background ,bg :family ,my-comment-family))))
   `(whitespace-trailing ((t (:background ,bg-highlight-2))))

   ;; magit
   `(magit-section-heading ((t (:weight bold :height 1.2))))
   `(magit-branch-local ((t (:weight bold))))
   `(magit-branch-remote ((t (:weight bold))))
   `(magit-branch-current ((t (:weight bold :box (:line-width -1)))))

   ;; markdown
   `(markdown-header-face-1 ((t ,headline-2)))
   `(markdown-header-face-2 ((t ,headline-3)))
   `(markdown-header-face-3 ((t ,headline-4)))
   `(markdown-header-face-4 ((t ,headline-4)))
   `(markdown-header-face-5 ((t ,headline-4)))
   `(markdown-header-face-6 ((t ,headline-4)))
   `(markdown-pre-face ((t (:foreground ,fg-medium :family ,my-string-family))))
   `(markdown-inline-code-face ((t (:foreground ,fg-medium :family ,my-string-family))))

   ;; compile
   `(compilation-error ((t (:inherit error))))

   ;; flycheck
   `(flycheck-error ((t (:inherit error))))
   `(flycheck-warning ((t (:inherit warning))))

   ;; dired
   `(dired-directory ((t (:weight bold))))
   `(dired-subtree-depth-1-face ((t (:background "grey90"))))

   ;; helm
   `(helm-source-header ((t (:foreground ,fg :background "grey90" :weight bold))))
   `(helm-header ((t (:foreground ,fg))))
   `(helm-selection-line ((t (:inherit region :weight bold))))
   `(helm-selection ((t (:background ,bg-highlight))))
   `(helm-ff-directory ((t (:foreground ,fg :weight bold))))
   `(helm-ff-dotted-directory ((t (:foreground ,fg :weight bold))))
   `(helm-ff-symlink ((t (:foreground ,fg :slant italic))))
   `(helm-ff-executable ((t (:foreground ,fg))))

   ;; iedit
   `(iedit-occurrence ((t (:background ,bg-highlight-3 :foreground ,fg))))

   ;; company
   `(company-echo-common ((t (:foreground ,fg))))
   `(company-preview ((t (:background ,bg-overlay))))
   `(company-tooltip ((t (:background ,bg-overlay))))
   `(company-tooltip-selection ((t (:background ,bg-highlight :foreground ,fg))))
   `(company-tooltip-common ((t (:underline t))))
   `(company-tooltip-search ((t (:weight bold))))
   `(company-scrollbar-bg ((t (:background ,bg-overlay))))
   `(company-scrollbar-fg ((t (:background "grey60"))))
   `(company-posframe-metadata ((t (:background ,bg-overlay))))
   `(company-posframe-quickhelp ((t (:background "white"))))

   ;; parens - parenface
   '(parenface-paren-face ((t (:foreground "gray70"))))
   '(parenface-curly-face ((t (:foreground "gray70"))))
   '(parenface-bracket-face ((t (:foreground "gray70"))))

   ;; parens - paren-face
   '(parenthesis ((t (:foreground "gray70"))))

   ;; parens - other
   `(sp-show-pair-match-face ((t (:foreground "black" :weight bold :underline t))))
   `(sp-show-pair-mismatch-face ((t (:background "red" :foreground "black" :weight bold))))
   `(show-paren-match ((t (:foreground "black" :weight bold :underline t))))
   `(show-paren-mismatch ((t (:background "red" :foreground "black" :weight bold))))

   ;; js2
   `(js2-function-param ((t (:foreground ,fg))))
   `(js2-external-variable ((t (:foreground ,fg))))

   ;; perl
   `(cperl-hash-face ((t (:foreground ,fg))))
   `(cperl-array-face ((t (:foreground ,fg))))
   `(cperl-nonoverridable-face ((t (:foreground ,fg))))

   ;; rpm-spec-mode
   `(rpm-spec-tag-face ((t (:inherit default))))
   `(rpm-spec-package-face ((t (:inherit default))))
   `(rpm-spec-macro-face ((t (:inherit default))))
   `(rpm-spec-doc-face ((t (:inherit default))))
   `(rpm-spec-var-face ((t (:inherit default))))
   `(rpm-spec-ghost-face ((t (:inherit default))))
   `(rpm-spec-section-face ((t (:inherit default :weight bold))))

   ;; misc
   `(sh-quoted-exec ((t (:foreground ,fg-medium))))
   `(idle-highlight ((t (:background ,bg-highlight))))
   `(yas-field-highlight-face ((t (:background "#eeeee8" :foreground ,fg))))
   `(eshell-prompt ((t (:foreground ,fg :weight bold))))
   `(cider-result-overlay-face ((t (:weight bold))))))

(enable-theme 'typo)

;; make org-mode fontify source code
(setq org-src-fontify-natively t)
(setq org-src-preserve-indentation t)

;; enable column number in info area
(column-number-mode t)

(global-display-line-numbers-mode t)

;; Allow quotes in org source blocks
(setq org-emphasis-regexp-components '(" \t('\"{" "- \t.,:!?;'\")}\\" " \t\r\n," "." 1))

;; store backup files where they don't bother me
(setq backup-directory-alist '(("." . "~/.emacs.d/backups/")))
;; don't create #autosave-files#
(setq auto-save-default nil)
;; don't create .#files
(setq create-lockfiles nil)

;; allow org-mode to use alphabetical lists
(setq org-list-allow-alphabetical t)

(autoload 'ox-html "org-mode" "Org Mode." t)
(autoload 'ox-rss "org-mode" "Org Mode." t)
(autoload 'ox-publish "org-mode" "Org Mode." t)

;; Set up blogging in Emacs

(setq org-static-blog-publish-title "bastibe.de")
(setq org-static-blog-publish-url "https://bastibe.de/")
(setq org-static-blog-publish-directory ".")
(setq org-static-blog-posts-directory "posts/")
(setq org-static-blog-drafts-directory "drafts/")
(setq org-static-blog-enable-tags t)
(setq org-static-blog-no-comments-tag "nocomments")
(setq org-export-with-toc nil)
(setq org-export-with-section-numbers nil)

(defun with-c-locale (orig-fun &rest args)
  (let ((system-time-locale "C")) (apply orig-fun args)))
(advice-add 'org-static-blog-publish :around #'with-c-locale)

(setq org-static-blog-page-header
"<meta name=\"author\" content=\"Bastian Bechtold\">
<meta name=\"referrer\" content=\"no-referrer\">
<link href= \"static/style.css\" rel=\"stylesheet\" type=\"text/css\" />
<link rel=\"icon\" href=\"static/favicon.ico\">
<link rel=\"apple-touch-icon-precomposed\" href=\"static/favicon-152.png\">
<link rel=\"msapplication-TitleImage\" href=\"static/favicon-144.png\">
<link rel=\"msapplication-TitleColor\" href=\"#0141ff\">
<script src=\"static/katex.min.js\"></script>
<script src=\"static/auto-render.min.js\"></script>
<script src=\"static/lightbox.js\"></script>
<link rel=\"stylesheet\" href=\"static/katex.min.css\">
<script>document.addEventListener(\"DOMContentLoaded\", function() { renderMathInElement(document.body); });</script>
<meta http-equiv=\"content-type\" content=\"application/xhtml+xml; charset=UTF-8\">
<meta name=\"viewport\" content=\"initial-scale=1,width=device-width,minimum-scale=1\">")

(setq org-static-blog-page-preamble
"<div class=\"header\">
  <a href=\"https://bastibe.de\">Basti's Scratchpad on the Internet</a>
  <div class=\"sitelinks\">
    <a href=\"https://github.com/bastibe\">Github</a> | <a href=\"https://bastibe.de/projects.html\">Projects</a> | <a href=\"https://bastibe.de/uses.html\">Uses</a> | <a href=\"https://bastibe.de/reviews.html\">Reviews</a> | <a href=\"https://bastibe.de/about.html\">About</a>
  </div>
</div>")

(setq org-static-blog-page-postamble
"<div id=\"archive\">
  <a href=\"https://bastibe.de/archive.html\">Other posts</a>
</div>
<center><a rel=\"license\" href=\"https://creativecommons.org/licenses/by-sa/3.0/\"><img alt=\"Creative Commons License\" style=\"border-width:0\" src=\"https://i.creativecommons.org/l/by-sa/3.0/88x31.png\" /></a><br /><span xmlns:dct=\"https://purl.org/dc/terms/\" href=\"https://purl.org/dc/dcmitype/Text\" property=\"dct:title\" rel=\"dct:type\">bastibe.de</span> by <a xmlns:cc=\"https://creativecommons.org/ns#\" href=\"https://bastibe.de\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">Bastian Bechtold</a> is licensed under a <a rel=\"license\" href=\"https://creativecommons.org/licenses/by-sa/3.0/\">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.</center>")

(setq org-static-blog-post-comments
"<script async src=\"https://talk.hyvor.com/embed/embed.js\" type=\"module\"></script>
<hyvor-talk-comments id=\"hyvorcomments\" website-id=\"3390\" page-id=\"\"></hyvor-talk-comments>
<script type=\"text/javascript\">
    document.getElementById(\"hyvorcomments\").setAttribute(\"page-id\", location.pathname);
</script>")

(defadvice org-preview-latex-fragment (around non-xelatex-org-preview-latex-fragment)
  "Strip down the LaTeX process to the bare minimum when compiling fragments"
  (let ((org-latex-default-packages-alist
        '((""     "amsmath"   t)
          (""     "amssymb"   t)))
        (org-latex-pdf-process
         '("xelatex -shell-escape -interaction nonstopmode -output-directory %o %f")))
       ad-do-it))
(ad-activate 'org-preview-latex-fragment)

;; This slows down org-publish to a crawl, and it is not needed since
;; I use magit anyway.
(remove-hook 'find-file-hooks 'vc-find-file-hook)

