#!/bin/bash

function conf_template(){
    POSITIONAL=()
    while [[ $# -gt 0 ]]
    do
    key="$1"

    case $key in
        -t|--template )
        template="$2"
        shift # past argument
        shift # past value
        ;;
        -r|--result )
        result="$2"
        shift # past argument
        shift # past value
        ;;
        *)    # unknown option
        _echoerr "Unknown option: $1"
        # should add exit code
        shift # past argument
        exit 1
        ;;
    esac
    done
    set -- "${POSITIONAL[@]}"

# Check parameters
if	[[ -z $template ]] || [[ -z $result ]]; then
	echo "Not enough options. Necessary 2."; exit
fi
if	[[ ! -f $template ]]; then
	echo "$template is not a template file."; exit
fi

# Create result file from template
regex='\{\%*([0-9A-Za-z_\-]+)*\%\}*'

cat $template | while read line; do

    while [[ "$line" =~ $regex ]]; do
        param="${BASH_REMATCH[1]}"
        line=${line//${BASH_REMATCH[0]}/${!param}}   
    done
    echo $line >> $result
done
}

if [ "${0}" == "./task1.sh" ]; then
    conf_template "${@}"
fi