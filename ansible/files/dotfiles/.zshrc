if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export ZSH="$HOME/.oh-my-zsh"
export PATH="${PATH}:${HOME}/.local/bin/"
export EDITOR="nano"
export TERM=xterm-256color


cat ~/.cache/wal/sequences

source ~/.cache/wal/colors-tty.sh

ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
#    zsh-autocomplete
    ssh-agent
    gpg-agent

    z
)

source $ZSH/oh-my-zsh.sh

# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
alias hyprcfg="code ${HOME}/.config/hypr/hyprland.conf"
alias waycfg="code ${HOME}/.config/waybar"

alias tf="terraform"

eval "$(direnv hook zsh)"


[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh


GPG_TTY=$(tty)
export GPG_TTY

alias ansible-playbook="ANSIBLE_COW_PATH=/home/ditrames/proggraming/infra/the-cows/cowsayrb ansible-playbook"

neofetch
cal


