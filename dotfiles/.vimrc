colorscheme ron

filetype plugin on
filetype indent on

syntax on

inoremap <C-H> <C-X><C-F>
nmap K i<CR><Esc>k$
nmap <C-i> o<Esc>k
nmap <C-o> O<Esc>j
noremap Y y$

set wildmenu
set wildmode=longest,list
set ignorecase
set incsearch
set nofoldenable
set number
set splitright
set directory=/tmp
set undodir=/tmp " where to save undo histories
set undofile                " Save undo's after file closes
set nowritebackup
set tabstop=4
set shiftwidth=4
set expandtab

set laststatus=1
set noshowcmd
set scrolloff=2