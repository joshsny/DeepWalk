(TeX-add-style-hook
 "essay"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper")))
   (TeX-run-style-hooks
    "latex2e"
    "header"
    "titlepage"
    "article"
    "art10"
    "tkz-graph"
    "thm-restate"
    "algpseudocode"
    "algorithm")
   (TeX-add-symbols
    "shadow"
    "D"
    "G"
    "V"
    "rar"
    "lar"
    "npart"
    "ntitle"
    "ndate"
    "SO")
   (LaTeX-add-labels
    "roy's loop")
   (LaTeX-add-bibliographies
    "references")
   (LaTeX-add-thmrestate-restatable-macros
    "MainDeepWalk"))
 :latex)

