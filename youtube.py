""" channels """
from pafy.pafy import new
from vlc import MediaPlayer

channels = {"dd news":"https://www.youtube.com/watch?v=EaOsJRru-YQ",
            "dd india": "https://www.youtube.com/watch?v=JeJrQNWgeV4",
            "dd spots": "https://www.youtube.com/watch?v=BJOGi1Wa-Pc",
            }

class Channel():
    """ channel class """
    def inputname(self):
        name = str(input("Enter the channel Name: "))
        return name
    def add(self):
        name = self.inputname()
        url = str(input("Enter the channe's URL: "))
        channels[name]=url
        print("channel %s is added to the channel list" % name)

    def play(self):
        print("Available channels are: ")
        for this in channels:
            print(this)
        name=self.inputname()
        url = channels[name]
        print(url)
        video=new(url)
        playable = video.getbest()
        media = MediaPlayer(playable.url)
        media.play()
    def remove(self):
        name=self.inputname()
        try:
            pop(channel[name])
            print("Channel %s is removed from the list" % name)
        except:
            print("please check the channel name")
    def choose(self):
        print("what you want to do, add, play or delete a channel \n options are: \n 1. add a channel \n 2. Delete a channel \n 3. Play a channel")
        try:
            in_put = int(input("Enter the number from given options: "))
        except:
            print("error")
        return in_put
    def aply(self,in_put):
        if in_put == 1:
            self.add()
        elif in_put == 2:
            self.remove()
        elif in_put == 3:
            self.play()
        else:
            print("please choose a valid option")

    
        
        
if __name__=="__main__":
    print("it only works for live youtube TV channels")
    ch = Channel()
    while 1:
        in_put = ch.choose()
        ch.aply(in_put)
    
