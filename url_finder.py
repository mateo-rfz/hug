import requests

"""
explain variable name :
send : send requests to sound cloud
main : the root variable for changes
counters : counter number for while loops
delete : delete parts of html text
"""

class Finder :
    def __init__ (self) :
        pass
    

    def finder_url(search) :
        
        def request(url):
            send = requests.get(url)
            return send.text
        
        main = request(f"https://soundcloud.com/search?q={search}")
        main = main.replace("<ul>" , "þ")
        main = main.replace("</ul>" , "Þ")

        counter1 = 0 
        counter2 = 0
        counter3 = 0
        while True :
            delete1 = main[counter1]
            if delete1 == "þ" :
                part1 = main[:counter1]
                main = main.replace(part1 , "")
                main = main.replace(main[0] , "")
                break
            
            counter1 = counter1 + 1
            
        while True :
            delete2 = main[counter2]
            if delete2 == "Þ" :
                part2 = main[:counter2]
                main = main.replace(part2 , "")
                main = main.replace(main[0] , "")
                break
            
            counter2 = counter2 + 1
            
        main = main.replace('<li><h2><a href="' , "œ")


        while True :
            delete3 = main[counter3]
            if delete3 == '"':
                part3 = main[counter3:]
                main = main.replace(part3 , "")
                break
            
            counter3 = counter3 + 1
            
        main = main.strip()
        main = main.replace("œ" , "")

        main = (f"https://soundcloud.com{main}")

        return main 