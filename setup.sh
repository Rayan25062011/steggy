RS="\033[0;31m"
YS="\033[1;33m"
CE="\033[0m"


#color end
CE="\033[0m"
#red start
RS="\033[0;31m"
#green start
GN="\033[0;32m"
#white start
WHS="\033[0m"

echo -e ""$GN"["$RS"+"$GN"]"$CE" Installing requirments"$C""
{
apt-get pip
apk add pip
pip install os sys time
} &> /dev/null

}
sleep 1
echo -e ""$GN"["$RS"+"$GN"]"$CE" Requierments successfully installed!"$C""
sleep 1
