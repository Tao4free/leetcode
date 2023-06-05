# Reference:
# 1. https://qiita.com/granddaifuku/items/c26b58b89d73b4a3de98
# 2. https://apple.stackexchange.com/questions/99077/how-to-set-gcc-4-8-as-default-gcc-compiler/99157#99157
# 3. https://stackoverflow.com/questions/17583578/what-command-means-do-nothing-in-a-conditional-in-bash
# 4. https://stackoverflow.com/questions/20802320/detect-if-homebrew-package-is-installed/20802425
# 5. https://linuxize.com/post/bash-heredoc/
if brew ls --versions gcc > /dev/null; then
    :
else
    brew install gcc > /dev/null 2>&1 || brew upgrade gcc > /dev/null 2>&1
fi
VER=$( brew info --json gcc | jq -r '.[0].aliases[0] | split("@") | .[1]' )

cat << EOF
To use gcc,

Step1:
Add below alias in ~/.bashrc
alias gcc="gcc-$VER"
alias cc="gcc-$VER"
alias g++="g++-$VER"
alias c++="c++-$VER"
alias gfortran="gfortran-$VER"

Step2:
Run command below to make alias work
source ~/.bashrc
EOF
