INSTRUCTIONS

The code is in project/chain-replication.da file
To execute just run the command - 
python3 -m da -f project/chain-replication.da



MAIN FILES

There is only one main file project/chain-replication.da.

The log file is in project/chan-replication.da.log
In LOGS the [Server] marked logs are sent from server and [Client] marked logs are sent from clients

It contains a Client class and a Bank Server class. These are the two important class.
The configuration is given in JSON format.
A sample JSON is present in project/config.json

The format is as below

{
  "config": [
    {
      "bank_name": "<name of the bank>",
      "length_of_chain": Integer,
      "number_of_clients": Integer,
      "startUpDelay": Integer (optional),
      "clients": [
        {
          "ip_address": "IP address",
          "operation": [
            {
              "type": "random (can be random or getDeposit,getBalance and withdraw)",
              "amount": "random (can be integer)",
              "request_id": "random (can be integer)",
              "accountNumber": "random (can be integer)"
            }
          ]
        }
      ]
    }
  ]
}
]

the main() method has the code to parse the JSON and call setup methods of client and server and start the client and server.

LIMITATION

The delay is common for client and server. Individual delay for each client and Server will be implemented in Phase 3.

CONTRIBUTION

The algorithm was written together and implementation was discussed in two langauges. The actual code in python is written by Devashish and the code in Elixir is written by Kaushik.
