import requests

# Set the base URL of your Miningcore instance
base_url = 'https://getablocks.com/api'

def get_all_pools(base_url):
    pools_url = f"{base_url}/pools"
    response = requests.get(pools_url)
    response.raise_for_status()
    try:
        return response.json()
    except ValueError:
        print("Error: Unable to parse response as JSON.")
        print("Response content:", response.content.decode('utf-8'))
        raise

def get_pool_stats(base_url, pool_id):
    stats_url = f"{base_url}/pool/{pool_id}/stats"
    response = requests.get(stats_url)
    response.raise_for_status()
    try:
        return response.json()
    except ValueError:
        print(f"Error: Unable to parse response as JSON for pool {pool_id}.")
        print("Response content:", response.content.decode('utf-8'))
        raise

def main():
    try:
        pools_data = get_all_pools(base_url)
        
        print("Debug: pools_data type:", type(pools_data))
        if isinstance(pools_data, dict):
            print("Debug: pools_data content:", pools_data)
        
        if not isinstance(pools_data, list):
            print("Unexpected data format for pools_data. Expected a list.")
            print("pools_data:", pools_data)
            return
        
        total_miners = 0
        total_blocks = 0

        for pool in pools_data:
            if isinstance(pool, dict):
                pool_id = pool.get('id')
                
                stats_data = get_pool_stats(base_url, pool_id)
                total_miners += stats_data.get('connectedMiners', 0)
                total_blocks += stats_data.get('poolStats', {}).get('validBlocks', 0)
            else:
                print("Unexpected data format for pool entry. Expected a dictionary.")
                print("pool:", pool)
        
        print("Total Information Across All Pools:")
        print(f"Total Connected Miners: {total_miners}")
        print(f"Total Blocks Found: {total_blocks}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
