# pyStockSeeder
Stock Data Seeder

The Stock Seeder is exactly that. A tool for getting basic stock data and historical stock daily results with which to start your stock history inquest. 

Ideally this tool is focused at people who have some grasp of what the Python language is and how it can be used. However, simply following the instructions will generate a foundational stock history file, complete with most of the stocks in the S&P 1500 (large, mid, small cap), that you may import into a database or use within some other technical context. 


## Stuff to Know

* This application retrieves historical stock data from https://eodhistoricaldata.com/. It is a pay service. If you do not have a subscription, it will severely limit the benefits of this script.

* The Python programming language and several python libraries will need to be installed to execute these scripts
    * It was built using Python 3.6.4 but should probably work with anything that starts with 3.
    * It uses the following libraries which can be installed with pip: 
        * json 
        * BeautifulSoup4
        * os
        * pandas
        * requests
        * sys
     * There is a configuration file that is necessary to run the commands. It will be called config.json and a sample template is provided called example-config.json which you will have to edit at least a very small amount before running the script.
     * This application relies on data from both wikipedia and nasdaq.com to work. I don't own those sites. If they break, it will break. But, the good news is that this seeder should only have to be run once. So, get in while it's early and you'll hopefully have nothing to worry about. 
     
     
## How to Run It
This application is very simple to set up and run if you follow the instructions here: 

1. clone this repository to your computer in a directory that is easy to access from the command line (Conda, Cmder, Powershell, etc.). It should run on a Mac or Linux environment probably much easier that Windows but I haven't tested it yet.

2. As mentioned above, make sure that Python and the suggested libraries are installed. I could explain this but there is much better info on the internet and it will save us both time if I don't. 

3. Open the example-config.json file and edit the "eodAPItoken" property where it says "your-key-goes-here". You will replace it with a key from https://eodhistoricaldata.com/, as mentioned above. You really shouldn't have to edit any other values in the config unless you want to (at your own risk). SAVE THE FILE AS *config.json*. 

4. Open your command line tool and navigate to the location where you placed the files. You should see BuildHistoryFile.py, GetIndexStocks, and the config file among others. Run the following commands: 

```
python GetIndexStocks.py
```
*this execution make take some time.*


```
python BuildHistoryFile.py
```
*this one should go somewhat quickly.*
     
    
