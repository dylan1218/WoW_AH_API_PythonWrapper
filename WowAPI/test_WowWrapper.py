from WoWWrapper import AuctionHouse
import pandas as pd

#Iniatlize the required inputs. The third argument is a function which grabs your IP which is a required argument for the Blizzard API endpoint. 
#You can enter your IP manually or get it through another means if preferred
class1 = AuctionHouse("moon guard", "ENTER_YOUR_API_HERE", AuctionHouse.get_Host_name_IP("self"))


#This loads the AuctionHouse data to a Json Dictionary and a dataframe.
#Pandas is not a requirement but is helpful for analysis.
JsonRawData =  class1.GetFullAH()
df = pd.DataFrame(JsonRawData['auctions'])
print(df.to_string())
