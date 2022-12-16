#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$CURRENT_DIR/settings.sh"

get_width() {
	local key_bindings=$(get_tmux_option "$width" "$default_width")
	local key
	for key in $key_bindings; do
		local value=$key
	done
	echo "$value"
}

get_height() {
	local key_bindings=$(get_tmux_option "$height" "$default_height")
	local key
	for key in $key_bindings; do
		local value=$key
	done
	echo "$value"
}

get_from() {
	local key_bindings=$(get_tmux_option "$from" "$default_from")
	local key
	for key in $key_bindings; do
		local value=$key
	done
	echo "$value"
}

get_to() {
	local key_bindings=$(get_tmux_option "$to" "$default_to")
	local key
	for key in $key_bindings; do
		local value=$key
	done
	echo "$value"
}

get_engine() {
	local key_bindings=$(get_tmux_option "$engine" "$default_engine")
	local key
	for key in $key_bindings; do
		local value=$key
	done
	echo "$value"
}

vars=$(echo "$(get_engine)" | sed "s/|/\n/g")
while IFS= read -r line; do
    ver=`grep -oP 'VERSION_ID="\K[\d.]+' /etc/os-release`
    # echo "$ver"
    if [ "$ver" = "16.04" ];then
        result="${result}echo ---$line---; tmux save-buffer - | xargs -I{} ~/.pyenv/versions/3.8.5/bin/python $CURRENT_DIR/engine/translator.py --engine=$line --from=$(get_from) --to=$(get_to) {}; echo ''; "
    else
        result="${result}echo ---$line---; tmux save-buffer - | xargs -I{} python $CURRENT_DIR/engine/translator.py --engine=$line --from=$(get_from) --to=$(get_to) {}; echo ''; "
    fi
done <<< "$vars"
#result="${result}read -r"
result="${result}"

#tmux popup -w $(get_width) -h $(get_height) -E "$result"
tmux popup -w $(get_width) -h $(get_height)  "$result"
