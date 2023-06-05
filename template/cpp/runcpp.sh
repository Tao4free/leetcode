make main

run() {
    echo 
    echo "Case: ${1%.*}"
    ./main < $1
}

if [[ $# -eq 0 ]] ; then
    for f in example_*.in
    do
        run $f
    done
    exit 0
else
    for f in "$@"
    do
        run $f
    done
fi
