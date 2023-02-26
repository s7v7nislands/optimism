import os
import json

# PWD: optimism root directory


def main():
  pjoin = os.path.join
  l1network = "bsc-testnet"
  deployment_dir = pjoin("packages/contracts-bedrock/deployments", l1network)


  contracts = os.listdir(deployment_dir)
  addresses = {}
  for c in contracts:
    if not c.endswith('.json'):
      continue
    data = read_json(pjoin(deployment_dir, c))
    addresses[c.replace('.json', '')] = data['address']

  print(json.dumps(addresses, indent=2))
  sdk_addresses = {}
  sdk_addresses.update({'AddressManager': '0x0000000000000000000000000000000000000000',
                         'StateCommitmentChain': '0x0000000000000000000000000000000000000000',
                         'CanonicalTransactionChain': '0x0000000000000000000000000000000000000000',
                         'BondManager': '0x0000000000000000000000000000000000000000',
                         })
  sdk_addresses['L1CrossDomainMessenger'] = addresses['Proxy__OVM_L1CrossDomainMessenger']
  sdk_addresses['L1StandardBridge'] = addresses['Proxy__OVM_L1StandardBridge']
  sdk_addresses['OptimismPortal'] = addresses['OptimismPortalProxy']
  sdk_addresses['L2OutputOracle'] = addresses['L2OutputOracleProxy']
  print(json.dumps(sdk_addresses, indent=2))


def read_json(path):
  with open(path, 'r') as f:
    return json.load(f)


if __name__ == '__main__':
  main()
