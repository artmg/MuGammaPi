2023-05-03-raspios-bullseye-arm64-lite.img.xz

$ uname -a
Linux PiStuff4 6.1.21-v8+ #1642 SMP PREEMPT Mon Apr  3 17:24:16 BST 2023 aarch64 GNU/Linux

$ lsb_release -a
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux 11 (bullseye)
Release:	11
Codename:	bullseye

$ dpkg --get-selections > dpkg-selections.txt

install:

adduser
alsa-topology-conf
alsa-ucm-conf
alsa-utils
apt
apt-listchanges
apt-utils
avahi-daemon
base-files
base-passwd
bash
bash-completion
bind9-host
bind9-libs:arm64
binutils
binutils-aarch64-linux-gnu
binutils-common:arm64
bluez
bluez-firmware
bsdextrautils
bsdutils
build-essential
busybox
bzip2
ca-certificates
cifs-utils
console-setup
console-setup-linux
coreutils
cpio
cpp
cpp-10
crda
cron
curl
dash
dbus
dc
debconf
debconf-i18n
debconf-utils
debian-archive-keyring
debianutils
device-tree-compiler
dhcpcd5
diffutils
dirmngr
distro-info-data
dmidecode
dmsetup
dns-root-data
dnsmasq-base
dos2unix
dosfstools
dphys-swapfile
dpkg
dpkg-dev
e2fsprogs
ed
eject
ethtool
exfatprogs
fake-hwclock
fakeroot
fbset
fdisk
file
findutils
firmware-atheros
firmware-brcm80211
firmware-libertas
firmware-misc-nonfree
firmware-realtek
flashrom
fontconfig-config
fonts-dejavu-core
fuse
g++
g++-10
gcc
gcc-10
gcc-10-base:arm64
gcc-9-base:arm64
gdb
gdisk
gettext-base
gnupg
gnupg-l10n
gnupg-utils
gpg
gpg-agent
gpg-wks-client
gpg-wks-server
gpgconf
gpgsm
gpgv
grep
groff-base
gzip
hardlink
hostname
htop
ifupdown
init
init-system-helpers
initramfs-tools
initramfs-tools-core
iproute2
iptables
iputils-ping
isc-dhcp-client
isc-dhcp-common
iso-codes
iw
kbd
keyboard-configuration
keyutils
klibc-utils
kmod
kms++-utils
less
libacl1:arm64
libalgorithm-diff-perl
libalgorithm-diff-xs-perl
libalgorithm-merge-perl
libapparmor1:arm64
libapt-pkg6.0:arm64
libargon2-1:arm64
libasan6:arm64
libasound2:arm64
libasound2-data
libassuan0:arm64
libatasmart4:arm64
libatomic1:arm64
libatopology2:arm64
libattr1:arm64
libaudit-common
libaudit1:arm64
libavahi-common-data:arm64
libavahi-common3:arm64
libavahi-core7:arm64
libbabeltrace1:arm64
libbinutils:arm64
libblas3:arm64
libblkid1:arm64
libblockdev-crypto2:arm64
libblockdev-fs2:arm64
libblockdev-loop2:arm64
libblockdev-part-err2:arm64
libblockdev-part2:arm64
libblockdev-swap2:arm64
libblockdev-utils2:arm64
libblockdev2:arm64
libbluetooth3:arm64
libboost-filesystem1.74.0:arm64
libboost-program-options1.74.0:arm64
libboost-regex1.74.0:arm64
libbpf0:arm64
libbrotli-dev:arm64
libbrotli1:arm64
libbsd0:arm64
libbz2-1.0:arm64
libc-bin
libc-dev-bin
libc-devtools
libc-l10n
libc6:arm64
libc6-dbg:arm64
libc6-dev:arm64
libcamera-apps-lite
libcamera0:arm64
libcap-ng0:arm64
libcap2:arm64
libcap2-bin
libcbor0:arm64
libcc1-0:arm64
libcom-err2:arm64
libcrypt-dev:arm64
libcrypt1:arm64
libcryptsetup12:arm64
libctf-nobfd0:arm64
libctf0:arm64
libcurl3-gnutls:arm64
libcurl4:arm64
libdaemon0:arm64
libdb5.3:arm64
libdbus-1-3:arm64
libdebconfclient0:arm64
libdebuginfod1:arm64
libdeflate0:arm64
libdevmapper1.02.1:arm64
libdns-export1110
libdpkg-perl
libdrm-common
libdrm2:arm64
libdvdread8:arm64
libdw1:arm64
libebml5:arm64
libedit2:arm64
libelf1:arm64
libestr0:arm64
libevent-2.1-7:arm64
libexif12:arm64
libexpat1:arm64
libext2fs2:arm64
libfakeroot:arm64
libfastjson4:arm64
libfdisk1:arm64
libfdt1:arm64
libffi7:arm64
libfftw3-single3:arm64
libfido2-1:arm64
libfile-fcntllock-perl
libflac8:arm64
libfmt7:arm64
libfontconfig1:arm64
libfreetype-dev:arm64
libfreetype6:arm64
libfreetype6-dev:arm64
libfstrm0:arm64
libftdi1-2:arm64
libfuse2:arm64
libgcc-10-dev:arm64
libgcc-s1:arm64
libgcrypt20:arm64
libgd3:arm64
libgdbm-compat4:arm64
libgdbm6:arm64
libgfortran5:arm64
libglib2.0-0:arm64
libgmp10:arm64
libgnutls30:arm64
libgomp1:arm64
libgpg-error0:arm64
libgpgme11:arm64
libgssapi-krb5-2:arm64
libgstreamer-plugins-base1.0-0:arm64
libgstreamer1.0-0:arm64
libgudev-1.0-0:arm64
libhogweed6:arm64
libicu67:arm64
libidn2-0:arm64
libimagequant0:arm64
libip4tc2:arm64
libip6tc2:arm64
libisc-export1105:arm64
libisl23:arm64
libitm1:arm64
libiw30:arm64
libjansson4:arm64
libjbig0:arm64
libjim0.79:arm64
libjpeg62-turbo:arm64
libjson-c5:arm64
libk5crypto3:arm64
libkeyutils1:arm64
libklibc:arm64
libkmod2:arm64
libkms++0:arm64
libkrb5-3:arm64
libkrb5support0:arm64
libksba8:arm64
liblapack3:arm64
liblcms2-2:arm64
libldap-2.4-2:arm64
libldap-common
liblmdb0:arm64
liblocale-gettext-perl
liblognorm5:arm64
liblsan0:arm64
libluajit-5.1-2:arm64
libluajit-5.1-common
liblz4-1:arm64
liblzma5:arm64
libmagic-mgc
libmagic1:arm64
libmatroska7:arm64
libmaxminddb0:arm64
libmbim-glib4:arm64
libmbim-proxy
libmd0:arm64
libmm-glib0:arm64
libmnl0:arm64
libmount1:arm64
libmpc3:arm64
libmpdec3:arm64
libmpfr6:arm64
libmtp-common
libmtp-runtime
libmtp9:arm64
libncurses6:arm64
libncursesw6:arm64
libndp0:arm64
libnetfilter-conntrack3:arm64
libnettle8:arm64
libnewt0.52:arm64
libnfnetlink0:arm64
libnfsidmap2:arm64
libnftables1:arm64
libnftnl11:arm64
libnghttp2-14:arm64
libnl-3-200:arm64
libnl-genl-3-200:arm64
libnl-route-3-200:arm64
libnm0:arm64
libnpth0:arm64
libnsl-dev:arm64
libnsl2:arm64
libnspr4:arm64
libnss-mdns:arm64
libnss3:arm64
libntfs-3g883
libogg0:arm64
liborc-0.4-0:arm64
libp11-kit0:arm64
libpam-chksshpwd:arm64
libpam-modules:arm64
libpam-modules-bin
libpam-runtime
libpam-systemd:arm64
libpam0g:arm64
libparted-fs-resize0:arm64
libparted2:arm64
libpcap0.8:arm64
libpci3:arm64
libpcre2-8-0:arm64
libpcre2-posix2:arm64
libpcre3:arm64
libpcsclite1:arm64
libperl5.32:arm64
libpipeline1:arm64
libpng-dev:arm64
libpng-tools
libpng16-16:arm64
libpolkit-agent-1-0:arm64
libpolkit-gobject-1-0:arm64
libpopt0:arm64
libprocps8:arm64
libprotobuf-c1:arm64
libpsl5:arm64
libpugixml1v5:arm64
libpython3-stdlib:arm64
libpython3.9:arm64
libpython3.9-minimal:arm64
libpython3.9-stdlib:arm64
libqmi-glib5:arm64
libqmi-proxy
libraspberrypi-bin
libraspberrypi-dev
libraspberrypi-doc
libraspberrypi0:arm64
libreadline8:arm64
librtmp1:arm64
libsamplerate0:arm64
libsasl2-2:arm64
libsasl2-modules:arm64
libsasl2-modules-db:arm64
libseccomp2:arm64
libselinux1:arm64
libsemanage-common
libsemanage1:arm64
libsepol1:arm64
libslang2:arm64
libsmartcols1:arm64
libsource-highlight-common
libsource-highlight4v5
libsqlite3-0:arm64
libss2:arm64
libssh2-1:arm64
libssl1.1:arm64
libstdc++-10-dev:arm64
libstdc++6:arm64
libsystemd0:arm64
libtalloc2:arm64
libtasn1-6:arm64
libteamdctl0:arm64
libtevent0:arm64
libtext-charwidth-perl
libtext-iconv-perl
libtext-wrapi18n-perl
libtiff5:arm64
libtinfo6:arm64
libtirpc-common
libtirpc-dev:arm64
libtirpc3:arm64
libtsan0:arm64
libturbojpeg0:arm64
libubsan1:arm64
libuchardet0:arm64
libudev1:arm64
libudisks2-0:arm64
libunistring2:arm64
libunwind8:arm64
libusb-1.0-0:arm64
libuuid1:arm64
libuv1:arm64
libv4l-0:arm64
libv4l2rds0:arm64
libv4lconvert0:arm64
libvolume-key1
libvorbis0a:arm64
libwbclient0:arm64
libwebp6:arm64
libwebpdemux2:arm64
libwebpmux3:arm64
libwrap0:arm64
libx11-6:arm64
libx11-data
libxau6:arm64
libxcb1:arm64
libxdmcp6:arm64
libxext6:arm64
libxml2:arm64
libxmuu1:arm64
libxpm4:arm64
libxtables12:arm64
libxxhash0:arm64
libyaml-0-2:arm64
libzstd1:arm64
linux-base
linux-libc-dev:arm64
locales
login
logrotate
logsave
lsb-base
lsb-release
lua5.1
luajit
mailcap
make
man-db
manpages
manpages-dev
mawk
media-types
mime-support
mksh
mkvtoolnix
modemmanager
mount
nano
ncdu
ncurses-base
ncurses-bin
ncurses-term
net-tools
netbase
network-manager
nfs-common
nftables
ntfs-3g
openresolv
openssh-client
openssh-server
openssh-sftp-server
openssl
p7zip
p7zip-full
parted
passwd
patch
pci.ids
pciutils
perl
perl-base
perl-modules-5.32
pi-bluetooth
pigz
pinentry-curses
pkg-config
policykit-1
ppp
procps
psmisc
publicsuffix
python-apt-common
python-is-python3
python3
python3-apt
python3-certifi
python3-chardet
python3-colorzero
python3-debconf
python3-distro
python3-gpiozero
python3-idna
python3-kms++
python3-libcamera
python3-minimal
python3-numpy
python3-picamera2
python3-pidng
python3-piexif
python3-pil:arm64
python3-pkg-resources
python3-prctl
python3-requests
python3-rpi.gpio
python3-simplejpeg
python3-six
python3-spidev
python3-toml
python3-urllib3
python3-v4l2
python3.9
python3.9-minimal
raspberrypi-archive-keyring
raspberrypi-bootloader
raspberrypi-kernel
raspberrypi-net-mods
raspberrypi-sys-mods
raspi-config
raspi-gpio
raspi-utils
raspinfo
readline-common
rfkill
rng-tools
rng-tools-debian
rpcbind
rpi-eeprom
rpi-update
rpi.gpio-common:arm64
rsync
rsyslog
runit-helper
sed
sensible-utils
ssh
ssh-import-id
strace
sudo
systemd
systemd-sysv
systemd-timesyncd
sysvinit-utils
tar
tasksel
tasksel-data
triggerhappy
tzdata
ucf
udev
udisks2
unzip
usb-modeswitch
usb-modeswitch-data
usbutils
userconf-pi
util-linux
v4l-utils
vim-common
vim-tiny
wget
whiptail
wireless-regdb
wireless-tools
wpasupplicant
xauth
xkb-data
xxd
xz-utils
zip
zlib1g:arm64
zlib1g-dev:arm64
