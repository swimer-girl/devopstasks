BEGIN { print "Вывод результатов" }
{
    array = int($0/10) 
    cnt[array]++
}
END {
    for (array=0; array<=9; array++) {
        view = sprintf("%*s",100*cnt[array]/FNR,"")
        gsub(" ","*",view)
		last = first + 9
        printf "%2d - %2d: %3d%% %-s\n", first, last, 100*cnt[array]/FNR, view
        first = last + 1
    }
	view1 = sprintf("%*s",100*cnt[array]/FNR,"")
	gsub(" ","*",view1)
	printf "100:     %3d%% %s\n", 100*cnt[array]/FNR, view1
}