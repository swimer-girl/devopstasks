BEGIN { print "Вывод результатов" }
{
    array = int($0/10)
    count[array]++
}
END {
    for (array=0; array<=9; array++) {
        view = sprintf("%*s",count[array],"")
        gsub(" ","*",view)
		last = first + 9
        printf "%2d - %2d: %3d %-s\n", first, last, count[array], view
        first = last + 1
    }
	view1 = sprintf("%*s",count[array],"")
	gsub(" ","*",view1)
	printf "100:     %3d %s\n", count[array], view1
}
