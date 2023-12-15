window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages : {'[+]' : ['html']}  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
  loader : { load : ['[tex]/html']}
};

document$.subscribe(() => { 
  MathJax.typesetPromise()
})

