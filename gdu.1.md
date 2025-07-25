---
date: {{date}}
section: 1
title: gdu
---

# NAME

gdu - Pretty fast disk usage analyzer written in Go

# SYNOPSIS

**gdu \[flags\] \[directory_to_scan\]**

# DESCRIPTION

Pretty fast disk usage analyzer written in Go.

Gdu is intended primarily for SSD disks where it can fully utilize
parallel processing. However HDDs work as well, but the performance gain
is not so huge.

# OPTIONS

**-h**, **\--help**\[=false\] help for gdu

**-i**, **\--ignore-dirs**=\[/proc,/dev,/sys,/run\]
    Paths to ignore (separated by comma).
    Supports both absolute and relative paths.

**-I**, **\--ignore-dirs-pattern**
    Path patterns to ignore (separated by comma).
    Supports both absolute and relative path patterns.

**-X**, **\--ignore-from**
    Read path patterns to ignore from file.
    Supports both absolute and relative path patterns.

**-l**, **\--log-file**=\"/dev/null\" Path to a logfile

**-m**, **\--max-cores** Set max cores that Gdu will use.

**-c**, **\--no-color**\[=false\] Do not use colorized output

**-x**, **\--no-cross**\[=false\] Do not cross filesystem boundaries

**-H**, **\--no-hidden**\[=false\] Ignore hidden directories (beginning with dot)

**-L**, **\--follow-symlinks**\[=false\] Follow symlinks for files, i.e. show the
size of the file to which symlink points to (symlinks to directories are not followed)

**-n**, **\--non-interactive**\[=false\] Do not run in interactive mode

**-p**, **\--no-progress**\[=false\] Do not show progress in
non-interactive mode

**-u**, **\--no-unicode**\[=false\] Do not use Unicode symbols (for size bar)

**-s**, **\--summarize**\[=false\] Show only a total in non-interactive mode

**-t**, **\--top**\[=0\] Show only top X largest files in non-interactive mode

**-d**, **\--show-disks**\[=false\] Show all mounted disks

**-a**, **\--show-apparent-size**\[=false\] Show apparent size

**-C**, **\--show-item-count**\[=false\] Show number of items in directory

**-M**, **\--show-mtime**\[=false\] Show latest mtime of items in directory

**\--si**\[=false\] Show sizes with decimal SI prefixes (kB, MB, GB) instead of binary prefixes (KiB, MiB, GiB)

**\--no-prefix**\[=false\] Show sizes as raw numbers without any prefixes (SI or binary) in non-interactive mode

**\--mouse**\[=false\] Use mouse

**\--no-delete**\[=false\] Do not allow deletions

**-f**, **\--input-file** Import analysis from JSON file. If the file is \"-\", read from standard input.

**-o**, **\--output-file** Export all info into file as JSON. If the file is \"-\", write to standard output.

**\--config-file**=\"$HOME/.gdu.yaml\"             Read config from file

**\--write-config**\[=false\] Write current configuration to file (default is $HOME/.gdu.yaml)

**-g**, **\--const-gc**\[=false\] Enable memory garbage collection during analysis with constant level set by GOGC

**\--enable-profiling**\[=false\] Enable collection of profiling data and provide it on http://localhost:6060/debug/pprof/

**\--use-storage**\[=false\] Use persistent key-value storage for analysis data (experimental)

**-r**, **\--read-from-storage**\[=false\] Read analysis data from persistent key-value storage

**-v**, **\--version**\[=false\] Print version

# FILE FLAGS

Files and directories may be prefixed by a one-character
flag with following meaning:

**!**

:   An error occurred while reading this directory.

**.**

:   An error occurred while reading a subdirectory, size may be not correct.

**\@**

:  File is symlink or socket.

**H**

:  Same file was already counted (hard link).

**e**

:  Directory is empty.
