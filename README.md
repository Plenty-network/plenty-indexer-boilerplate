README

Environment:

-	Tezos blockchain 
-	Plenty defi amm 
-	DipDup framework 	v3.1
-	Python 			v3.9.7
-	Node 			v14.17.6
-	Poetry dependencies 
-	Postgress database
-	Hasura GraphQL

clone the plenty indexer code

install poetry in your work environment: https://python-poetry.org/docs/

run command $ poetry install


Install docker and docker compose in your work environment

After installing the packages and dependencies you have configure the Postgress database password 
and you have to configure an admin secret for Hasura. 
This has to be set in the dipdup.yml file, dipdup.env file and in the dipdup-docker.yml file. 



After configuring the work environment it’s now time for running the code for the first time. 
To run the code for the first time, a few steps must be taken first. The reason for this is that 
the indexer must first synchronize the data with Tezos blockchain before the hooks are executed. 
You do this by commenting out the job section in the dipdup.yml file. The job section in the dipdup.yml 
execute the hooks that are also defined in the yml file. 


steps: 

1.	Comment out the job section in the dipdup.yml file
2.	Navigate to the docker directory via the terminal in your IDE
3.	Run the following command $ docker-compose up –build 
4.	Run the code until the indexer is synchronized with the blockchain and has a REALTIME status in Hasura. (see chapter 3.3 in documentation)
5.	Close program with the keys option + c 
6.	Undo step 1, so that the hooks will be executed in the next run 
7.	Run the following command $ docker-compose up –build 

After following these steps, the indexer is running and will calculate the plenty and token stats that will be saved in the database. 
Via Hasura you can easily access this data. If you run the code locally go to the following link http://127.0.0.1:8080/  
and fill in the admin secret you have configured before. 


For more information we refer you to the documentation 

coming soon:

-	Extra data models: volume, liquidity and price (boilerplate for charts) 
-	Calculate historical price, volume and liquidity stats in dollars (charts)
-	Calculate buy and sell volume in dollars and percentages for each token
-	Calculate volume token in dollars over a longer period of time
-	And more 


for questions we invite you to our discord

https://discord.gg/N2fD7fZq




