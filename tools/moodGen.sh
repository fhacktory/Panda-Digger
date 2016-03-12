#!/bin/sh
#Moodbar generation

usage()
{
    echo "Usage: ${0} file1 [file2 ...]" > /dev/stderr
    echo "Generates a moodbat for a given file" > /dev/stderr
}

if [ $# -lt 1 ]
then
    usage
    exit 1
fi

ret=0

#Looping over argunents
for file in "$@"
do
    ext="${file:(-4)}"
    if [ "${ext}" == ".mp3" ]
    then
	#Creating output name and call to moodbar application
	output="${file%mp3}mood"
	moodbar "${file}" -o "${output}"
	ret=$?
	if [ $ret -ne 0 ]
	then
	    break
	fi
    else
	echo "${file}: Not a mp3 file" > /dev/stderr
    fi
done

exit ${ret}
