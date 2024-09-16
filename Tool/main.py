





import requests
import cfscrape 
import time
import sys
import os


scraper = cfscrape.create_scraper()
Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}


R = '\033[31m' # red 
G = '\033[32m' # green 
Y = '\033[33m' # yellow
E = '\033[0m' # end


def request_(url,filename):
    
    time.sleep(1)
    try:
        req_res = requests.get(url)
        with open(filename,"w") as f:
            f.write(req_res.content.decode())
            return True            
            

    except:
        return False


def cfscrape(url,filename):
    
    time.sleep(1)
    try:
        cfs_res = scraper.get(url,headers=Headers)
        with open(filename,"w") as f:
            f.write(cfs_res.content.decode())
            return True


    except:
        return False
        
        


def main():
    
    if len(sys.argv) == 3:
        
        link = sys.argv[1]
        filename = sys.argv[2]
                
        req_response = request_(link,filename)
        if req_response is True:
            print(f"{Y}[$]{E} file successfully saved in {G}{os.getcwd()}/{filename}{E}")
            sys.exit(0)
            
        elif req_response is False:
            print(f"{R}{req_response}{E} : Some kind of WAF might blocking the connection !! Trying again") 
            
            
            cfs_response = cfscrape(link,filename)
            if cfs_response is True:
                print(f"{Y}[$]{E} file successfully saved in {G}{os.getcwd()}/{filename}{E}")
                
            elif cfs_response is False:
                print(f"{Y}[!]{R}Failed to establish connection{E}")          
                sys.exit(1)      
                

    else:
        print(f"{R}[!]{Y}READ THE MANUAL BEFORE USE{E}")





if __name__ == '__main__':
    main()

