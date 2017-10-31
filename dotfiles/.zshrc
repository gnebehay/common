# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="robbyrussell"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git vi-mode command-not-found)

# User configuration

# export PATH="/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
# export MANPATH="/usr/local/man:$MANPATH"

DISABLE_AUTO_UPDATE="true"

source $ZSH/oh-my-zsh.sh

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#

### Begin customization
unsetopt share_history
autoload -Uz compinit promptinit
compinit
promptinit

zstyle ':completion:*' special-dirs true

setopt automenu
#setopt menucomplete

bindkey "^R" history-incremental-search-backward
bindkey '^N' expand-or-complete
bindkey '^P' reverse-menu-complete
bindkey '^O' accept-line
bindkey '^[OH' beginning-of-line
bindkey -a '^[OH' beginning-of-line
bindkey '^[OF' end-of-line
bindkey -a '^[OF' end-of-line
bindkey '^[[3~' delete-char
bindkey -a '^[[3~' delete-char
bindkey '^[[5~' up-line
bindkey -a '^[[5~' up-line
bindkey '^[[6~' down-line
bindkey -a '^[[6~' down-line

bindkey -s "^[OM" "^M"

alias rmt=gvfs-trash
alias cp='cp -i'
alias rm='rm -i'
alias mv='mv -i'
alias xclip='xclip -selection c'
alias python='python3'
alias pip='pip3'
alias ipython='ipython3'
alias mysql="mysql --pager='less -S'"

export DROPBOX="/home/$USER/Dropbox"

if [ "$USER" = "locatee" ]; then
  DROPBOX='/home/locatee/Dropbox (Locatee)'
fi

#The latter one is for locatee only
export PYTHONPATH="$DROPBOX/common/py:$DROPBOX/experiments/locatee-test"
export PATH="/sbin:/home/$USER/.local/bin:$DROPBOX/common/bin:$PATH"
export HISTTIMEFORMAT="%d/%m/%y %T "
export EDITOR=vi
