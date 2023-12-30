# 2023-12-30 18:56:22 by cmdshell 7.12.1
# software id = 
#
/routing filter rule
add chain=bgp_rule comment=mobile-cn disabled=no rule=\
    "if ( bgp-communities equal 100:100) {set gw *0x14; accept}"
add chain=bgp_rule comment=unicom-cn disabled=no rule=\
    "if ( bgp-communities equal 200:200) {set gw *0x1c; accept}"
add chain=bgp_rule comment=telecom-cn disabled=no rule="if ( bgp-communities e\
    qual 300:300) {set gw *0x6;set distance -20; accept}"
add chain=bgp_rule comment=aliyun-cn disabled=no rule="if ( bgp-communities eq\
    ual 400:400) {set gw *0x6;set distance -10; accept}"
add chain=bgp_rule comment="default telecom" disabled=no rule=\
    "if (protocol bgp) {set gw *0x6; accept}"
add chain=bgp_rule comment="google service" disabled=yes rule=\
    "if (bgp-as-path 15169) {set gw 192.168.100.3; accept}"
add chain=bgp_rule comment=github disabled=yes rule=\
    "if (bgp-as-path 36459) {set gw 192.168.100.3; accept}"
add chain=bgp_rule comment=telegram disabled=yes rule=\
    "if (bgp-as-path 62041\$|59930\$) {set gw 192.168.100.3; accept}"
