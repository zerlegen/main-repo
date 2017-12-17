###############################################################
# files/directories
## chmod
## chown

# tmux

# networking
## ip
## ifconfig
## nmap
## netstat
## ethtool
## iw
## ss
## host
## whois
## dig
## tcpdump
## ping

# crypto
## base64
## openssl
## gpg

# archives
## tar
## 7z
## gpg
## bzip2
## zip

# http/web
## wget
## curl

# media 
## ffmpeg
## sox

# processes
## ps
## top
## strace
## lsof
## watch

# disks
## mount
## du/df
## fdisk

# remote systems
## scp
## ssh

# misc
## tr
## seq
## sort
## join
## printf
## cal
## date
## mkisofs
## cdparanoia
## uname
## udevadm
## lspci
## lsusb
## dmidecode
## smartctl
## hdparm
## badblocks
## git
## find
## fg
## bg
## rev
## fmt
## locate
## free

## dpkg
## rpm
## apt


# logging
## /var/log/messages


###############################################################
# Filesystem

FILES_LIST_ALL="ls -alh"
FILES_MOVE="mv"
FILES_RENAME="mv"
FILES_COPY="cp"
FILES_COPY_TREE="cp -R"

FILES_REMOVE_TREE="rm -rf"

DIR_CHANGE="cd"
DIR_CREATE="mkdir"
DIR_CREATE_TREE="mkdir -p"

LINK_SYM_CREATE="ln -s"



alias files-list-all="$FILES_LIST_ALL"
alias files-show-all="$FILES_SHOW_ALL"
alias files-move="$FILES_MOVE"
alias files-rename="$FILES_RENAME"
alias files-copy="$FILES_COPY"
alias files-copy-tree="$FILES_COPY_TREE"
alias files-remove-tree="$FILES_REMOVE_TREE"

alias link-sym-create_loc_name="$LINK_SYM_CREATE"

alias desc-files-list-all="echo $FILES_LIST_ALL"
alias desc-files-move="echo $FILES_MOVE"
alias desc-files-rename="echo $FILES_RENAME"
alias desc-files-copy="echo $FILES_COPY"
alias desc-files-copy-tree="echo $FILES_COPY_TREE"
alias desc-files-remove-tree="echo $FILES_REMOVE_TREE"


###############################################################
# Tmux

TMUX_NEW_SESSION_NAME="tmux new -s"
TMUX_KILL_SESSION_NAME="tmux kill-session -t"
TMUX_SHOW_SESSIONS="tmux ls"
TMUX_ATTACH_LAST="tmux at"
TMUX_ATTACH_SESSION_NAME="tmux at -t"
TMUX_DETACH="tmux detach"
TMUX_RENAME_SESSION_CURRENT_NEW="tmux rename-session -t"
TMUX_NEW_WINDOW="tmux new-window"
TMUX_PREVIOUS_WINDOW="tmux previous-window"
TMUX_NEXT_WINDOW="tmux next-window"
TMUX_SPLIT_WINDOW_TOP_BOTTOM="tmux split-window -v"
TMUX_SPLIT_WINDOW_LEFT_RIGHT="tmux split-window -h"
TMUX_LAST_PANE="tmux last-pane"

DESC_TMUX_PREVIOUS_SESSION="ctrl-b \("
DESC_TMUX_NEXT_SESSION="ctrl-b \)"
DESC_TMUX_LAST_PANE="ctrl-b o"

alias tmux-new-session_name="$TMUX_NEW_SESSION_NAME"
alias tmux-show-sessions="$TMUX_SHOW_SESSIONS"
alias tmux-kill-session_name="$TMUX_KILL_SESSION_NAME"
alias tmux-attach-last="$TMUX_ATTACH_LAST"
alias tmux-attach-session_name="$TMUX_ATTACH_SESSION_NAME"

alias tmux-detach="$TMUX_DETACH"
alias tmux-rename-session_current_new="$TMUX_RENAME_SESSION_CURRENT_NEW"

alias tmux-new-window="$TMUX_NEW_WINDOW"
alias tmux-previous-window="$TMUX_PREVIOUS_WINDOW"
alias tmux-next-window="$TMUX_NEXT_WINDOW"

alias tmux-split-window-top-bottom="$TMUX_SPLIT_WINDOW_TOP_BOTTOM"
alias tmux-split-window-left-right="$TMUX_SPLIT_WINDOW_LEFT_RIGHT"

alias tmux-switch-pane="$TMUX_LAST_PANE"

alias desc-tmux-new-session_name="echo $TMUX_NEW_SESSION_NAME"
alias desc-tmux-show-sessions="echo $TMUX_SHOW_SESSIONS"
alias desc-tmux-kill-session_name="echo $TMUX_KILL_SESSION_NAME"
alias desc-tmux-rename-window="echo $DESC_TMUX_RENAME_WINDOW"
alias desc-tmux-attach-session_name="echo $TMUX_ATTACH_SESSION_NAME"
alias desc-tmux-attach-last="echo $TMUX_ATTACH_LAST"
alias desc-tmux-detach="echo $TMUX_DETACH"
alias desc-tmux-rename-session_current_new="echo $TMUX_RENAME_SESSION_CURRENT_NEW"

alias desc-tmux-previous-session="echo ${DESC_TMUX_PREVIOUS_SESSION}"
alias desc-tmux-next-session="echo ${DESC_TMUX_NEXT_SESSION}"

alias desc-tmux-new-window="echo $TMUX_NEW_WINDOW"
alias desc-tmux-previous-window="echo $TMUX_PREVIOUS_WINDOW"
alias desc-tmux-next-window="echo $TMUX_NEXT_WINDOW"

alias desc-tmux-split-window-top-bottom="echo $TMUX_SPLIT_WINDOW_TOP_BOTTOM"
alias desc-tmux-split-window-left-right="echo $TMUX_SPLIT_WINDOW_LEFT_RIGHT"
alias desc-tmux-switch-pane="echo $DESC_TMUX_LAST_PANE"


###############################################################
# Linux

LINUX_MODULES_SHOW="lsmod"
LINUX_MODULE_INFO_NAME="modinfo"

alias linux-modules-show=$LINUX_MODULES_SHOW
alias linux-module-info_name=$LINUX_MODULE_INFO_NAME

alias desc-linux-modules-show="echo $LINUX_MODULES_SHOW"
alias desc-linux-module-info_name="echo $LINUX_MODULE_INFO_NAME"

###############################################################
# Disks

DISK_FREE_SPACE="df -h"
DISK_USAGE_DIR="du -cksh"

alias disk-free-space=$DISK_FREE_SPACE
alias disk-usage_dir=$DISK_USAGE_DIR

alias desc-disk-free-space="echo $DISK_FREE_SPACE"
alias desc-disk-usage_dir="echo $DISK_USAGE_DIR"



###############################################################
# Media

AUDIO_CD_RIP_TO_FLAC="abcde -o flac"
AUDIO_CD_RIP_TO_WAV="abcde -o wav"

alias audio-cd-rip-to-flac="$AUDIO_CD_RIP_TO_FLAC"
alias audio-cd-rip-to-wav="$AUDIO_CD_RIP_TO_WAV"
alias desc-audio-cd-rip-to-flac="echo $AUDIO_CD_RIP_TO_FLAC"
alias desc-audio-cd-rip-to-wav="echo $AUDIO_CD_RIP_TO_WAV"


