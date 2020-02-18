#!/bin/bash

function conf_template(){
template=$1
result=$2

# Check parameters
if	[ -z "$template" ] || [ -z $result ]; then
	echo "Not enough options. Necessary 2."; exit
fi
if	[ ! -f "$template" ]; then
	echo "$template is not a template file."; exit
fi
if	[ ! -f "$result" ]; then
	echo "$result is not a file."; exit
fi

# Create result file from template
regex='\$\{([a-zA-Z_][a-zA-Z_0-9]*)\}'
cat $template | while read line; do
    while [[ "$line" =~ $regex ]]; do
        param="${BASH_REMATCH[1]}"
        line=${line//${BASH_REMATCH[0]}/${!param}}
    done
    echo $line >> $result
done
}

if [ "${1}" == "task1.sh" ]; then
    conf_template "${@}"
fi