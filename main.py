import multiprocessing
import software
import time
from pyfiglet import Figlet

if __name__ == '__main__':

    f = Figlet(font='slant')
    print(f.renderText('Homemaker'))

    processes = {}
    # Call the main function for each piece of software in the software package.
    for module in software.__all__:
        process = multiprocessing.Process(target=getattr(software, module).main)
        process.start()
        processes[module] = process
    
    # Wait for all processs to finish.
    # Display whether each process has finsihed or not.
    spinner_chars = ['-', '\\', '|', '/']
    i = 0
    alive_processs = False
    while alive_processs:
        alive_processs = False
        process_count = 0
        for name, process in processes.items():
            process_count += 1
            if process.is_alive():
                print(name + spinner_chars[i])
                alive_processs = True
            else:
                process.join()
                if process.exitcode == 0:
                    # print green checkmark
                    print(name + ' \u2713')
                else:
                    # Print red x if the process failed.
                    print('\033[91m' + name + '✗' + '\033[0m')
        # Reset cursor to the top of this display.
        print('\033[{}A'.format(process_count))
        i = 1 % len(spinner_chars)
        time.sleep(0.05) # 50ms
    