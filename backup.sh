#!/bin/bash

backup_files="/home/kaobe"
dest="/home/kaobe/Desktop/Programming_Projects/Inter-Language_Projects/Backup/venv/include/Backups
"

day=$(date +%Y-%m-%d)
hostname=$(hostname -s)
archive_file="${day}_${hostname}.tar.gz"

echo "Backing up $backup_files to $dest/$archive_files"
date

tar czf $dest/$archive_file $backup_files

echo
echo "Backup finished"

echo
echo "Uploading to Drive"
./quickstart.py "${archive_file}"

echo
echo "Uploaded"

rm "$dest/$archive_file"