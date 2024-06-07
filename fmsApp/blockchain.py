from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


# Get the first account from Ganache
account = web3.eth.accounts[0]

# Smart contract ABI (obtained from Remix IDE)
contract_abi = json.loads('''

[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "logId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "method",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "contentType",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "objectId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "objectName",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"name": "LogAdded",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "method",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "contentType",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "objectId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "objectName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"name": "addLog",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAllLogs",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "logId",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "method",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "contentType",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "objectId",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "objectName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "user",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "date",
						"type": "string"
					}
				],
				"internalType": "struct SystemLog.LogEntry[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getLog",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "logId",
				"type": "uint256"
			}
		],
		"name": "getLogById",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getLogCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "logById",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "logId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "method",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "contentType",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "objectId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "objectName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "logs",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "logId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "method",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "contentType",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "objectId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "objectName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "nextLogId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

''')

# Deployed contract address (obtained from Remix IDE)
contract_address = "0x6B3e7f2efa383bd5dB1487425113aeedC0De38fA"

# Interact with the deployed contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


def test_connection():
    return web3.is_connected()


# Function to add a log
def add_log(method, content_type, object_id, object_name, user, date):
    tx_hash = contract.functions.addLog(method, content_type, object_id, object_name, user, date).transact(
        {'from': account})
    web3.eth.get_transaction_receipt(tx_hash)


# Function to get a log by ID
def get_log_by_id(log_id):
    return contract.functions.getLogById(log_id).call()


# Function to get all logs
def get_all_logs():
    return contract.functions.getAllLogs().call()
