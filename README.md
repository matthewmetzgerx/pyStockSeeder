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
     * At the time of writing this, 06/06/2019, the first commit is being made. There are plans to expand this project that will come in time. To that end, some aspects of the operation may change as the idea and approach grow in size.
     
     
## How to Run It
This application is very simple to set up and run if you follow the instructions here: 

1. Clone this repository to your computer in a directory that is easy to access from the command line (Conda, Cmder, Powershell, etc.). It should run on a Mac or Linux environment probably much easier than Windows but I haven't tested it yet.

2. As mentioned above, make sure that Python and the suggested libraries are installed. I could explain this but there is much better info on the internet and it will save us both time if I don't. 

3. Open the example-config.json file and edit the "eodAPItoken" property where it says "your-key-goes-here". You will replace it with a key from https://eodhistoricaldata.com/, as mentioned above. You really shouldn't have to edit any other values in the config unless you want to (at your own risk). SAVE THE FILE AS *config.json*. 

4. Open your command line tool and navigate to the location where you placed the files. You should see BuildHistoryFile.py, GetIndexStocks.py, and the config file among others. Run the following commands: 

```
python GetIndexStocks.py
```
*this execution make take some time.*


```
python BuildHistoryFile.py
```
*this one should go somewhat quickly.*
     
if there are issues, they will likely be indicated by warning messaage. Since not all stocks in the S&P 1500 are of the Nasdaq, NYSE, or AMEX exchanges, there may be a few which do not get imported. That said, there will be a good base with which to start. 


## Moving Forward

Obviously this is a very small effort but some of the subsequent effort will related to automating data updates, creating visualization code, and creating and overall predictive evaluation machine. Depending on the extent to which those efforts grow, they may be put in separate repositories. Please reach out if you'd like to chat.


    
## Author
This project was created by [Mattew Metzger](https://matthewmetzgerx.github.io/). Please feel free to add me on [LinkedIn](https://www.linkedin.com/in/matthewmetzgerx/) (*please explain the context*).
