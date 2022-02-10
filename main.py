import argparse
from colorama import Fore,Back,Style
from matplotlib import style
from subprocess import Popen,PIPE


class webReconPath:

    def __init__(self):

        print(Fore.RED+'\t\t\t\t\t\t\t\t==============================================')
        print('\t\t\t\t\t\t\t\t==============================================')
        print("\t\t\t\t\t\t\t\t=============INITILIAZED PROGRAM==============")
        print('\t\t\t\t\t\t\t\t==============================================')
        print('\t\t\t\t\t\t\t\t==============================================')
        print(Style.RESET_ALL)


    def executeRecon(self, wordlist, url):

        try:
            with open(wordlist, 'r') as words:
                for word in words:

                    cmd = Popen(
                        ['/bin/bash', '-c', 'curl -o /dev/null --write-out %{http_code} -H "User-Agent: OwnTool" '+url+'/'+word], 
                        stdout=PIPE, 
                        stderr=PIPE
                    )
                    stdoutdata,stderrdata = cmd.communicate()
                    result = stdoutdata.decode('utf-8')
                    if result == '200':
                        print(Fore.GREEN+'URL FOUND: '+url+'/'+word, end="")
                print(Style.RESET_ALL)
        except KeyboardInterrupt:
            print(Style.RESET_ALL)
        except Exception as e:
            print(f'ERROR: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--wordlist', help='path to wordlist file')
    parser.add_argument('--url', help='destination server')

    args = parser.parse_args()
    if args.wordlist == None or args.url == None:
        print('None arguments are given, use --help for options')
        exit(0) 
    ob = webReconPath()
    ob.executeRecon(args.wordlist, args.url)