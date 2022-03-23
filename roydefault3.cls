% !TEX TS-program = xelatex
% !TEX encoding = UTF-8 Unicode
% \ProvidesClass{classname}[2017/02/27 notes]
\documentclass[10pt]{article}%__________________________________________________________________Page geometry
% \usepackage[letterpaper,margin=0.6in,marginratio=3:5,twoside]{geometry}
\usepackage[a4paper,margin=15mm,marginratio=3:5,twoside]{geometry}
% \usepackage[a5paper,margin=13mm]{geometry}
%\usepackage[letterpaper,margin=0.6in,marginratio=3:5,twoside]{geometry}
% \usepackage[paperwidth=5.5in, paperheight=8.5in, margin=13mm]{geometry}
% \usepackage{relsize}
% \relscale{0.3} % or whatever scaling is desired
%\geometry{landscape} % sets the page to landscape orientation

%\usepackage{ulem}
% \usepackage{fancyhdr} % This should be set AFTER setting up the page geometry
%\pagestyle{fancyplain} % options: empty , plain , fancy
%_____________________________________________________________________MATH STUFF
\usepackage{amsmath,amssymb,amsopn}% read amsldoc.pdf for more details
\usepackage{fontspec}
\usepackage{unicode-math}
%\DeclareMathOperator{\}{}
\DeclareMathOperator{\arccot}{arccot}
\DeclareMathOperator{\arcsec}{arcsec}
\DeclareMathOperator{\arccsc}{arccsc}
\DeclareMathOperator{\sech}{sech}
\DeclareMathOperator{\csch}{csch}
\DeclareMathOperator{\arcsinh}{arcsinh}
\DeclareMathOperator{\arccosh}{arccosh}
\DeclareMathOperator{\arctanh}{arctanh}
\DeclareMathOperator{\arccoth}{arccoth}
\DeclareMathOperator{\arcsech}{arcsech}
\DeclareMathOperator{\arccsch}{arccsch}
%\DeclareMathOperator{\min}{min}
%\DeclareMathOperator{\max}{max}
%____macros to make quick note taking easier all escapes under 3 chars
\def\t{\text }
\def\parti{\partial}
\def\o{\over}
\def\({\left( }
\def\){\right) }
\def\[{\left[ }
\def\]{\right] }
% \def\l{\left. }
% \def\r{\right. }
%\usepackage{leqno}
%__________________________________________________________________Font settings
% \usepackage[scaled=.92]{helvet}
% \usepackage{times}
% \usepackage{morefloats}
\usepackage{xcolor}
\usepackage{titlesec}
% \defaultfontfeatures{Ligatures=TeX}
\setsansfont{NotoSans-Light.ttf} % Set sans serif font
% \setsansfont{DejaVu Sans, ExtraLight} % Set sans serif font
% \setsansfont{DejaVu Sans ExtraLight}
% [    Extension = .ttf,
%    UprightFont = *,
%       BoldFont = *-Bold,
%     ItalicFont = *-Italic,
% BoldItalicFont = *-BoldItalic,
% ]
% \setmainfont{Latin Modern Math} % Set serifed font
% \setmainfont{DejaVu Math TeX Gyre} % Set serifed font
\setmainfont{XITS} %#/usr/share/texlive/texmf-dist/fonts/opentype
[    Extension = .otf,
   UprightFont = *-Regular,
      BoldFont = *-Bold,
    ItalicFont = *-Italic,
BoldItalicFont = *-BoldItalic,
]
\setmathfont{XITSMath-Regular}
[    Extension = .otf,
      BoldFont = XITSMath-Bold,
]
% \setmathfont{Latin Modern Math} % Set serifed font

% Define light and dark Microsoft blue colours
\definecolor{MSBlue}{rgb}{.204,.353,.541}
\definecolor{MSLightBlue}{rgb}{.31,.506,.741}
\definecolor{PitchBlack}{rgb}{.0,.0,.0}

% Define a new fontfamily for the subsubsection font
% Don't use \fontspec directly to change the font
% \newfontfamily\subsubsectionfont[Color=MSLightBlue]{DejaVu Math TeX Gyre}
% Set formats for each heading level

\titleformat*{\section}{\Large\bfseries\sffamily\color{PitchBlack}}
\titleformat*{\subsection}{\Large\bfseries\sffamily\color{PitchBlack}}
\titleformat*{\subsubsection}{\Large\bfseries\sffamily\color{PitchBlack}}
% \titleformat*{\subsection}{\large\bfseries\sffamily\color{MSLightBlue}}
% \titleformat*{\subsubsection}{\itshape\subsubsectionfont}

%______________________________Multicol http://tex.stackexchange.com/a/3987/1244
\usepackage{multicol}
\usepackage{ifthen}
% \let\oldsection\section
% \renewcommand*{\section}[1]{%
%     \ifthenelse{\equal{\@currenvir}{multicols}}{\end{multicols}}{}
%     \ifthenelse{\thesection = 0}{}{\end{multicols}}%
%     \begin{multicols}{2}[\oldsection{#1}]}
% \let\oldsubsection\subsection
% \renewcommand*{\subsection}[1]{%
%     \ifthenelse{\thesubsection = 0}{}{\end{multicols}}%
%     \begin{multicols}{2}[\oldsubsection{#1}]}
% \let\oldend\enddocument
% \renewcommand*{\enddocument}{\end{multicols}\oldend}

