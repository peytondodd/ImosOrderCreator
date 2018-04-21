#google maps confirm location.
import webbrowser
starturl = "https://www.google.co.in/maps/place/"
addarr = raw_input("Enter the name of the place: ").split(' ')

answer = starturl
for i in range(0,len(addarr)):
	if (i!=len(addarr)-1):
		answer = answer + addarr[i] + '+'
	else:
		answer = answer + addarr[i]

print answer
webbrowser.open(answer)