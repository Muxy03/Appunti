[PAGINE MAN](https://linux.die.net/man/)

[PUNTATORI](./PDF/LAB2/Lezione3.pdf)

le stringhe terminano con '\\0'

stdin -> 0
stdout -> 1
stderr -> 2
fopen mode:
1. r -> reading -> Open text file for reading.  The stream is positioned at the beginning of the file.
2.  r+ -> Open for reading and writing.  The stream is positioned at the beginning of the file.
3. w -> Truncate  file  to zero length or create text file for writing.  The stream is positioned at the beginning of the file.
4.  w+ -> Open for reading and writing.  The file is created if it does not exist, otherwise it is  truncated.   The stream is positioned at the beginning of the file.
5. a -> Open for appending (writing at end of file).  The file is created if it does not exist.  The stream is positioned at the end of the file.
6. a+ -> Open for reading and appending (writing at end of file).  The file is created if it does not exist.   Output  is always appended to the end of the file.  POSIX is silent on what the initial read position is when using this mode.  For glibc, the initial file position for reading is at the beginning of  the  file,  but for Android/BSD/MacOS, the initial file position for reading is at the end of the file.

![[Pasted image 20230623022701.png]]

[man fprintf](https://linux.die.net/man/3/fprintf)

fclose() -> flushes the stream pointed to by stream (writing any buffered output data using fflush(3)) and closes the underlying file descriptor.

[man perror](https://linux.die.net/man/3/perror)

[man errno](https://linux.die.net/man/3/errno)

codici sui puntatori -> lezione 7

