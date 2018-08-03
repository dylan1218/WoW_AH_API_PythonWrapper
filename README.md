# WoW_AH_API_PythonWrapper
Simple python wrapper for the WoW Auction House API. Provides a simple means to load the latest AH data for a given realm.


See usage below:
#Iniatlize the required inputs. The third argument is a function which grabs your IP which is a required argument for the Blizzard API endpoint. 
#You can enter your IP manually or get it through another means if preferred
class1 = AuctionHouse("moon guard", "273c9wsur533aj6tvpjhjgmx79dpycyn", AuctionHouse.get_Host_name_IP("self"))


#This loads the AuctionHouse data to a Json Dictionary and a dataframe.
#Pandas is not a requirement but is helpful for analysis.
JsonRawData =  class1.GetFullAH()
df = pd.DataFrame(JsonRawData['auctions'])
