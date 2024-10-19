Prerequistes-
pip install watchdog



Libraries used
1)	Os    
1.	Scandir() – Iterates over files and directories in a folder
2.	Rename(),exists()
2)	shutil.move()
3)	time.sleep() pauses exec. For a duration
4)	logging- logs events and provides details if a file is moved
5)	watchdog.observers( ) and .filesystemhandler 
monitors a direc and triggers when changes occur


Source direc and distination dir
Helper files unique-checks if file is unique provides counter eg-page will become page(1) if exists page(2)
 and move_file- calls unique func if exits or else calls shutil.move()

Move handler
Check what kind of file it is if jpeg,jpg it goes to images
.mp2,.mp4,.mv4 all are regarded as video
Audio and dif. By file size tht is 10MB
Checks handler and with the help of check audio video files etc 
Main block
Set up logging with its configuration of date and message
Call the MoverHandler() and observer() function
Observer calls the event handler recursively through the path
(using observer.schedule(MoverHandler(),path,recursive=True)
Observer.start()
*start the observer
Observer.join()
*joins paths in a platform independent way


